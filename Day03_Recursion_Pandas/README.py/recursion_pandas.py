🧠 Day 03 – Recursion (DSA) & Pandas Basics (AIML)

📌 SLOT 01: Recursion (DSA)

1️⃣ What is Recursion?
✅ Answer:
Recursion is a technique where a function calls itself to solve a problem.

👉 Simple words:
Ek function jo khud ko call karta hai, jab tak kaam complete na ho jaaye.

2️⃣ Base Case & Recursive Case:
✅ Answer:
Recursion me do cheez zaroori hoti hain:
📌Base Case: jahan function ruk jaata hai.
📌Recursive Case: jahan function khud ko dobara call karta hai.
❌ Base case nahi hoga to program infinite loop me chala jaayega.

3️⃣ Factorial using Recursion
📌 Factorial:

5! = 5 × 4 × 3 × 2 × 1
🧑‍💻 Code:
Python
def factorial(n):
    if n == 1:          # base case
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
📌 Output:
120

4️⃣ Print Numbers from N to 1 (Recursion):
🧑‍💻 Code:
Python
def print_num(n):
    if n == 0:          # base case
        return
    print(n)
    print_num(n-1)

print_num(5)
📌 Output:
5
4
3
2
1

5️⃣ Fibonacci using Recursion (Basic):
🧑‍💻 Code:
Python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
📌 Output:
5

📌 Note:
Fibonacci recursion slow hota hai, par concept samajhne ke liye important hai.

📌 SLOT 02: Pandas Basics (AIML):

1️⃣ What is Pandas?
✅ Answer:
Pandas is a Python library used to work with data in tables (rows & columns).
Use cases:
📌CSV files.
📌Data analysis.
📌Machine Learning se pehle data handle karna.

2️⃣ Creating a DataFrame
🧑‍💻 Code:
Python
import pandas as pd
data = {
    "Name": ["Raju", "Amit", "Sita"],
    "Marks": [80, 75, 90]
}

df = pd.DataFrame(data)
print(df)
📌 Output:

Name  Marks
0  Raju     80
1  Amit     75
2  Sita     90

3️⃣ Reading CSV File:
🧑‍💻 Code:
Python
import pandas as pd

df = pd.read_csv("data.csv")
print(df)

4️⃣ Selecting Rows & Columns
🧑‍💻 Code:
Python
print(df["Marks"])   # column
print(df.head())     # first 5 rows

5️⃣ Basic Operations:
🧑‍💻 Mean of Marks:
Python
print(df["Marks"].mean())
🧑‍💻 Filter (Marks > 80):

Python
print(df[df["Marks"] > 80])


🔁 Quick Revision
📌Recursion = function calling itself
📌Base case = stopping condition
📌Pandas = data handle karne ka tool
📌DataFrame = table (rows × columns)
.mean() = average


✅Day 03 – Recursion & Pandas Completed
✅Day 03 Notes Complete
 
