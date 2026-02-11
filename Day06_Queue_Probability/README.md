🧠 Day 06 – Queue & Probability Basics (DSA + AIML):

📌 SLOT 01: Queue Basics (DSA).

1️⃣ What is a Queue?
Answer:
A queue is a linear data structure where elements are added from one end (rear) and removed from the other end (front).

👉 Simple words:
Bus line jaisa — jo pehle aata hai, wahi pehle jata hai.

2️⃣ FIFO Concept (First In First Out)
Answer:
Jo element pehle add hota hai, wahi pehle remove hota hai.

👉 Example:
10 → 20 → 30
Remove → 10 pehle niklega

3️⃣ Queue Operations

👉Enqueue → element add karna
👉Dequeue → element remove karna
👉Front → pehla element dekhna

4️⃣ Queue using Python List
Python me queue ko list se bana sakte hain.

🧑‍💻 Code:
queue = []

5️⃣ Enqueue Elements

🧑‍💻 Code:

queue = []

queue.append(10)
queue.append(20)
queue.append(30)

print(queue)


📌 Output:
[10, 20, 30]

6️⃣ Dequeue Elements

🧑‍💻 Code:

queue = [10, 20, 30]

queue.pop(0)

print(queue)


📌 Output:
[20, 30]

7️⃣ Check Queue Empty or Not
🧑‍💻 Code:

if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")

📌 SLOT 02: Probability Basics (AIML / Python):

1️⃣ What is Probability?
Answer:
Probability batata hai ki koi event hone ka chance kitna hai.

Formula:

Probability = Favorable outcomes / Total outcomes

👉 Example:
Dice me 6 sides
Probability of getting 3:

1 / 6

2️⃣ Mean (Average)

Mean = Average value
🧑‍💻 Code:
numbers = [10, 20, 30, 40]
mean = sum(numbers) / len(numbers)
print(mean)

3️⃣ Median

Median = Middle value
🧑‍💻 Code:

import numpy as np

numbers = [10, 20, 30, 40]
print(np.median(numbers))

4️⃣ Mode

Mode = Most repeated value
🧑‍💻 Code:

from statistics import mode

numbers = [2, 4, 4, 6]
print(mode(numbers))

5️⃣ Variance (Basic Idea)

Variance batata hai data kitna spread hai.
🧑‍💻 Code:

import numpy as np

numbers = [2, 4, 6, 8]
print(np.var(numbers))

🎯 Simple Probability Example

Probability of getting number > 5 from 1–10

Numbers > 5 → 6, 7, 8, 9, 10
Total numbers → 10

Probability = 5 / 10 = 0.5

🔁 Quick Revision

🎯Queue → FIFO
🎯Enqueue → add element
🎯Dequeue → remove element
🎯Mean → average
🎯Median → middle value
🎯Mode → most frequent
🎯Variance → spread of data

✅ Status

Day 06 Completed Successfully 💯
