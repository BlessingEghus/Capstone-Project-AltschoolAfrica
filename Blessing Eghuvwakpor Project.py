#!/usr/bin/env python
# coding: utf-8

# First Semester Project: Automating Accounting Procedures for a 
# Business(Individual Project)
# Project Overview:
# A local retail business, dealing with a variety of products, aims to streamline and automate its 
# accounting procedures. The business operates two shifts per day with one worker on each shift.
# The primary goal is to create a Python project that assists in automating essential accounting 
# tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.
# Key Features:
# 1. Calculate Total Sales for the Day: from sales data for morning and evening shifts,
# produce total sales for the day.
# 2. Calculate Worker's Salary: given hourly rate and hours worked by a worker. 
# retrieve the worker's salary.
# 3. Calculate Profit: given a list of numbers representing total sales and total cost of 
# items sold, find the profit.(or loss if negative)
# 4. Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped 
# for the shift (2% of shift sales).
# 5. Calculate Total Tips for the Day: with sales data for morning and evening shifts, 
# return total tips for the day (sum of tips from both shifts).
# Think of your shift sales as a list.

# In[1]:


# Define a function to calculate the total sales for a shift
def total_sales(shift_data):
  # Initialize a variable to store the sum of sales
  total = 0
  # Loop through the sales data for the shift
  for sale in shift_data:
    # Add the sale amount to the total
    total += sale
  # Return the total sales for the shift
  return total
try:
    # Define some sample sales data for morning shift
    morning_shift = []
    #Define total number of sales 
    morning = int(input("Please enter total number of sales for morning shift: "))
    #Iterate till range
    for i in range(0, morning):
        sales = float(input("please enter sales for your shift: "))
        # Adding sales to morning_shift
        morning_shift.append(sales)

        
    # Define some sample data for Evening shift
    evening_shift = []
    # Define total number of sales 
    evening = int(input("Please enter total number of sales for evening shift:"))
    for i in range(0, evening):
        sales = float(input("please enter sales for your shift: "))
        # Adding sales to evening_shift
        evening_shift.append(sales)


    # Calculate the total sales for the day by adding the total sales for each shift
    total_sales_day = total_sales(morning_shift) + total_sales(evening_shift)

    # Print the result
    print(f"The total sales for the day are ${total_sales_day}.")
except ValueError:
    print("PLEASE ENTER A NUMERICAL VALUE!!!")


# In[10]:


# Define a function to calculate the worker's salary
def worker_salary(hourly_rate, hours_worked):
  # Multiply the hourly rate by the hours worked
  salary = hourly_rate * hours_worked
  # Return the salary
  return salary

# Define some sample values for hourly rate and hours worked
hourly_rate = 15 # dollars per hour
hours_worked = 8 # hours per day

# Calculate the worker's salary by calling the function
salary = worker_salary(hourly_rate, hours_worked)

# Print the result
print(f"The worker's salary is ${salary}.")


# In[3]:


# Define a function to calculate profit or loss from a list of sales and costs
def calculate_profit_or_loss(sales, costs):
  # Initialize profit or loss as zero
  profit_or_loss = 0
  # Loop through the lists of sales and costs
  for sale, cost in zip(sales, costs):
    # Add the difference between sale and cost to profit or loss
    profit_or_loss += sale - cost
  # Return the final profit or loss
  return profit_or_loss

# Example list of sales and costs
sales = [1000, 1200, 800, 1500, 900]
costs = [1200, 1300, 900, 1600, 1000]

# Call the function and print the result
result = calculate_profit_or_loss(sales, costs)
print("The profit or loss is:", result)


# In[9]:


# Define a function to calculate tips for a shift
def calculate_tips(sales, tip_rate):
  # Initialize the total tips as zero
  total_tips = 0
  # Loop through the list of sales
  for sale in sales:
    # Add the tip amount for each sale to the total tips
    total_tips += sale * tip_rate / 100
  # Return the total tips
  return total_tips

# Example list of sales for a shift in $
sales = [200, 190, 250, 180, 90]

# Tip rate as a percentage
tip_rate = 2

# Call the function and print the result
result = round(calculate_tips(sales, tip_rate, ), 2)
print(f"The total tips for the shift are: ${result}")


# In[11]:


# Define a function to calculate the total tips for the day
def calculate_total_tips(morning_sales, evening_sales, tip_rate):
  # Initialize the total tips as zero
  total_tips = 0
  # Loop through the lists of morning and evening sales
  for sale in morning_sales + evening_sales:
    # Add the tip amount for each sale to the total tips
    total_tips += sale * tip_rate / 100
  # Return the total tips
  return total_tips

# Example lists of sales for morning and evening shifts
morning_sales = [100, 150, 200, 120, 80]
evening_sales = [250, 300, 180, 90, 150]

# Tip rate as a percentage
tip_rate = 2

# Call the function and print the result
result = round(calculate_total_tips(morning_sales, evening_sales, tip_rate), 2)
print(f"The total tips for the day are: {result}")


# In[ ]:




