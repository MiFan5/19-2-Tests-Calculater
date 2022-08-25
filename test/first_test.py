import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc=Calculator

# ТЕСТ НА УМНОЖЕНИЕ

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 5, 5)==25

    def test_multiply_calculation_failed(self):
         assert self.calc.multiply(self, 5, 5) == 5

# ТЕСТ НА ДЕЛЕНИЕ

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 2)==3

    def test_division_calculation_failed(self):
         assert self.calc.division(self, 6, 2) == 6

# ТЕСТ НА ВЫЧЕТАНИЕ

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 4, 2)==2

    def test_subtraction_calculation_failed(self):
         assert self.calc.subtraction(self, 4, 2) == 4

# ТЕСТ НА СЛОЖЕНИЕ

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 2, 2)==4

    def test_adding_calculation_failed(self):
         assert self.calc.adding(self, 2, 2) == 2
