# app/config/app.py

PRESTART_HOOKS = {
    "fastapi": ["app.utils.test_hook.prestart_hook"],
}

MIDDLEWARE = {"mcp": [{"middleware": "app.middleware.MyMiddleware", "priority": 1}]}

SERVICES = [
    "core.services.server_info",
    "app.services.test_services",
]
