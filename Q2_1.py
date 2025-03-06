import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' if using Qt
import matplotlib.pyplot as plt
import numpy as np

# Read the steps from the file
with open("steps.txt", "r") as file:
    steps = [int(line.strip()) for line in file]

# Task 2.1: Display steps taken on March 1st (Indexing starts from 0, March 1st is at index 59)
steps_march_1 = steps[59]
print(f"Steps taken on 03/01: {steps_march_1}")

# Task 2.2: Calculate and display the average steps per month
months_days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

average_steps_per_month = {}
index = 0
for month, days in months_days.items():
    month_steps = steps[index:index+days]
    average_steps_per_month[month] = sum(month_steps) / days
    index += days

# Display average steps per month
print("Average steps per month:")
for month, avg_steps in average_steps_per_month.items():
    print(f"{month}: {avg_steps:.2f}")

# Task 2.3: Plot the steps data
plt.figure(figsize=(10, 5))
plt.plot(range(1, 366), steps, label="Steps per day", color="blue")
plt.xlabel("Day of the Year")
plt.ylabel("Number of Steps")
plt.title("Daily Steps Taken in 2019")
plt.legend()
plt.grid()
plt.show()
