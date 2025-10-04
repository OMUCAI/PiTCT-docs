# printdat(TXT, DAT)

convert a DAT file to a TXT file.

### Parameters
| Name       | Type    | Description                                              |  Default   |
|------------|---------|----------------------------------------------------------|------------|
| `TXT`      | string  | name of TXT file                                         | *required* |
| `DAT`      | string  | name of DAT file (control data)                          | *required* |


## Example

```python title="sample 1"

pitct.condat("DAT", "PLANT", "SUP")

pitct.printdat("TXT", "DAT")

```
