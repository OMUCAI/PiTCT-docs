---
title: is_controllable
---

# is_controllable(G1,G2)

verify whether or not automaton G2 is controllable with respect to automaton G1

### Parameters
| Name       | Type    | Description             |  Default   |
|------------|---------|-------------------------|------------|
| `G1`       | string  | name of plant automaton | *required* |
| `G2`       | string  | name of automaton       | *required* |


## Example

```python title="sample 1"

pitct.is_controllable('G1','G2')

```
