from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi import Response

from sqlalchemy.exc import IntegrityError

from ..model.depend import create_session
from ..schemas import PostFilterModel, FilterModel
from ..controller import record_filter as ctrl
from ..utility.paging import PagingParam

router = APIRouter()
PREFIX = "filter"


@router.post("/", response_model=FilterModel, status_code=201)
async def add_filter_record(
    series: PostFilterModel, session=Depends(create_session)
):
    try:
        result = await ctrl.create_resource(series, session)
    except IntegrityError as exc:
        print(exc)
        raise HTTPException(
            status_code=409, detail="given product is a duplicate"
        )
    return result


@router.get("/", response_model=List[FilterModel], status_code=200)
async def list_all_filters(
    response: Response,
    paging_params=Depends(PagingParam),
    session=Depends(create_session),
):

    result, count = await ctrl.list_resource(paging_params, session)

    response.headers["X-total"] = str(count)
    response.headers["X-page"] = str(paging_params.page)
    return result
