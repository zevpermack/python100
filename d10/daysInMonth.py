print("--- is it a leap year? ---")

# year = int(input("what year do you want to check? "))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
  if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
      return True
  else:
    return False

def days_in_month(year, month):
  if month < 1 or month > 12:
    return "Invalid Month"
  if is_leap_year(year) and month == 2:
    return 29
  return month_days[month - 1]

year = (int(input("Enter a year: ")))
month = (int(input("Enter a month: ")))
days = days_in_month(year, month)
print(days)

