from __future__ import annotations

"""SDK configuration defaults and immutable runtime config."""

from dataclasses import dataclass

DEFAULT_BASE_URL = "https://sendou.ink/api"
DEFAULT_TIMEOUT_SECONDS = 20.0


class SendouDefaults:
    """Default settings used by :class:`SendouClient`."""

    base_url = DEFAULT_BASE_URL
    timeout_seconds = DEFAULT_TIMEOUT_SECONDS


@dataclass(frozen=True)
class SendouConfig:
    """Resolved client configuration used by the HTTP layer.

    Attributes:
        base_url: API base URL.
        timeout_seconds: Per-request timeout in seconds.
        token: Optional bearer token for authenticated endpoints.
    """

    base_url: str = DEFAULT_BASE_URL
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS
    token: str | None = None
