from pydantic import BaseModel, Field


class Car(BaseModel):
    name: str = Field(...)
    color: str = Field(..., description="color in RGB format")