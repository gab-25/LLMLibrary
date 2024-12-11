FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY . .
RUN poetry install --with test

ENTRYPOINT ["poetry", "run", "pytest", "./tests", "-v"]
