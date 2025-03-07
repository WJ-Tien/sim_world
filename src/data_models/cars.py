import random
from src.data_models.directions import Directions
from pydantic import BaseModel, Field


class Car(BaseModel):
    name: str = Field(...)
    color: tuple[int, int, int] = Field(..., description="RGB color")
    grid_pos: list[int] = Field(default_factory=lambda: [0, 0])

    def move(self, grid_cols: int, grid_rows: int) -> None:
        direction = random.choice(list(Directions))
        if direction is Directions.UP and self.grid_pos[1] > 0:
            self.grid_pos[1] -= 1
        elif direction is Directions.DOWN and self.grid_pos[1] < grid_rows - 1:
            self.grid_pos[1] += 1
        elif direction is Directions.LEFT and self.grid_pos[0] > 0:
            self.grid_pos[0] -= 1
        elif direction is Directions.RIGHT and self.grid_pos[0] < grid_cols - 1:
            self.grid_pos[0] += 1
