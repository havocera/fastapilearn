from pydantic import BaseModel
from typing import Optional, Union


class CreatTask(BaseModel):
    name: str
    model: str
    email: str
    file: list


class SearchTask(BaseModel):
    name: Union[str, None] = None
    email: Union[str, None] = None
    order_no: Union[str, None] = None


class DownloadTask(BaseModel):
    order_no: Union[str, None] = None
class DownloadFile(BaseModel):
    filename: Union[str, None] = None

