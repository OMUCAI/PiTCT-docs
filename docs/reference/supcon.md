---
title: supcon
---

# supcon(SUP,G,SPEC)

 computes the optimal supervisor SUP that achieves the supremal controllable subspecfication of SPEC w.r.t the plant G.

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `SUP`                        | string | name of the supervisor                                       | *required* |
| `G`                          | string | name of the plant                                            | *required* |
| `SPEC`                       | string | name of the specification                                    | *required* |


## Example

```
pitct.supcon('SUP','G','SPEC')

```
