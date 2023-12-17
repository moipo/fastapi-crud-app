from typing import Union

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: Union[str, None] = None
    is_checked = False
