# display_automaton(name: string [, convert: bool, color: bool]) -> AutomatonDisplay

Get AutomatonDisplay instance and display automaton.

#### Parameter 
| Name      | Type      | Description           | Default  |
|-----------|-----------|-----------------------|----------|
| `name`    | string    | DES model name        | *required* |
| `convert` | bool      | Apply and display String Event and String State | `True` |
| `color`   | bool      | Separate colors depending on whether the control is uncontrollable or controllable.  | `False` |

## Return

[AutomatonDisplay](./automaton_display.md) instance

## Example

```python title='render sample'
model = pitct.display_automaton('model')
model.render()
```
An image window will appear. If you are in a Jupyter environment, it will appear below the cell.


```python title="save sample"
model = pitct.display_automaton('model')
model.save('model')
```

The file is saved as "model.png" in the current directory.
