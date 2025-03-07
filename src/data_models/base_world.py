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
    block_ratio: float = 0.07

    @classmethod
    def get_cell_size(cls):
        return cls.model_fields["cell_size"].default

    @classmethod
    def get_grid_rows(cls):
        return cls.model_fields["grid_rows"].default

    @classmethod
    def get_grid_cols(cls):
        return cls.model_fields["grid_cols"].default
    