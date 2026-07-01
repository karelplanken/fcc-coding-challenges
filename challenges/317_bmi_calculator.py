# Daily Coding challenge #317 (2026-06-23) - freeCodeCamp.org
# BMI Calculator
# Given a weight in pounds and a height in inches, return the BMI (Body Mass Index)
# rounded to one decimal place.
#
# To get BMI: divide the weight by the height squared, then multiply the result by 703.
from pytest import mark


class BMICalculator:
    KG_PER_LBS = 0.453592
    METER_PER_INCH = 0.0254
    BMI_IMPERIAL_TO_METRIC = round(KG_PER_LBS / (METER_PER_INCH**2))

    def __init__(
        self, factor: int = BMI_IMPERIAL_TO_METRIC, precision: int = 1
    ) -> None:
        self.factor = factor
        self.precision = precision

    def __call__(self, weight: int, height: int) -> float:
        return round(weight / height**2 * self.factor, self.precision)


calculate_bmi = BMICalculator()  # drop-in replacement; same call signature

tests = [
    (180, 70, 25.8),
    (140, 64, 24.0),
    (160, 76, 19.5),
    (200, 60, 39.1),
    (150, 68, 22.8),
]


@mark.parametrize('weight, height, expected', tests)
def test_calculate_bmi(weight: int, height: int, expected: float) -> None:
    assert calculate_bmi(weight, height) == expected


if __name__ == '__main__':
    weight, height, expected = tests[0]
    print(calculate_bmi(weight, height))
