# mcp_server/tools/add.py
from core.utils.logger import logger  # Use to add logging capabilities
from mcp.server.fastmcp import (
    Context,
)  # Use `ctx: Context` as function param to get mcp context
from core.utils.state import global_state  # Use to add and read global vars


def add_numbers_tool(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
