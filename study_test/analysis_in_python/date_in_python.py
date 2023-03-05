from datetime import date, timedelta

start = date(2023, 3, 4)
end = date(2023, 12, 4)

print(start.day)
print(start.month)
print(start.year)
print(start.weekday())

# Subtract the two dates and print the number of days
print((end - start).days)

# Convert to ISO and US formats
start.isoformat()  # ISO
start.strftime("%m/%d/%Y")  # US
