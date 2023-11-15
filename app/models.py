from pydantic import BaseModel, Field
import re


class FormData(BaseModel):
    f_name1: str = Field(..., description="Description for field 1")
    f_name2: str = Field(..., description="Description for field 2")

    class Config:
        orm_mode = True



def get_field_type(value):
    if re.match(r'\d{4}-\d{2}-\d{2}$', value):
        return 'date'
    elif re.match(r'\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}$', value) or re.match(r'\+7\d{10}$', value):
        return 'phone'
    elif '@' in value and '.' in value:
        return 'email'
    else:
        return 'text'

