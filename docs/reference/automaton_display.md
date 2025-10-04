# AutomatonDisplay(name: string [, convert: bool, color: bool])

Convert a DES file to Image

#### Parameter 
| Name      | Type      | Description           | Default  |
|-----------|-----------|-----------------------|----------|
| `name`    | string    | DES model name        | *required* |
| `convert` | bool      | Apply and display String Event and String State | `True` |
| `color`   | bool      | Separate colors depending on whether the control is uncontrollable or controllable.  | `False` |

## Method

### save(filename[, fileformat, layout, dpi, label, timelabel, **kwargs])
save image

#### Parameter
| Name      | Type      | Description           | Default  |
|-----------|-----------|-----------------------|----------|
| `filename`   | string | save file name        | *required* |
| `fileformat` | string | save file format e.g) png, jpeg, gif | `png` |
| `layout`     | str    | graphviz layout  | `dot` |
| `dpi`        | int    | image dpi  | `300` |
| `label`      | str    | header title  | `None` |
| `timelabel`  | bool   | whether to display time labels | `True` |
| `**kwargs`   |        | Additional graphviz attribute  | `{}` |


### render([layout, dpi, label, timelabel, format, **kwargs])
render image

#### Parameter
| Name      | Type      | Description           | Default  |
|-----------|-----------|-----------------------|----------|
| `layout`     | str    | graphviz layout  | `dot` |
| `dpi`        | int    | image dpi  | `300` |
| `label`      | str    | header title  | `None` |
| `timelabel`  | bool   | whether to display time labels | `True` |
| `format`     | string | file format e.g) png, jpeg, gif | `png` |
| `**kwargs`   |        | Additional graphviz attribute  | `{}` |


## Example

```python title'render sample'
model = pitct.AutomatonDisplay('model')
model.render()
```
An image window will appear. If you are in a Jupyter environment, it will appear below the cell.


```python title'save sample'
model = pitct.AutomatonDisplay('model')
model.save("model")
```

The file is saved as "model.png" in the current directory.
