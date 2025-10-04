---
title: sync
---

# sync(DES,DES1,DES2,...,DESk)

creates a (reachable) synchronous product of DES1,DES2,...,DESk. 

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `DES`                        | string | synchronous product of DES1,DES2,...,DESk.                   | *required* |
| `DES1, DES2, ..., DESk`      | string | DESs used to create a synchronous product.                   | *required* |


## Example

```python title="sample 1"
delta1 = [
    (0, 10, 1),
    (1, 12, 0),
]
Qm = [0]
pitct.create("DES1", 2, delta1, Qm)


delta2 = [
    (0, 11, 1),
    (1, 10, 2),
    (2, 10, 0),
]
Qm = [0]
pitct.create("DES2", 3, delta2, Qm)

pitct.sync("DES", "DES1", "DES2")

```
DES need not be coreachable

