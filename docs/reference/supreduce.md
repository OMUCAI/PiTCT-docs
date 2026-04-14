---
title: supreduce
---

# supreduce(RSUP, G, SUP, CONDAT)

computes a reduced supervisor RSUP that preserves the control logic of the original supervisor SUP while reducing the number of states.

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

