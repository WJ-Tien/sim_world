import random
from .. data_models.directions import Directions
from pydantic import BaseModel, Field


class Car(BaseModel):
    name: str = Field(...)
    color: tuple[int, int, int] = Field(..., description="RGB color")
    grid_pos: list[int] = Field(default_factory=lambda: [0, 0])

    def move(self, grid_cols: int, grid_rows: int, blocks: set[tuple[int, int]]) -> None:
        direction = random.choice(list(Directions))
        new_pos = self.grid_pos.copy()

        if direction is Directions.UP and self.grid_pos[1] > 0:
            new_pos[1] -= 1
        elif direction is Directions.DOWN and self.grid_pos[1] < grid_rows - 1:
            new_pos[1] += 1
        elif direction is Directions.LEFT and self.grid_pos[0] > 0:
            new_pos[0] -= 1
        elif direction is Directions.RIGHT and self.grid_pos[0] < grid_cols - 1:
            new_pos[0] += 1

        # Check if new position is blocked
        if tuple(new_pos) not in blocks:
            self.grid_pos = new_pos
