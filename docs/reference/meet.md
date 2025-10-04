# meet(DES,DES1,DES2,...,DESk)

creates a reachable cartesian product of DES1, DES2, ..., DESk.

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `DES`                        | string | a reachable cartesian product of DES1, DES2, ..., DESk.      | *required* |
| `DES1, DES2, ..., DESk`      | string | DESs used to create a reachable cartesian product.           | *required* |


## Example

```python title="sample 1"
delta1 = [
    (0, 11, 1),
    (1, 10, 0)
]
Qm = [0]
pitct.create("DES1", 2, delta1, Qm)


delta2 = [
    (0, 10, 1),
    (1, 10, 2),
    (2, 11, 0),
]
Qm = [0]
pitct.create("DES2", 3, delta2, Qm)

pitct.meet("DES", "DES1", "DES2")

```
