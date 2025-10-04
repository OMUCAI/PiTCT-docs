# shortest_string(G,m,n)

generate a shortest string from state m (which need not be the initial state) to another (reachable) state n

### Parameters
| Name       | Type    | Description      |  Default   |
|------------|---------|------------------|------------|
| `G`        | string  | name of DES      | *required* |
| `m`        | int     | state number     | *required* |
| `n`        | int     | state number     | *required* |



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

pitct.shortest_string('G',1,3)
```
