# create(G, statenum, trans, marker)

creates an automaton model (.DES file)

### Parameters
| Name         | Type      | Description               | Default    |
|--------------|-----------|---------------------------|------------|
| `G`          | string    | name of output automaton  | *required* |
| `statenum`   | int       | number of states          | *required* |
| `trans`      | TransList | list of transition tuples.<br>For more information, please see [TransList Type](#translist-type).| *required* |
| `marker`     | list      | list of marker states     | *required* |


### TransList Type

There are several options for writing transition tuples.

1. Number-type event (Traditional TCT)

    `(exit state: int, event: int, enter_state: int)`

    !!! note
        By default odd-number event is controllable and even-number event is uncontrollable.

    ```python
    trans: TransList = [
        (0, 11, 1),
        (1, 10, 0),
        (1, 12, 2),
    ]
    ```

2. String-type event (PyTCT Original)

    `(exit state: int, event: string, enter_state: int, 'u'[uncontrollable] or 'c'[controllable])`

    !!! note
        String-type events and number-type events cannot be mixed.

    ```python
    trans: TransList = [
        (0, 'run', 1, 'c'),
        (1, 'finish', 0, 'u'),
        (1, 'broken', 2, 'u'),
    ]
    ```

3. String-type event and string-type state (PyTCT Original)
    
    `(exit state: string, event: string, enter_state: string, 'u'[uncontrollable] or 'c'[controllable])`

    !!! note
        String-type states cannot be displayed on AutomatonDisplay after being processed by other functions such as sync.
    
    ```python
    trans: TransList = [
        ('idle', 'run', 'working', 'c'),
        ('working', 'finish', 'idle', 'u'),
        ('working', 'broken', 'repairing', 'u'),
    ]
    ```

## Example

```python title="sample 1"
delta = [
    (0, 11, 1),
    (1, 10, 0),
    (1, 12, 2),
    (2, 13, 0),
    (0, 15, 3)
]
Qm = [0, 1]
pitct.create('G', 4, delta, Qm)
```

```python title="sample 2"
delta = [
    (0, 'run', 1, 'c'),
    (1, 'finish', 0, 'u'),
    (1, 'broken', 2, 'u'),
    (2, 'repaired', 0, 'c'),
    (0, 'sold', 3, 'c')
]
Qm = [0,1]
pitct.create('G', 4, delta, Qm)
```

```python title="sample 3"
delta = [
    ('idle', 'run', 'running', 'c'),
    ('running', 'finish', 'idle', 'u'),
    ('running', 'broken', 'broken', 'u'),
    ('broken', 'repaired', 'idle', 'c'),
    ('idle', 'sold', 'sold', 'c')
]
Qm = ['idle', 'running']
pitct.create('G', 4, delta, Qm)
```
