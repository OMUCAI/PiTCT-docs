# trim(new_name, plant_name)

is the trim (reachable and coreachable) substructure of DES

### Parameters
| Name           | Type      | Description               |  Default   |
|----------------|-----------|---------------------------|------------|
| `new_name`     | string    | new DES model name        | *required* |
| `plant_name`   | string    | plant DES model name      | *required* |


## Example

```python title="sample 1"
delta = [
    (0, 10, 1),
    (1, 11, 2),
    (2, 11, 0),
    (2, 13, 3)
]
Qm = [0, 1]
pitct.create("model_1", 4, delta, Qm)

pitct.trim("model_2", "model_1")
```

```python title="sample 2"
delta = [
    (0, 10, 1),
    (1, 11, 2),
    (2, 11, 0),
    (3, 13, 2)
]
Qm = [0, 3]
pitct.create("model_1", 4, delta, Qm)

pitct.trim("model_2", "model_1")
```
