🧠 Day 08 – Searching & Logistic Regression (DSA + AIML)

📌 SLOT 01: Searching Algorithms (DSA):

1️⃣ What is Searching?
Answer:
Searching means finding a specific element inside a collection (array/list).

👉 Simple words:
Data ke andar kisi ek value ko dhundhna.
Example:

[10, 20, 30, 40]
Find 30

2️⃣ Linear Search
Idea:
Check elements one by one from start to end.
Time Complexity: O(n)
👉 Worst case: last element pe milega.
🧑‍💻 Code (Linear Search)
Python
arr = [10, 20, 30, 40]
target = 30

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        
3️⃣ Binary Search
Idea:
Middle element check karo.
Agar target chhota hai → left side
Agar bada hai → right side

⚠ Important:
Binary Search works only on sorted array.
Example:

[10, 20, 30, 40, 50]
🧑‍💻 Code (Binary Search)
Python
arr = [10, 20, 30, 40, 50]
target = 30

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
        
4️⃣ Time Complexity Idea
Algorithm
Time Complexity
Linear Search
O(n)
Binary Search
O(log n)
👉 O(log n) fast hota hai large data me.

📌 SLOT 02: Logistic Regression (Machine Learning Basics):

1️⃣ What is Logistic Regression?
Answer:
Logistic Regression is used for classification problems.
👉 Example: Pass / Fail
Yes / No
0 / 1

2️⃣ Regression vs Classification
Regression
Classification
Predict number
Predict category
Example: marks
Example: pass/fail

3️⃣ Sigmoid Function
Formula:

1 / (1 + e^-x)
Output always between 0 and 1.
👉 Used to convert output into probability.
Graph shape: S-shaped curve.

4️⃣ Small Dataset Example
Marks → Pass/Fail

Marks: [30, 40, 50, 60, 70]
Result: [0, 0, 1, 1, 1]
🧑‍💻 Code (Logistic Regression Example)
Python
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[30], [40], [50], [60], [70]])
y = np.array([0, 0, 1, 1, 1])

model = LogisticRegression()
model.fit(X, y)

prediction = model.predict([[55]])
print("Prediction:", prediction)

🔁 Quick Revision

👉Searching = find element
👉Linear = check one by one
👉Binary = works on sorted data
👉O(n) vs O(log n)
👉Logistic Regression = classification
👉Sigmoid = probability function
👉Output = 0 or 1

✅ Status
Day 08 Completed Successfully 💯🔥
