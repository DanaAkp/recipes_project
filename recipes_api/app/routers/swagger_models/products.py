from typing import Optional

from app.constants import UnitMeasure
from app.routers.swagger_models import DataBaseModel


class ProductDataIn(DataBaseModel):
    name: str
    calories: Optional[float]
    fats: Optional[float]
    carbohydrates: Optional[float]
    proteins: Optional[float]
    unit_measure: UnitMeasure
    units_measure_nutrition_facts: int


class ProductData(DataBaseModel):
    id: int
    name: str
    calories: Optional[float]
    fats: Optional[float]
    carbohydrates: Optional[float]
    proteins: Optional[float]
    unit_measure: UnitMeasure
    units_measure_nutrition_facts: int

