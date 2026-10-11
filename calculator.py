"""被测代码：一个简单的计算器模块，用于演示 pytest 自动化测试。"""


class CalculatorError(Exception):
    """计算器自定义异常。"""


class Calculator:
    """支持基本运算的计算器。"""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise CalculatorError("除数不能为 0")
        return a / b

    def power(self, base: float, exp: float) -> float:
        return base ** exp
