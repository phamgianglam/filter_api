from fastapi import FastAPI
from . import record_filter


def config_route(app: FastAPI, dependencies=None, prefix=None):
    app.include_router(
        record_filter.router,
        prefix=f"/{prefix}/{record_filter.PREFIX}",
        tags=[record_filter.PREFIX],
    )
