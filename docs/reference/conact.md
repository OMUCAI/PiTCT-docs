---
title: conact
---

# conact(DES1, DES2)

returns control data DAT for the supervisor DES2, which controls DES1

### Parameters
| Name       | Type    | Description                                                          |  Default   |
|------------|---------|----------------------------------------------------------------------|------------|
| `DAT`      | string  | name of the control data for the supervisor DES2. (.DAT file)        | *required* |
| `DES1`     | string  | name of the DES1, which is controlled by DES2.                       | *required* |
| `DES2`     | string  | name of the supervisor DES2.                                         | *required* |


## Example

```python title="sample 1"

DAT=pitct.conact('DES1', 'DES2')

```
