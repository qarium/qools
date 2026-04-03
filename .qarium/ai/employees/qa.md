## Config

| Setting          | Value                                  |
|------------------|----------------------------------------|
| run_tests_cmd    | pytest --tb=short                      |
| lint_cmd         | ruff check qools/ tests/               |
| lint_fix_cmd     | ruff check --fix qools/ tests/         |
| format_cmd       | ruff format --check qools/ tests/      |
| format_fix_cmd   | ruff format qools/ tests/              |

## Rules

Project test configuration. Used by the `qarium:employees:qa:feature` skill.

### Mapping

| Source path pattern | Test directory     | Notes         |
|---------------------|--------------------|---------------|
| `qools/**/*.py`     | `tests/qools/`     | Mirror layout |

### Mock Patterns

| Pattern | Example |
|---------|---------|

### Helpers

| Helper | Location | Purpose |
|--------|----------|---------|

### Conventions

- Naming: `test_<what>_<scenario>`
- Never mock `builtins.open` — use `tmp_path` fixture
- Integration tests use `pytest.mark.skipif` when external tools unavailable

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
