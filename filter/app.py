from fastapi import FastAPI
from filter.config import config
from filter.apis import config_route

app = FastAPI(docs_url=f"/{config.API_PREFIX}/", title="Filter Record API")

config_route(app, prefix=config.API_PREFIX)


@app.get("/healthcheck", status_code=200, include_in_schema=False)
async def healthcheck():
    return "ok"
