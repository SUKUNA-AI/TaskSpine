from fastapi import APIRouter

from libs.common.config import settings

router = APIRouter(prefix="/system", tags=["System"])

@router.get("/info")
async def get_system_info():
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "app_description": settings.app_description,
        "app_env": settings.app_env,
    }


@router.get("/health")
async def health_check():
    return {"status": "ok",
            "service": settings.app_name,
            }


@router.get("/version")
async def get_version():
    return {"version": settings.app_version}


@router.get("/readyz")
async def ready():
    return{
        "status": "ready",
        "service": settings.app_name,
        "enviroment": settings.app_env,
    }