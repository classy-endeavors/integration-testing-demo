import os
import subprocess
import sys


SUITES = {
    "frontend-backend": {
        "label": "Frontend-Backend Integration",
        "pytest_args": ["-m", "frontend_backend", "test_sockshop.py"],
    },
    "backend-only": {
        "label": "Backend-Only Integration",
        "pytest_args": ["-m", "backend", "test_backend_services.py"],
    },
    "all": {
        "label": "All Integration Suites",
        "pytest_args": [
            "test_sockshop.py",
            "test_backend_services.py",
        ],
    },
}


def print_header(title: str) -> None:
    line = "=" * 72
    print(line)
    print(f"RUNNING: {title}")
    print(line)


def main() -> int:
    suite = os.environ.get("TEST_SUITE", "all").strip().lower()
    selected = SUITES.get(suite)
    if selected is None:
        valid = ", ".join(SUITES.keys())
        print(f"Invalid TEST_SUITE '{suite}'. Valid values: {valid}")
        return 2

    print_header(selected["label"])
    cmd = ["pytest", "-s", "-vv", *selected["pytest_args"]]
    print(f"Command: {' '.join(cmd)}")
    print("-" * 72)
    completed = subprocess.run(cmd, check=False)
    print("-" * 72)
    if completed.returncode == 0:
        print(f"RESULT: PASS ({selected['label']})")
    else:
        print(f"RESULT: FAIL ({selected['label']})")
    print("=" * 72)
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
