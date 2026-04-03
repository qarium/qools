import typing as t
from functools import wraps
from threading import Lock

DEFAULT_TIMEOUT: t.Final = 5
DEFAULT_DELAY: t.Final = 0.5

WrappedType = t.Callable[[...], t.Any]  # type: ignore[misc]


def called_once(f: WrappedType) -> t.Callable:
    rv = None
    lock = Lock()
    is_called = False

    @wraps(f)
    def wrapper(*args: t.Any, **kwargs: t.Any) -> t.Any:
        with lock:
            nonlocal rv, is_called

            if not is_called:
                is_called = True
                rv = f(*args, **kwargs)

            return rv

    return wrapper
