# Tech Writer Config

## Config

| Key           | Value                      | Description                         |
|---------------|----------------------------|-------------------------------------|
| build_cmd     | `mkdocs build`             | Build validation command            |
| deploy_cmd    | `mkdocs gh-deploy --force` | Deploy command                      |
| examples_file |                            | File for usage examples (optional)  |
| logo_url      | `https://avatars.githubusercontent.com/u/262344922?s=200&v=4` | Standard qarium logo |
| base_branch   | `0.0.x`                    | Base branch for git diff comparison |

## Rules

### Mapping

| Source path | Documentation files |
|-------------|---------------------|
| `qools/__init__.py` | `docs/api-reference.md`, `docs/index.md` |
| `qools/*.py` | `docs/api-reference.md` |

### Conventions

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
| `docs/overrides/main.html` did not match template | Onboarding used minimal overrides instead of full template | Audit overrides during onboarding verification, compare with `.claude/templates/` |