from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from ..schemas import PostFilterModel
from ..model.models import Filter
from ..utility.paging import PagingParam, count_query, paging_query


async def create_resource(product: PostFilterModel, session: AsyncSession):

    new_series = Filter(**product.dict(exclude_unset=True))
    print(product.dict())
    session.add(new_series)
    await session.commit()
    return new_series


async def list_resource(paging_param: PagingParam, session: AsyncSession):
    stmt = select(Filter)

    count_stmt = await count_query(stmt)
    paging_stmt = await paging_query(
        stmt, paging_param.page, paging_param.size
    )

    result = (await session.execute(paging_stmt)).scalars().all()
    count = (await session.execute(count_stmt)).scalars().one()
    return result, count
