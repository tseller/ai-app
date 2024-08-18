from pydantic import BaseModel, Field

class Play(BaseModel):
    play: str = Field(
        description='Next play from the player.')
    board: dict = Field(
        description='Current board.')
