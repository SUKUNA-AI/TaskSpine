from fastapi import FastAPI
from contextlib import asynccontextmanager


from apps.api.routes.system import router as system_router
from libs.common.config import settings 


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Здесь позже можно:
    # - инициализировать shared resources
    # - прогреть клиенты
    # - логировать старт приложения
    yield
    # Здесь позже можно:
    # - закрывать соединения
    # - освобождать ресурсы

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=settings.app_description,
        lifespan=lifespan,
    )

    app.include_router(system_router)

    return app


app = create_app()
