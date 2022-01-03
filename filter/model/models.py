from uuid import UUID, uuid4
from datetime import datetime
from sqlalchemy.sql.sqltypes import DateTime, String, ARRAY
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID as sqlUUID

from sqlalchemy.orm import declarative_base

BaseModel = declarative_base()


class Filter(BaseModel):
    __tablename__ = "filter"
    id_: UUID = Column(
        "id", sqlUUID(as_uuid=True), default=uuid4, primary_key=True
    )
    search: str = Column(ARRAY(String), nullable=False)
    sort: str = Column(String, nullable=False)
    price: str = Column(String, nullable=True)
    date: datetime = Column(
        DateTime(timezone=True), nullable=False,
    )
