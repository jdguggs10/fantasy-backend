FROM python:3.12-slim
WORKDIR /code
COPY pyproject.toml poetry.lock* /code/
RUN pip install poetry && poetry install --no-root
COPY . /code
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8080"]
