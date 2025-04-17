FROM python:3.12-slim
WORKDIR /src
COPY uv.lock pyproject.toml ./
RUN pip install --no-cache-dir uv
RUN uv sync
COPY . .
ENV PYTHONPATH="/src"
CMD ["uv", "run", "litestar", "--app", "backend.src.main:app", "run", "-r"]
