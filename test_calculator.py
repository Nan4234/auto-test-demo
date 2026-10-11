"""pytest 自动化测试用例：覆盖计算器模块的核心逻辑。"""

import pytest

from calculator import Calculator, CalculatorError


@pytest.fixture
def calc() -> Calculator:
    """每个测试用例共享的 Calculator 实例（fixture）。"""
    return Calculator()


# ---------- 基本断言 ----------

def test_add_basic(calc):
    assert calc.add(2, 3) == 5


def test_subtract_negative_result(calc):
    assert calc.subtract(3, 10) == -7


def test_multiply_by_zero(calc):
    assert calc.multiply(5, 0) == 0


# ---------- 参数化测试 ----------

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (2.5, 2.5, 5.0),
        (100, 200, 300),
    ],
)
def test_add_parametrized(calc, a, b, expected):
    assert calc.add(a, b) == expected


# ---------- 异常测试 ----------

def test_divide_by_zero_raises(calc):
    with pytest.raises(CalculatorError, match="除数不能为 0"):
        calc.divide(1, 0)


# ---------- 使用 approx 处理浮点精度 ----------

def test_divide_float_precision(calc):
    assert calc.divide(1, 3) == pytest.approx(0.333333, rel=1e-3)


# ---------- 标记分组 ----------

@pytest.mark.slow
def test_power_large_exponent(calc):
    assert calc.power(2, 10) == 1024


def test_power_zero_exponent(calc):
    assert calc.power(7, 0) == 1
