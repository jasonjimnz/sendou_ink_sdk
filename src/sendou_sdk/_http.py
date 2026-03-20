from __future__ import annotations

"""Internal HTTP transport wrapper used by SDK resources."""

from typing import Any

import httpx

from .config import SendouConfig
from .errors import SendouApiError, SendouAuthError, SendouRateLimitError


class SendouHttpClient:
    """Thin async HTTP client that normalizes URLs and maps API errors."""

    def __init__(self, config: SendouConfig) -> None:
        """Create an HTTP client from resolved SDK configuration."""

        self._config = config
        base_url = self._normalize_base_url(config.base_url)
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=config.timeout_seconds,
            headers=self._build_headers(config.token),
        )

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json_body: dict[str, Any] | None = None,
    ) -> Any:
        """Execute an HTTP request and return decoded JSON payload.

        Raises:
            SendouAuthError: For 401/403 responses.
            SendouRateLimitError: For 429 responses.
            SendouApiError: For all other non-2xx responses.
        """

        response = await self._client.request(method, path, params=params, json=json_body)
        payload = self._safe_json(response)
        if response.status_code in (401, 403):
            raise SendouAuthError(response.status_code, "Authentication failed", payload)
        if response.status_code == 429:
            raise SendouRateLimitError(response.status_code, "Rate limited", payload)
        if response.status_code >= 400:
            message = self._format_error_message(response, payload)
            raise SendouApiError(response.status_code, message, payload)
        return payload

    async def close(self) -> None:
        """Close the underlying :class:`httpx.AsyncClient`."""

        await self._client.aclose()

    def _build_headers(self, token: str | None) -> dict[str, str]:
        """Build default request headers including optional bearer auth."""

        headers = {"Accept": "application/json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return headers

    def _normalize_base_url(self, base_url: str) -> str:
        """Ensure the configured base URL points at the `/api` root."""

        if base_url.endswith("/api"):
            return base_url
        return f"{base_url.rstrip('/')}/api"

    def _safe_json(self, response: httpx.Response) -> Any:
        """Decode JSON response payload and preserve raw text when invalid."""

        if not response.content:
            return None
        try:
            return response.json()
        except ValueError:
            return {"raw": response.text}

    def _format_error_message(self, response: httpx.Response, payload: Any | None) -> str:
        """Extract a short base error message from response payload."""

        if isinstance(payload, dict):
            message = payload.get("message") or payload.get("error")
            if message:
                return str(message)
        if isinstance(payload, list):
            return "Unexpected list payload"
        if isinstance(payload, str):
            return payload
        if isinstance(payload, dict) and payload.get("raw"):
            return str(payload["raw"])
        return f"HTTP {response.status_code}"
