# Copilot Instructions for sendou-sdk-python

## Scope

These instructions apply to files under `sendou-sdk-python/`.

## Project goals

- Keep the SDK async-first and strongly typed.
- Preserve simple, stable public APIs in `sendou_sdk` exports.
- Prefer predictable behavior over implicit magic.

## Coding conventions

- Target Python 3.10+ syntax.
- Use type hints on all public functions and methods.
- Keep modules ASCII-only unless existing file content requires otherwise.
- Use concise docstrings on public classes and methods.
- Prefer `pydantic` models for typed request/response payloads.

## Resource layer rules

- Add new endpoint wrappers in `src/sendou_sdk/resources/`.
- Reuse `BaseResource._get` and `BaseResource._post` for transport calls.
- Return typed models (or typed aliases) from resource methods.
- Keep path construction explicit and local to each method.

## Error handling rules

- Map API auth failures to `SendouAuthError`.
- Map rate limits to `SendouRateLimitError`.
- Raise `SendouApiError` for other non-success responses.
- Include readable payload context in exception messages.

## Documentation rules

When behavior changes, update docs in the same change set:

- `README.md` for quick start and build commands.
- `docs/usage.md` for typed examples.
- `docs/reference.md` for signatures and model mapping.
- `docs/configuration.md` for runtime options.
- `docs/playground.md` for token-based walkthroughs.

## Packaging and release rules

- Keep `pyproject.toml` metadata and dependencies in sync with docs.
- Build artifacts with `python -m build --wheel`.
- Validate artifacts with `python -m twine check dist/*`.
- Do not commit generated files under `dist/` or `build/`.

## Safety checks before finishing

- Run file diagnostics for modified Python files.
- Avoid introducing unrelated refactors.
- Do not remove or rename exported symbols without explicit request.

