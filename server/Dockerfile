FROM python:3-slim as requirements
RUN apt-get update
RUN apt-get install -y build-essential cmake
RUN pip install poetry
COPY pyproject.toml poetry.lock /app/
WORKDIR /app
RUN poetry export --without-hashes > requirements.txt
RUN poetry export --without-hashes --dev > requirements.dev.txt
RUN pip install -r requirements.txt

FROM python:3-slim as base
COPY --from=requirements /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=requirements /app /app
WORKDIR /app
RUN python -m spacy download en_core_web_sm

FROM base as dev
RUN pip install -r requirements.dev.txt
COPY . /app
ENV PYTHONPATH=/app:$PYTHONPATH

FROM base as prod
COPY . /app
