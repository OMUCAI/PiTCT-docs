---
title: create
---

# create(name, size, trans, marker)

creates an automaton model of DES (a .DES file)

### Parameters
| Name     | Type      | Description           | Default  |
|----------|-----------|-----------------------|----------|
| `name`   | string    | DES model name        | *required* |
| `size`   | int       | number of state       | *required* |
| `trans`  | TransList | transition tuple.     | *required* |
| `marker` | list      | marker state list     | *required* |

## Example
```python
pitct.create()
```