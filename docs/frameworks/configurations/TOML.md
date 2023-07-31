## TOML - Tom's Obvious Markup Language

### Description

- TOML is a Markup language that is meant to create configurations for applications. The syntax is very easy to read and is accessible to get certain credentials easily.

### Use Cases

1. Accessing private information for a Streamlit application to connect successfully.

2. Setting up exact parameters that you need to connect to a database.

### Syntax

- TOML has support for key value pairs which have the format below:

```toml
"key" = "value"
```

- If you want to setup an object, you can write the `toml` configuration as follows:

```toml
["object name"]
"key_1" = "value_1"
"key_2" = "value_2"
```

- There are different data types available within `toml`.
  - Key / Value Pairs
  - Arrays
  - Tables
  - Array of Tables
  - Integers and Floats
  - Booleans
  - Dates and Times

### Accessing TOML with Python

#### Installation

- Install via `pip`

```bash
pip install toml
```

#### Example

```python
import toml

# Load a .toml file
data = toml.load('example.toml')
# Returns a dictionary

print(data)
```

### Resources

- [TOML Documentation](https://toml.io/en/)
