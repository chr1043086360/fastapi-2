from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from ..db.database import create_connection, disconnect
from app.api.routers.questions import router as questions_router
from app.api.routers.users import router as users_router

# app = FastAPI(__name__)


def generate_application() -> FastAPI:
    application = FastAPI(__name__)
    application.debug = True

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_connection)
    application.add_event_handler("shutdown", disconnect)

    application.include_router(
        questions_router, prefix="/quesitons"
    )
    application.include_router(
        users_router, prefix="/users"
    )

    return application


app = generate_application()
