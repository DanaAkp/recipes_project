from pydantic import BaseModel


class DataBaseModel(BaseModel):
    class Config:
        orm_mode = True


class SuccessData(DataBaseModel):
    success: bool
