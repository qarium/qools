# Getting Started

## Installation

```bash
pip install qools
```

For local development:

```bash
git clone https://github.com/qarium/qools.git
cd qools
pip install -e ".[test,docs]"
```

## First Steps

The main module is `funcutils`, imported in submodule style:

```python
from qools import funcutils
```

### `called_once` — run once decorator

The `called_once` decorator ensures a function executes only once. All subsequent calls return the cached result without re-executing the function body. The decorator is thread-safe.

```python
from qools import funcutils

@funcutils.called_once
def load_config():
    print("Loading config...")
    return {"key": "value"}

# First call — executes the function
config = load_config()  # Loading config...

# Subsequent calls — return cached result
config = load_config()  # (no output, returns {"key": "value"})
```

Typical use cases:

- One-time initialization (database connections, config loading)
- Lazy singletons
- Expensive computations that should not repeat

!!! note
    If the first call raises an exception, the exception propagates to the caller, but the function is still marked as called — all subsequent calls return `None` without retrying. Wrap the first call in error handling if a retry may be needed.
