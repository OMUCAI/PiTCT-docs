# transnum(name)

returns the number of DES transitions

### Parameters
| Name       | Type    | Description |  Default   |
|------------|---------|-------------|------------|
| `name`     | string  | name of DES | *required* |



## Example

```python title="sample 1"
delta = [
    (0, 11, 1),
    (1, 12, 2),
    (2, 11, 0),
    (2, 14, 3)
]
Qm = [3]
pitct.create("model", 4, delta, Qm)

pitct.transnum("model")
```
