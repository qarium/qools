# Lead

## Config

| Key            | Value  | Description                                  |
|----------------|--------|----------------------------------------------|
| default_branch | 0.0.x  | Default branch for CI triggers and diff base |

## Architecture & Decisions
- **setuptools-scm for dynamic versioning** — versions derived from git tags, agents must not hardcode versions in pyproject.toml
- **Branch `0.0.x` as default** — non-standard naming, affects CI triggers and diff bases
- **Template-based project bootstrap** — project initialized from qarium template with `${ROLE_*}` placeholders processed during employee onboarding; agents must not re-fill these values

## Project Structure
- **Single flat package layout (`qools/`)** — library without subdirectories, all modules at the top level
- **`funcutils.py` — functional utilities module** — decorators (`called_once`), constants; new decorators and helpers go here

## Code Patterns
- **Thread-safe singleton decorator** — `called_once` uses `threading.Lock` for safe concurrent lazy initialization
- **Submodule-style imports** — `from qools import funcutils` then `funcutils.called_once(...)`; `__init__.py` stays empty, no re-exports
- **`typing as t` convention** — all type hints use `t.` prefix instead of full paths

## TODO
- Fix `WrappedType` annotation in `funcutils.py:8` — replace `t.Callable[[...], t.Any]` with `t.Callable[..., t.Any]`, remove `# type: ignore[misc]`
- Fix exception-safety in `called_once` (`funcutils.py:21-23`) — move `is_called = True` after `rv = f(...)` so failed calls can be retried
- Remove unused constants `DEFAULT_TIMEOUT` and `DEFAULT_DELAY` from `funcutils.py:5-6`
- Add tests for `funcutils.py` in `tests/qools/test_funcutils.py`

## LLM Directives
<!-- empty -->

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
