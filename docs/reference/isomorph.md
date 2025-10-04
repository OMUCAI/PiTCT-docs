---
title: isomorph
---

# isomorph(DES1,DES2)

verify if two automata (DES1,DES2) are the same (modulo relabeling states and events)

### Parameters
| Name                         | Type   | Description                                                  |  Default   |
|------------------------------|--------|--------------------------------------------------------------|------------|
| `DES1`                       | string | automaton model name                                         | *required* |
| `DES2`                       | string | automaton model name                                         | *required* |


## Example

```

pitct.isomorph('DES1', 'DES2')

```

