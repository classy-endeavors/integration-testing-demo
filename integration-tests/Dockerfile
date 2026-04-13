FROM python:3.12-slim

WORKDIR /tests

COPY integration-tests/requirements.txt /tests/requirements.txt
RUN pip install --no-cache-dir -r /tests/requirements.txt

COPY integration-tests /tests

CMD ["pytest", "-q", "test_sockshop.py"]
