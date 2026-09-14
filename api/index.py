"""Vercel entry point: exposes the Flask app in turnaround/app.py as a WSGI handler."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "turnaround"))
from app import app  # noqa: E402,F401
