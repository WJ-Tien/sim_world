from pydantic import BaseModel

class WorldConfig(BaseModel):
    grid_cols: int = 10
    grid_rows: int = 10
    cell_size: int = 50
    frame_update_interval: int = 500 # frame update interval (ms)