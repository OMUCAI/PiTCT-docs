---
title: localize
---

# localize(['C1', 'C2'], 'G', 'SUP', ['G1','G2'])

computes local controllers for each agent such that their collective behavior is equivalent to that of the supervisor SUP.

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `C1`                         | string | name of the local controller for G1                          | *required* |
| `C2`                         | string | name of the local controller for G2                          | *required* |
| `SUP`                        | string | name of the supervisor                                       | *required* |
| `G`                          | string | name of the plant                                            | *required* |
| `G1`                         | string | name of agent 1                                              | *required* |
| `G2`                         | string | name of agent 2                                              | *required* |


## Example

```
pitct.localize(['C1', 'C2'],'G','SUP',['G1','G2'])

```
