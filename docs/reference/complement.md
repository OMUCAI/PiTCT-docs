---
title: complement
---

# complement(DESCo, DES, auxiliary event)

creates complement of DES

### Parameters
| Name       | Type    | Description                                              |  Default   |
|------------|---------|----------------------------------------------------------|------------|
| `DESCo`      | string  | name of DES that the marked behaviour is the complement of the marked behaviour of the original DES.| *required* |
| `DES`     | string  | name of original DES                                             | *required* |
| `auxiliary event`| list  | list of events that are not in the original DES, added to complement.  | *required* |

## Example

```python title="sample 1"
delta = [
    (0, 10, 1),
    (1, 11, 0),
]
Qm = [0]
pitct.create("G", 2, delta, Qm)

pitct.complement("Gco", "G", [])

```

```python title="sample 2"
delta = [
    (0, 10, 1),
    (1, 11, 0),
]
Qm = [0]
pitct.create("G", 2, delta, Qm)

pitct.complement("Gco", "G", [12,13])

```