---
title: allevents
---

# allevents(ALL, G)

creates a one-state automaton ALL selflooped with all the events of G

### Parameters
| Name       | Type    | Description             |  Default   |
|------------|---------|-------------------------|------------|
| `ALL`      | string  | name of output outmaton | *required* |
| `G`        | string  | name of input automaton | *required* |


## Example

```python title="sample 1"
delta = [
    (0, 11, 1),
    (1, 10, 0)
]
Qm = [0]
pitct.create('G', 2, delta, Qm)

pitct.allevents('ALL', 'G')

```

```python title="sample 2"
delta = [
    (0, 11, 1),
    (1, 12, 2),
    (2, 11, 0),
    (2, 14, 3)
]
Qm = [0, 3]
pitct.create('G', 4, delta, Qm)

pitct.allevents('ALL', 'G')
```
