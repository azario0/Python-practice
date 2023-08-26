"""
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, 
respectively, in MMDDYYYY format.

Constraints
 2000 < year < 3000
"""
import calendar

def main():
    date = input('Enter the date as the following format MM DD YYYY  Separated by only one space : ').split(' ')
    month = int(date[0])
    day = int(date[1])
    year = int(date[2])
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())
    
if __name__ == '__main__':
    main()