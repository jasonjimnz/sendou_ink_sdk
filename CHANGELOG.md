# Changelog

All notable changes to this project are documented in this file.

## [1.0.1] - 2026-03-20

### Changed

- Fixed tournament bracket response model parsing when API returns `meta: {}` by making optional `meta` fields default to `None` in `TournamentBracketMeta`.
- Improved local tournament playground behavior to iterate bracket indices from the tournament response instead of assuming a single fixed index.

## [1.0.0] - 2026-03-20

### Added

- Initial public release of `sendou-ink-sdk`.
- Async typed resource wrappers for users, teams, calendar, sendouq, tournaments, and organizations.
- Error types for API, auth, and rate-limit handling.
- MkDocs-based documentation with usage, reference, configuration, and playground guides.

