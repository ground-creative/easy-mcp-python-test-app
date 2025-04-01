# app/middlewares/MyMiddleware.py

from core.utils.logger import logger  # Use to add logging capabilities
from mcp.server.fastmcp import (
    Context,
)  # Use `ctx: Context` as function param to get mcp context
from core.utils.state import global_state  # Use to add and read global vars
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


class MyMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, *args, **kwargs):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        """Your code here"""

        response = await call_next(request)
        return response
