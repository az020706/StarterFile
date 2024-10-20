# Import datetime module
from datetime import datetime, timedelta

# Get today's date from the user
today_date = input("Enter today's date (dd/mm/yyyy): ")

# Convert the input string to a date object
today_date_obj = datetime.strptime(today_date, '%d/%m/%Y')

# Calculate the date for tomorrow
tomorrow_date_obj = today_date_obj + timedelta(days=1)

# Format the date for tomorrow in dd/mm/yy format
tomorrow_date = tomorrow_date_obj.strftime('%d/%m/%y')

# Output the date for tomorrow
print("Date for tomorrow:", tomorrow_date)
