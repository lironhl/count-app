import enum

import humps
from pydantic import BaseModel


class YashishModel(BaseModel):
    class Config:
        orm_mode = True
        alias_generator = humps.camelize
        allow_population_by_field_name = True


class Role(str, enum.Enum):
    Superuser = "Superuser"
    Leader = "Leader"
    Volunteer = "Volunteer"


class InteractionType(str, enum.Enum):
    InPerson = "InPerson"
    Phone = "Phone"
