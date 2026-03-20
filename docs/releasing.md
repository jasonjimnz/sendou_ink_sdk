# Releasing

This project uses GitHub Actions for release automation.

## Workflows

- `deploy-docs.yml`
  - Trigger: pushes to `main` that modify docs-related files.
  - Action: builds MkDocs and deploys to GitHub Pages.

- `release-tag-publish.yml`
  - Trigger: tag pushes (`v*` or `*.*.*`) and manual dispatch.
  - Action order:
    1. Deploy docs for the tag.
    2. Validate tag version matches `pyproject.toml` version.
    3. Build package distributions.
    4. Run `twine check`.
    5. Publish to PyPI.

## Tag format

Recommended tag format:

```bash
git tag v1.0.1
git push origin v1.0.1
```

The workflow strips the leading `v` before comparing with `project.version`.

## Required setup

Configure PyPI Trusted Publishing for this repository:

- Repository: `jasonjimnz/sendou_ink_sdk`
- Workflow: `release-tag-publish.yml`

No PyPI API token is required when Trusted Publishing is configured.

## Manual local build (optional)

```bash
python -m pip install -e ".[build]"
python -m build
python -m twine check dist/*
```

