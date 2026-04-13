#!/usr/bin/env bash

set -uo pipefail

OUTPUT_MD_FILE="output/integration-test-latest.md"
RAW_LOG_FILE="$(mktemp)"

run_suite() {
  local suite_name="$1"
  local label="$2"

  echo "========================================================================" | tee -a "$RAW_LOG_FILE"
  echo "RUNNING: ${label}" | tee -a "$RAW_LOG_FILE"
  echo "========================================================================" | tee -a "$RAW_LOG_FILE"

  TEST_SUITE="$suite_name" docker compose \
    -f deploy/docker-compose/docker-compose.yml \
    -f deploy/docker-compose/docker-compose.integration.yml \
    run --build --rm integration-tests 2>&1 | tee -a "$RAW_LOG_FILE"

  local rc=${PIPESTATUS[0]}
  if [[ $rc -eq 0 ]]; then
    echo "RESULT: PASS (${label})" | tee -a "$RAW_LOG_FILE"
  else
    echo "RESULT: FAIL (${label})" | tee -a "$RAW_LOG_FILE"
  fi
  echo | tee -a "$RAW_LOG_FILE"
  return $rc
}

frontend_rc=0
backend_rc=0

run_suite "frontend-backend" "Frontend-Backend Integration" || frontend_rc=$?
run_suite "backend-only" "Backend-Only Integration" || backend_rc=$?

echo "========================================================================" | tee -a "$RAW_LOG_FILE"
echo "OVERALL SUMMARY" | tee -a "$RAW_LOG_FILE"
echo "========================================================================" | tee -a "$RAW_LOG_FILE"
if [[ $frontend_rc -eq 0 ]]; then
  echo "- Frontend-Backend Integration: PASS" | tee -a "$RAW_LOG_FILE"
else
  echo "- Frontend-Backend Integration: FAIL" | tee -a "$RAW_LOG_FILE"
fi

if [[ $backend_rc -eq 0 ]]; then
  echo "- Backend-Only Integration: PASS" | tee -a "$RAW_LOG_FILE"
else
  echo "- Backend-Only Integration: FAIL" | tee -a "$RAW_LOG_FILE"
fi

if [[ $frontend_rc -eq 0 && $backend_rc -eq 0 ]]; then
  overall_result="PASS"
  exit_code=0
else
  overall_result="FAIL"
  exit_code=1
fi

echo "OVERALL RESULT: ${overall_result}" | tee -a "$RAW_LOG_FILE"

mkdir -p "$(dirname "$OUTPUT_MD_FILE")"
{
  echo "# Integration Test Run Output"
  echo
  echo "- Date: $(date '+%Y-%m-%d %H:%M:%S %Z')"
  echo "- Frontend-Backend Integration: $([[ $frontend_rc -eq 0 ]] && echo PASS || echo FAIL)"
  echo "- Backend-Only Integration: $([[ $backend_rc -eq 0 ]] && echo PASS || echo FAIL)"
  echo "- Overall Result: ${overall_result}"
  echo
  echo "## Full Console Output"
  echo
  echo '```text'
  sed 's/\r$//' "$RAW_LOG_FILE"
  echo '```'
} > "$OUTPUT_MD_FILE"

echo "Markdown report written to: ${OUTPUT_MD_FILE}"
rm -f "$RAW_LOG_FILE"

exit "$exit_code"
