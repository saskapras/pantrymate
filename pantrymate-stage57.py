# === Stage 57: Add structured result objects for command handlers ===
# Project: PantryMate
from dataclasses import dataclass


@dataclass(frozen=True)
class ShelfResult:
    """Structured outcome returned by every pantry command handler."""
    action: str = "none"
    details: dict = None
    message: str = "No changes applied."
    error: str = ""

    def __post_init__(self):
        if self.details is None:
            object.__setattr__(self, 'details', {})


@dataclass(frozen=True)
class PantryResponse:
    """Top-level response envelope sent to the client after a command."""
    status: str = "ok"
    result: ShelfResult = None
    meta: dict = None

    def __post_init__(self):
        if self.result is None:
            object.__setattr__(self, 'result', ShelfResult())


def default_response() -> PantryResponse:
    return PantryResponse(status="ok", result=ShelfResult(), meta={"version": "57"})
