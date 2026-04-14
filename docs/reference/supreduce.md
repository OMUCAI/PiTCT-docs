---
title: supreduce
---

# supreduce(RSUP,G,SUP,CONDAT)

 computes the optimal supervisor SUP that achieves the supremal controllable subspecfication of SPEC w.r.t the plant G.

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `RSUP`                       | string | name of the reduced supervisor                               | *required* |
| `SUP`                        | string | name of the supervisor                                       | *required* |
| `G`                          | string | name of the plant                                            | *required* |
| `CONDAT`                     | string | name of the control data                                     | *required* |


## Example

```
pitct.supreduce(RSUP,G,SUP,CONDAT)

```

