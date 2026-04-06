# API Reference

## `funcutils`

Submodule-style import: `from qools import funcutils`

### Functions

#### `called_once(f)`

Thread-safe decorator that ensures the decorated function is called only once. On the first invocation, the function executes normally and the result is cached. All subsequent calls return the cached result without re-executing the function body.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `f` | `Callable` | Function to wrap |

**Returns:** `Callable` — a wrapper function with the same signature as `f`.

**Example:**

```python
from qools import funcutils

@funcutils.called_once
def create_service():
    print("Creating service...")
    return Service()

service = create_service()  # Creating service...
service = create_service()  # cached, no output
```

### Constants

| Name | Type | Value | Description |
|------|------|-------|-------------|
| `DEFAULT_TIMEOUT` | `int` | `5` | Default timeout value |
| `DEFAULT_DELAY` | `float` | `0.5` | Default delay value |

### Type Aliases

| Name | Definition | Description |
|------|------------|-------------|
| `WrappedType` | `Callable[[...], Any]` | Type alias for wrapped callable signatures |
