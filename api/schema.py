# build a schema using pydantic
from pydantic import BaseModel
from typing import Optional

class Fbdata(BaseModel):
    page_name: str
    date: str
    text: Optional[str]
    reactions_nbr: int
    shares_nbr: int
    comments_nbr:int
    comments: str
    images_url: list(str)
    videos_url: list(str)

    class Config:
        orm_mode = True