# Routes package - export so "from routes import employees, attendance" works
from . import employees, attendance

__all__ = ["employees", "attendance"]
