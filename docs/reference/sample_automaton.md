# sample_automaton(G,m)

sample G.DES with a string of length m

### Parameters
| Name       | Type    | Description      |  Default   |
|------------|---------|------------------|------------|
| `G`        | string  | name of DES      | *required* |
| `m`        | int     | length of string | *required* |



## Example

```python title="sample 1"
delta = [
    (0, 11, 1),
    (1, 12, 2),
    (2, 11, 0),
    (2, 14, 3)
]
Qm = [3]
pitct.create('G', 4, delta, Qm)

pitct.sample_automaton('G',2)
```
