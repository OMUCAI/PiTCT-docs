# mutex(NEW_DES, DES1, DES2, STATE_PAIRS)

creates reachable cartesian product of DES1, DES2, excluding STATE_PAIRS.

### Parameters
| Name          | Type    | Description                                                             |  Default   |
|---------------|---------|-------------------------------------------------------------------------|------------|
| `NEW_DES`     | string  | name of reachable cartesian product of DES1, DES2, excluding STATE_PAIRS| *required* |
| `DES1`        | string  | name of DES1                                                            | *required* |
| `DES2`        | string  | name of DES2                                                            | *required* |
| `STATE_PAIRS` | list    | name of state pairs excluded from new DES                               | *required* |


## Example

```python title="sample 1"
delta1 = [
    (0, 11, 1),
    (1, 13, 2),
    (2, 10, 3),
    (3, 15, 4),
    (4, 12, 5)
]
Qm1 = [5]
pitct.create("DES1", 6, delta1, Qm1)


delta2 = [
    (0, 21, 1),
    (1, 23, 2),
    (2, 20, 3),
    (3, 25, 4),
    (4, 22, 5)
]
Qm2 = [5]
pitct.create("DES2", 6, delta2, Qm2)


state_pairs = [
    (1,1),
    (2,2),
    (3,3),
    (4,4),
]


pitct.mutex("new_DES","DES1","DES2",state_pairs)
```

