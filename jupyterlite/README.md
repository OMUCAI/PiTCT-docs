# Local Development

## Install

in parent directory
```bash
uv sync --all-groups
```

## Put PiTCT wheel

```bash
gh release download --repo OMUCAI/PiTCT --pattern "*-pyodide_2025_*.whl" --dir custom_wheels
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