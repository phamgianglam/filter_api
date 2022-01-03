from typing import List
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class PostFilterModel(BaseModel):
    search: List[str] = Field([], description="search field")
    sort: Optional[str] = Field(None, description="description of product")
    price: Optional[str] = Field(None, description="price range")
    date: Optional[datetime] = Field(
        datetime.now(), description="date that filter is requested"
    )

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {
            "example": {
                "search": ["name:vpn", "name:remote"],
                "sort": "price:asc",
                "price": "20-50",
                "date": "2022-01-01T13:40:40.603227",
            }
        }


class FilterModel(BaseModel):
    id_: UUID = Field(..., alias="id")
    search: List[str] = Field(..., description="search field")
    sort: str = Field(..., description="sort term")
    price: str = Field(..., description="price range")
    date: Optional[datetime] = Field(
        ..., description="date that filter is requested"
    )

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        extra = "forbid"
        schema_extra = {
            "example": {
                "id": uuid4(),
                "search": ["name:vpn", "name:remote"],
                "sort": "price:asc",
                "price": "20-50",
                "date": "2022-01-01T13:40:40.603227",
            }
        }
