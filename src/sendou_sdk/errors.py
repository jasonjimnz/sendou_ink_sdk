from __future__ import annotations

import json
from typing import Any


class SendouSdkError(RuntimeError):
    """Base exception for SDK-related errors."""


class SendouApiError(SendouSdkError):
    """Represents a non-successful API response."""

    _MAX_PAYLOAD_SUMMARY_LEN = 240

    def __init__(self, status_code: int, message: str, payload: Any | None = None) -> None:
        """Build a readable API exception with optional payload context."""

        message_text = self._clean_text(message) or f"HTTP {status_code}"
        detail = f"{message_text} (status {status_code})"
        payload_summary = self._payload_summary(payload)
        if payload_summary and not self._looks_duplicate(message_text, payload_summary):
            detail = f"{detail}: {payload_summary}"
        super().__init__(detail)
        self.status_code = status_code
        self.payload = payload

    @staticmethod
    def _clean_text(value: Any) -> str:
        """Normalize whitespace in arbitrary values for compact error text."""

        text = str(value).strip()
        return " ".join(text.split())

    @classmethod
    def _truncate(cls, value: str) -> str:
        """Truncate long payload snippets for concise error messages."""

        return (
            value[: cls._MAX_PAYLOAD_SUMMARY_LEN] + "..."
            if len(value) > cls._MAX_PAYLOAD_SUMMARY_LEN
            else value
        )

    @classmethod
    def _looks_duplicate(cls, message_text: str, payload_summary: str) -> bool:
        """Check whether payload text duplicates the base message."""

        msg = cls._clean_text(message_text).lower()
        summary = cls._clean_text(payload_summary).lower()
        return bool(msg and summary and (summary == msg or summary in msg or msg in summary))

    @staticmethod
    def _payload_summary(payload: Any | None) -> str | None:
        """Extract a short human-readable payload summary when possible."""

        if payload is None:
            return None

        if isinstance(payload, dict):
            errors = payload.get("errors")
            if isinstance(errors, list) and errors:
                first = errors[0]
                if isinstance(first, dict):
                    first_message = first.get("message") or first.get("error") or first.get("detail")
                    if first_message:
                        return SendouApiError._truncate(SendouApiError._clean_text(first_message))

            for key in ("message", "error", "detail"):
                value = payload.get(key)
                if value:
                    return SendouApiError._truncate(SendouApiError._clean_text(value))
            text = payload.get("raw")
            if text:
                return SendouApiError._truncate(SendouApiError._clean_text(text))
            try:
                rendered = json.dumps(payload, ensure_ascii=True)
            except (TypeError, ValueError):
                return "Unserializable JSON payload"
            return SendouApiError._truncate(rendered)

        if isinstance(payload, list):
            if payload and isinstance(payload[0], dict):
                first = payload[0]
                first_message = first.get("message") or first.get("error") or first.get("detail")
                if first_message:
                    return SendouApiError._truncate(SendouApiError._clean_text(first_message))
            try:
                rendered = json.dumps(payload, ensure_ascii=True)
            except (TypeError, ValueError):
                return "Unserializable list payload"
            return SendouApiError._truncate(rendered)

        return SendouApiError._truncate(SendouApiError._clean_text(payload))


class SendouAuthError(SendouApiError):
    """Raised when authentication fails or is missing."""


class SendouRateLimitError(SendouApiError):
    """Raised when the API rate limits a request."""
