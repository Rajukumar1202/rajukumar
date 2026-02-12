🧠 Day 07 – Sorting & Linear Regression (DSA + AIML)

📌 SLOT 01: Sorting Algorithms (DSA).

1️⃣ What is Sorting?
Sorting means arranging elements in a specific order (ascending or descending).
Example:
Unsorted array:

[5, 2, 9, 1]
Sorted array (ascending):

[1, 2, 5, 9]

2️⃣ Why Sorting is Important?
Makes searching faster
Organizes data
Required for Binary Search
Useful in Data Analysis & Machine Learning.

3️⃣ Bubble Sort
Idea:
Repeatedly compare adjacent elements and swap them if they are in the wrong order.
Largest elements move to the end step by step.
Python Code:
Python
arr = [5, 2, 9, 1]

for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)

4️⃣ Selection Sort
Idea:
Find the smallest element and place it at the beginning.
Repeat for the remaining elements.
Python Code:
Python
arr = [5, 2, 9, 1]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
5️⃣ Time Complexity (Basic Idea)
Bubble Sort → O(n²)
Selection Sort → O(n²)
Meaning:
If number of elements increases, time increases very fast (quadratically).

📊 SLOT 02: Linear Regression (Machine Learning Basics).

1️⃣ What is Linear Regression?
Linear Regression is a machine learning algorithm used to predict a value based on input data using a straight line.

Example:
Hours Studied → Marks
2️⃣ Independent and Dependent Variables
Independent Variable (X) → Input
Dependent Variable (Y) → Output
Example: X = Hours Studied
Y = Marks

3️⃣ Line of Best Fit
Linear Regression finds the best straight line that fits the data.
Equation:

y = mx + c
Where:
m = slope
c = intercept

4️⃣ Training and Prediction
Training → Teaching the model using data
Prediction → Using the model to predict new values
Mini Example (Python)
Python
import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([40, 50, 60, 70, 80])

# Model
model = LinearRegression()
model.fit(hours, marks)

# Prediction
prediction = model.predict([[6]])
print("Predicted Marks:", prediction)

🔁 Quick Revision
🚀Sorting arranges data.
🚀Bubble Sort swaps adjacent elements.
🚀Selection Sort selects smallest element.
🚀Linear Regression predicts using straight line.
🚀Equation: y = mx + c..


✅Day 07 Sorting and Linear Regression Complete.😍
notes.md
sorting.py
linear_regression.py
