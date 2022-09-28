from pydantic import BaseModel
from typing import Optional

class Payload_request(BaseModel):
    user: str
    text_field: str = ''
    order_by: str = 'name'
    filter_list: list = []
    days_in_cache: int = 3


class Payload_response(BaseModel):
    cache_id: int = -1
    status_code: int = 500
    data: list = []
    from_cache: bool = False
    msg: str = ''
