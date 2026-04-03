import typing as t
from threading import Thread

from qools.funcutils import DEFAULT_DELAY, DEFAULT_TIMEOUT, called_once


class TestCalledOnce:
    def test_called_once_returns_cached_result(self):
        call_count = 0

        @called_once
        def inc() -> int:
            nonlocal call_count
            call_count += 1
            return call_count

        assert inc() == 1
        assert inc() == 1

    def test_called_once_calls_function_once(self):
        call_count = 0

        @called_once
        def side_effect() -> None:
            nonlocal call_count
            call_count += 1

        side_effect()
        side_effect()
        side_effect()

        assert call_count == 1

    def test_called_once_with_args_and_kwargs(self):
        @called_once
        def add(a: int, b: int, *, offset: int = 0) -> int:
            return a + b + offset

        assert add(1, 2, offset=10) == 13
        assert add(99, 99) == 13

    def test_called_once_preserves_metadata(self):
        @called_once
        def documented_func() -> None:
            """Important docstring."""

        assert documented_func.__name__ == "documented_func"
        assert documented_func.__doc__ == "Important docstring."

    def test_called_once_with_none_return(self):
        @called_once
        def returns_none() -> None:
            return None

        assert returns_none() is None
        assert returns_none() is None

    def test_called_once_first_exception_returns_none(self):
        @called_once
        def raises() -> t.NoReturn:
            raise ValueError("boom")

        import pytest

        with pytest.raises(ValueError, match="boom"):
            raises()
        assert raises() is None

    def test_called_once_thread_safety(self):
        call_count = 0

        @called_once
        def slow_inc() -> int:
            nonlocal call_count
            call_count += 1
            return call_count

        results: list[t.Any] = []

        def worker() -> None:
            results.append(slow_inc())

        threads = [Thread(target=worker) for _ in range(10)]
        for th in threads:
            th.start()
        for th in threads:
            th.join()

        assert call_count == 1
        assert all(r == 1 for r in results)


class TestConstants:
    def test_default_timeout_value(self):
        assert DEFAULT_TIMEOUT == 5

    def test_default_delay_value(self):
        assert DEFAULT_DELAY == 0.5
