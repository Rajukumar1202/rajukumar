🧠 Day 10 – Hashing & Decision Tree (DSA + ML):

📌 SLOT 01: Hashing Basics (DSA):

1️⃣ What is Hashing?
Hashing is a technique used to store and access data quickly using a special function called a hash function.

👉 Simple words:
Data ko ek special index number par store karna taaki turant mil jaye.

2️⃣ Hash Table / Hash Map
A Hash Table stores data in:

Key → Value
Example:

Name → Raju
Age  → 20
In Python, dictionary is a hash map.
Code:
Python
student = {
    "name": "Raju",
    "age": 20
}

print(student["name"])
Output:

Raju

3️⃣ Why Hashing is Fast?
Searching in:
List → O(n)
Hash map → O(1) average
👉 Means constant time (almost same speed even if data increases)

4️⃣ Frequency Counting (Very Important for Interviews)
Example: Count frequency of numbers
Python
nums = [1, 2, 2, 3, 1, 2]

freq = {}

for n in nums:
    if n in freq:
        freq[n] += 1
    else:
        freq[n] = 1

print(freq)
Output:

{1: 2, 2: 3, 3: 1}
Practice Question 🔥
If:
Python
word = "apple"
How many times each character appears?
(Socho — hash map use karo.)

📌 SLOT 02: Decision Tree (Machine Learning):

1️⃣ What is Decision Tree?
A Decision Tree is a machine learning algorithm used for classification and regression.
👉 It makes decisions like a flowchart.

2️⃣ Tree Structure
Root Node → Starting question
Decision Node → Condition
Leaf Node → Final output
Example:

Weather?
  |
  |-- Sunny → Don't Play
  |-- Rainy → Play
  
3️⃣ Gini Index / Entropy (Basic Idea)
These are used to measure how pure a split is.
👉 Simple words:
If all values same → Good split
If mixed values → Bad split
You don’t need deep math now.

4️⃣ Overfitting
Overfitting means:
Model remembers training data too much.
👉 Works perfectly on training data
👉 Fails on new data
Solution:
Limit tree depth
Use pruning

5️⃣ Mini Example – Train Decision Tree
Python
from sklearn.tree import DecisionTreeClassifier

# Example dataset
# 0 = No, 1 = Yes
weather = [[1], [0], [1], [0]]   # 1 = Rainy, 0 = Sunny
play = [1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(weather, play)

prediction = model.predict([[1]])
print(prediction)
Practice Question 🔥
If tree depth is too high, what problem can happen?

🔁 Quick Revision.
👉Hashing → Key–Value storage
👉Dictionary in Python → Hash map
👉Search time → O(1) average
👉Decision Tree → Flowchart model
👉Overfitting → Model too specific

Day 10  Hashing and Decision Tree Complete✅😍😇
