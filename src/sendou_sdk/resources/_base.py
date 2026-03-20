from __future__ import annotations

"""Shared helper class for strongly-typed resource wrappers."""

from typing import Any

from .._http import SendouHttpClient


class BaseResource:
    """Base class exposing convenience HTTP helpers for resources."""

    def __init__(self, http: SendouHttpClient) -> None:
        """Bind the resource to a shared HTTP client instance."""

        self._http = http

    async def _get(self, path: str, *, params: dict[str, Any] | None = None) -> Any:
        """Perform an internal GET request for a resource endpoint."""

        return await self._http.request("GET", path, params=params)

    async def _post(self, path: str, *, payload: dict[str, Any] | None = None) -> Any:
        """Perform an internal POST request for a resource endpoint."""

        return await self._http.request("POST", path, json_body=payload)
