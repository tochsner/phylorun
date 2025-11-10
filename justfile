test:
  uv run pytest tests

check:
  uv run ruff check --fix phylorun
  uv run pyright phylorun

format:
  uv run ruff format phylorun

update-jars:
  cp /Users/ochsneto/Documents/PhyloSpec/phylospec/core/java/target/phylospec-core-0.0.1-SNAPSHOT-jar-with-dependencies.jar phylorun/jars/convertToLPhy.jar

build:
  rm -rf dist
  uv build

publish:
  uv version --bump minor
  just build
  source .env && uv publish --token $UV_PUBLISH_PASSWORD
