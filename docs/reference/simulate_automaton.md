---
title: simulate_automaton
---

# simulate_automaton(G,[s])

simulate G.DES with a string s

### Parameters
| Name         | Type      | Description                            | Default    |
|--------------|-----------|----------------------------------------|------------|
| `G`          | string    | name of automaton                      | *required* |
| `s`          | string    | string                                 | *required* |


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

pitct.selfloop('G',['11,12,13'])

```
