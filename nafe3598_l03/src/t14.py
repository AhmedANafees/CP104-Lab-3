"""
------------------------------------------------------------------------
Lab 3, Task 14
------------------------------------------------------------------------
Author: Ahmed Nafees
ID:     169053598
Email:  nafe3598@mylaurier.ca
__updated__ = "2023-09-27"
------------------------------------------------------------------------
"""
num_minutes = int(input("Enter number of minutes:"))
num_days = num_minutes//1440
remain_hours = num_minutes // 60 - num_days*24
remain_minutes = num_minutes % 60
print(f'there are {num_days} days, {remain_hours} hours, and {remain_minutes} minutes in {num_minutes} minutes')
