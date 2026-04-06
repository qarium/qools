# qools

Utility tools from Qarium

## Installation

```bash
pip install qools
```

## Quick Start

```python
from qools import funcutils

@funcutils.called_once
def init_connection():
    print("Connecting...")
    return "connected"

# First call — executes the function
result = init_connection()  # Connecting...

# Subsequent calls — return cached result without execution
result = init_connection()  # (no output, returns "connected")
```

## API

### `funcutils`

Submodule-style import: `from qools import funcutils`.

| Name | Description |
|------|-------------|
| `called_once(f)` | Thread-safe decorator. Ensures the function is called only once; subsequent calls return the cached result. |
| `DEFAULT_TIMEOUT` | Constant `5` |
| `DEFAULT_DELAY` | Constant `0.5` |

## Documentation

Full documentation: https://qarium.github.io/qools/
