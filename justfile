test:
  uv run pytest tests

check:
  uv run ruff check --fix phylorun
  uv run pyright phylorun

format:
  uv run ruff format phylorun

build:
  rm -rf dist
  uv build

publish:
  just build
  uv version --bump minor
  source .env && uv publish --token $UV_PUBLISH_PASSWORD
