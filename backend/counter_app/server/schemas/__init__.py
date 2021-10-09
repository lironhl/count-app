import humps
from pydantic import BaseModel


class CounterAppModel(BaseModel):
    class Config:
        orm_mode = True
        alias_generator = humps.camelize
        allow_population_by_field_name = True
