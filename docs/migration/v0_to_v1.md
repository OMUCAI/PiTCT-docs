# PyTCT v0 → v1 Migration Guide

This document explains the changes and steps required to migrate PyTCT from v0 to v1.

## 1. Changes (Overview)

- Package name change (the package name was changed because a duplicate name existed on PyPI)
    - old: `pytct` → new: `pitct`
- Changes related to source distribution/ownership (e.g. from closed-source to open-source)

## 2. Migration steps

Below are representative migration approaches. Choose the one that suits your project size and compatibility requirements.

### Method 1 — Keep compatibility (use an alias)

If you want to run existing code with minimal changes, import the new package under the old name as an alias.

```python
# Example: run old code unchanged in a v1 environment
import pitct as pytct

# After this you can call pytct.<function> as before
pytct.init("xxx")
```

The advantage of this approach is that it minimizes code diffs. The downside is that you will still need to migrate to the official name (`pitct`) at some point.

### Method 2 — Replace directly (recommended)

Replace occurrences in your codebase to use the new package name explicitly. This is the recommended long-term approach.

```python
# v1 usage (recommended)
import pitct

pitct.init("xxx")
```

A simple search-and-replace (for example: replace "pytct" with "pitct" across the project) will often be sufficient, but be sure to run tests and builds to confirm there are no issues.

