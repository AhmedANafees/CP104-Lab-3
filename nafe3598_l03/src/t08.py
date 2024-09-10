"""
------------------------------------------------------------------------
Lab 3, Task 8
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-10-04"
------------------------------------------------------------------------
"""
dirt_amount = float(input("Enter amount of dirt (m^3):"))
gravel_amount = float(input("Enter amount of gravel (m^3):"))
sand_amount = float(input("Enter amount of sand (m^3):"))
total = int(dirt_amount + gravel_amount + sand_amount)
print("Material   Cubic Metres")
print(f'Dirt      {dirt_amount:8.1f}')
print(f'Gravel    {gravel_amount:8.1f}')
print(f'Sand      {sand_amount:7.1f}')
print(f'Total     {total:8.1f}')
