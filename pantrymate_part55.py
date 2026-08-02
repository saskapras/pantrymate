# === Stage 55: Add a setting to disable colorized output ===
# Project: PantryMate
def disable_color():
    """Disable colorized output and return a no-op formatter."""
    import sys, os
    if sys.stdout.isatty() and os.environ.get("TERM", "") in ("dumb", "xterm"):
        os.environ["NO_COLOR"] = "1"
