# Build Stage
FROM python:3.11.14-alpine3.23 AS builder

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --user --no-cache-dir --no-compile -r requirements.txt

# Production Stage
FROM python:3.11.14-alpine3.23

WORKDIR /app

COPY --from=builder /root/.local /root/.local 

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["python", "app.py"]
