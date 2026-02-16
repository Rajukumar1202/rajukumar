🧠 Day 11 – Hashing Collision & Random Forest (DSA + ML):

📌 SLOT 01: Hashing – Collision Handling (DSA):

1️⃣ What is Collision?
Collision happens when two different keys get the same index in a hash table.

👉 Simple words:
2 alag data same jagah store hone aa gaye 😄
Example:

Hash function: key % 5

10 % 5 = 0
15 % 5 = 0
Both go to index 0 → Collision

2️⃣ Why Collision Happens?
Table size limited hoti hai
Hash function perfect nahi hota
Data jyada ho jata hai

3️⃣ Collision Handling Methods
🔹 (A) Chaining
Same index par list bana dete hain.
Example:

Index 0 → [10, 15]
Python Concept:
Python
table = [[] for _ in range(5)]

def insert(key):
    index = key % 5
    table[index].append(key)

insert(10)
insert(15)

print(table)

🔹 (B) Linear Probing
Agar index occupied ho → next empty index check karo.
Example:

Index 0 occupied
Check index 1
Concept:
Python
table = [None] * 5

def insert(key):
    index = key % 5
    while table[index] is not None:
        index = (index + 1) % 5
    table[index] = key
    
4️⃣ Load Factor (Important Concept)
Formula:

Load Factor = Number of elements / Table size
👉 Agar load factor jyada ho gaya → collision badhega
Example:
Table size = 5
Elements = 4
Load factor = 4 / 5 = 0.8 (High)

5️⃣ Time Complexity
Operation
Average
Worst
Insert
O(1)
O(n)
Search
O(1)
O(n)
👉 Agar collision kam → fast
👉 Agar collision jyada → slow
🔥 Practice Question
If table size = 5
Insert: 7 and 12
Where will they go?

📌 SLOT 02: Random Forest (Machine Learning)
1️⃣ What is Random Forest?
Random Forest is a machine learning algorithm that uses multiple decision trees together.
👉 Simple words:
Bahut saare trees milkar decision lete hain.

2️⃣ Ensemble Learning Concept
Ensemble = Multiple models working together.
Example:
Tree 1 → Yes
Tree 2 → No
Tree 3 → Yes
Final Output → YES (Majority voting)

3️⃣ Why Random Forest is Powerful?
✔ Reduces overfitting
✔ More accurate
✔ Stable model
✔ Works well on large data

4️⃣ Overfitting Reduction
Single Decision Tree: Can memorize data → Overfit
Random Forest: Different trees trained on different samples → Balanced decision

5️⃣ Feature Importance
Random Forest tells: Which feature is more important in prediction.
Example: Height may be more important than weight.

6️⃣ Mini Example – Train Random Forest
Python
from sklearn.ensemble import RandomForestClassifier

# Small dataset
X = [[1], [2], [3], [4]]
y = [0, 0, 1, 1]

model = RandomForestClassifier()
model.fit(X, y)

prediction = model.predict([[2]])
print(prediction)
🔥 Practice Question
Why Random Forest performs better than single Decision Tree?

🔁 Quick Revision

🔹Hashing → Fast data access
🔹Collision → Same index problem
🔹Chaining → List at same index
🔹Linear Probing → Next empty index
🔹Load Factor → elements / size
🔹Random Forest → Many trees
🔹Ensemble learning → Multiple models
🔹Voting → Final prediction
🔹Reduces overfitting

✅ Status
Day 11 Completed Successfully 💯🔥
