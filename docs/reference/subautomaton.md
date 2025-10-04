---
title: subautomaton
---

# subautomaton(S,G,[states],[transitions])

create subautomaton S by removing [states] and [transitions] from G 

### Parameters
| Name         | Type      | Description                            | Default    |
|--------------|-----------|----------------------------------------|------------|
| `S`          | string    | name of output automaton               | *required* |
| `G`          | string    | name of innput automaton               | *required* |
| `states`     | string    | state list                             | *required* |
| `transitions`| TransList | transition list                        | *required* |


## Example

```python title="sample 1"
delta = [
    (0, 11, 1),
    (1, 10, 0),
    (1, 12, 2),
    (2, 13, 0),
    (0, 15, 3)
]
Qm = [0, 1]
pitct.create('G', 4, delta, Qm)

pitct.subautomaton(S,G,[2],[])

```
