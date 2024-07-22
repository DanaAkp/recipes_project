from typing import Optional
from pydantic import validate_arguments
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

    @validate_arguments
    def validate_unit_measure(cls, value):
        if value in UnitMeasure.get_all_units():
            return UnitMeasure(value)
        raise ValueError(f'Значение единиц измерения должно соответствовать списку: '
                         f'{", ".join(UnitMeasure.get_all_units())}')


class ProductData(DataBaseModel):
    id: int
    name: str
    calories: Optional[float]
    fats: Optional[float]
    carbohydrates: Optional[float]
    proteins: Optional[float]
    unit_measure: UnitMeasure
    units_measure_nutrition_facts: int
