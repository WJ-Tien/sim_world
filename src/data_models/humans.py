from enum import Enum
from pydantic import BaseModel, Field


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class Human(BaseModel):
    name: str = Field(..., description="English name")
    gender: Gender = Field(...)
    age: int = Field(...)
    nation: str = Field(...)
    height: float = Field(..., description="unit (cm)")
    weight: float = Field(..., description="unit (kg)")
    role: str = Field(..., description="occupation")

