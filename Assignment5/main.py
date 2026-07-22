from Utilities.calculator import add, subtract, multiply, divide
from Utilities.string_operations import re_st,cap_st, lw_st, up_st

print("Using calculator.py:")
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

sample_string = "hello World"

print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", re_st(sample_string))
print("Capitalized:", cap_st(sample_string))
print("Lowercase:", lw_st(sample_string))
print("Uppercase:", up_st(sample_string))