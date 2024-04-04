from datetime import datetime
from typing import List

from pydantic import BaseModel

class NewsSummaryDomainModel(BaseModel):
    authors: List[str]
    title: str
    published_date: datetime
    summary: str
    top_image: str

    class Config:
        orm_mode = True

class GetNewsRequest(BaseModel):
    url: str