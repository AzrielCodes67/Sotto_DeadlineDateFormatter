import datetime
event_title = input("Enter the event title: ")
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))

deadline = datetime.date(year, month, day)

print("\n--- EVENT DEADLINE ---")
print("Event Title:", event_title.upper())
print("Readable Date:", deadline.strftime("%B %d, %Y"))
print("Year:", deadline.year)
print("Month:", deadline.month)
print("Day:", deadline.day)
print("Weekday:", deadline.strftime("%A"))]

