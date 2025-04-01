from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from core.utils.env import EnvConfig

router = APIRouter()


@router.get("/test")
async def test():
    html_content = (
        f"<h1>{EnvConfig.get("SERVER_NAME")}</h1>" f"<p>Test service working</p>"
    )
    return HTMLResponse(html_content)
