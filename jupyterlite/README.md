# Local Development

## Install

in parent directory
```bash
uv sync --all-groups
```

## Build

```bash
jupyter lite build
uv run python ./patch/load_graphviz.py 
```

## Test

in parent directory
```bash
uv run python -m http.server --directory site 8000
```