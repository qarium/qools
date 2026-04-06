# qools

Utility tools from Qarium — a collection of Python utilities designed for simplicity and thread safety.

## Features

- **`funcutils.called_once`** — thread-safe decorator that ensures a function executes only once and returns the cached result on subsequent calls

## Quick Start

```python
from qools import funcutils

@funcutils.called_once
def init_connection():
    print("Connecting...")
    return "connected"

result = init_connection()
```

## Sections

- [Getting Started](getting-started.md) — installation and first steps
- [API Reference](api-reference.md) — detailed API documentation
