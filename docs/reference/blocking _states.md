# blocking _states(DES)

generate all blocking states in DES

### Parameters
| Name       | Type    | Description                                                          |  Default   |
|------------|---------|----------------------------------------------------------------------|------------|
| `DES`      | string  | name of the blocking data for the DES.                               | *required* |


## Example

```python title="sample 1"

delta = [
    (0, 11, 1),
    (1, 12, 2),
    (2, 11, 0),
    (2, 14, 3)
]
Qm = [0]
pitct.create('DES', 4, delta, Qm)


pitct.blocking_states('DES')

```
