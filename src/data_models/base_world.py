from pydantic import BaseModel

class WorldConfig(BaseModel):
    grid_cols: int = 25
    grid_rows: int = 25
    cell_size: int = 30
    frame_update_interval: int = 500 # frame update interval (ms)
    fps: int = 60
    map_background_color: tuple = (255, 255, 255)
    grid_line_color: tuple = (200, 200, 200)
    block_color: tuple = (100, 100, 100)