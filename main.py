# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Employee data
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# Order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# STEP 2
# Seeing data from employees table
df_first_five = pd.read_sql("""
    SELECT employeeNumber, lastName 
    FROM employees
""", conn)

# STEP 3
# Seeing last names and employee numbers from employees
df_five_reverse = pd.read_sql("""
    SELECT lastName, employeeNumber 
    FROM employees
""", conn)

# STEP 4
# Seeing last names and employee numbers as ID from employees
df_alias = pd.read_sql("""
    SELECT lastName, employeeNumber AS ID 
    FROM employees
""", conn)

# STEP 5
# Seeing all employees with a new column 'role' based on jobTitle
df_executive = pd.read_sql("""
    SELECT *,
    CASE
        WHEN jobTitle = 'President' OR jobTitle = 'VP Sales' OR jobTitle = 'VP Marketing'
        THEN 'Executive'
        ELSE 'Not Executive'
    END AS role
    FROM employees
""", conn)

# STEP 6
# Seeing name length of lastName
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)

# STEP 7
# Seeing short job title from employees
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)

# STEP 8
# Shows sum total price
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_amount
    FROM orderDetails
""", conn).iloc[0]

# STEP 9
# Shows day, month, and year from orderDate
df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           SUBSTR(orderDate, 9, 2) AS day,
           SUBSTR(orderDate, 6, 2) AS month,
           SUBSTR(orderDate, 1, 4) AS year
    FROM orders
""", conn)

conn.close()