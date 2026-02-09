🧠 Day 04 – Linked List & Data Cleaning (DSA + AIML)

📌 SLOT 01: Linked List Basics (DSA)

1️⃣ What is a Linked List?
Answer:
A linked list is a linear data structure where elements are stored in non-continuous memory.
Each element is called a node.
👉 Simple words:
Data alag-alag jagah hota hai, aur link se juda hota hai.

2️⃣ Node (Data + Next)
Answer:
A node has two parts:
Data → value store karta hai
Next → next node ka address
🧑‍💻 Code:
Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

3️⃣ Singly Linked List
Answer:
Sirf forward direction me move hota hai
Last node ka next = None

4️⃣ Traversing a Linked List
Answer:
Traversing ka matlab:
👉 har node ko ek-ek karke visit karna
🧑‍💻 Code:
Python
temp = head
while temp:
    print(temp.data)
    temp = temp.next

5️⃣ Insert Node at End (Basic Idea)
Answer:
New node ko list ke last me add karna.
👉 Steps:
New node banao
Last node tak jao
Last node ke next me new node add karo.

📌 SLOT 02: Data Cleaning using Pandas (AIML)

1️⃣ What is Data Cleaning?
Answer:
Data cleaning ka matlab:
Galat data hatana
Missing data fill karna
Duplicate data remove karna
👉 ML ke liye accurate data banana.

2️⃣ Missing Values (NaN)
Answer:
Missing value ko Pandas me NaN (Not a Number) kehte hain.

3️⃣ Fill Missing Values
🧑‍💻 Code:
Python
import pandas as pd

df.fillna(0)
👉 Mean se fill:
Python
df.fillna(df.mean())

4️⃣ Drop Rows / Columns
🧑‍💻 Code:
Python
df.dropna()

5️⃣ Remove Duplicate Data
🧑‍💻 Code:
Python
df.drop_duplicates()


🔁 Quick Revision
👉Node = data + next.
👉Traversing = ek-ek node visit.
👉Data cleaning = clean & usable data.
👉fillna() → missing value fill.
👉drop_duplicates() → duplicate remove.

✅ Day 04 Completed Successfully 💯
