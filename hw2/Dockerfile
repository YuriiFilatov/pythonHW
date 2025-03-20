FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends  texlive-latex-base && apt-get clean  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY scripts/ ./scripts
COPY pictures/ ./pictures

RUN pip install uv

COPY --link --from=ghcr.io/astral-sh/uv:0.4 /uv /usr/local/bin/uv

RUN cd scripts \
    && uv sync \
    && uv run main.py \
    && pdflatex result.tex
