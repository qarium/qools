# DevOps

## Config

| Key            | Value            | Description                                 |
|----------------|------------------|---------------------------------------------|
| ci_provider    | github-actions   | CI provider                                 |
| trigger_branch | 0.0.x            | Default branch for triggers                 |
| diff_range     | HEAD~5           | Git diff range for auto-analysis in feature |

## Rules

### Workflow Registry

| Workflow     | File               | Trigger                         | Purpose                                |
|--------------|--------------------|---------------------------------|----------------------------------------|
| Lint         | lint.yml           | push/PR to 0.0.x               | Ruff lint + format check               |
| Tests        | tests.yml          | push/PR to 0.0.x               | pytest on Python 3.10–3.14 matrix      |
| Docs         | docs.yml           | push to 0.0.x                  | mkdocs gh-deploy --force               |
| Publish      | publish.yml        | workflow_dispatch               | Build + publish to PyPI + GitHub Release |
| New Version  | new_version.yml    | workflow_dispatch               | Create X.Y.x branch, set as default   |
| Strictacode  | strictacode.yml    | push/PR to 0.0.x               | Code quality analysis                  |
| Notify       | notify.yml         | workflow_run after Publish Release | Telegram notification on release   |

### Conventions

## Lessons

| Problem | Why | How to prevent |
|---------|-----|----------------|
