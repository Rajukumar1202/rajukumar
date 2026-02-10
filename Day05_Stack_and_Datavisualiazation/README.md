🧠 Day 05 – Stack & Data Visualization (DSA + AIML):

📌 SLOT 01: Stack Basics (DSA)

1️⃣ What is a Stack?
Answer:
A stack is a linear data structure where elements are added and removed from one end only, called the top.
👉 Simple words:
Plate stack jaisa — upar se hi plate rakho aur upar se hi nikalo.

2️⃣ LIFO Concept (Last In First Out)
Answer:
Jo element last me add hota hai, wahi pehle remove hota hai.
👉 Example:
A → B → C (C last aaya)
Remove → C pehle niklega

3️⃣ Stack Operations
Push → element add karna
Pop → element remove karna
Peek / Top → upar wala element dekhna.

4️⃣ Stack using Python List
Python me stack ko list se bana sakte hain.
🧑‍💻 Code:
Python
stack = []

5️⃣ Push Elements into Stack
🧑‍💻 Code:
Python
stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
📌 Output:

[10, 20, 30]

6️⃣ Pop Elements from Stack
🧑‍💻 Code:
Python
stack = [10, 20, 30]
stack.pop()
print(stack)
📌 Output:

[10, 20]

7️⃣ Check Stack Empty or Not
🧑‍💻 Code:
Python
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
    
📌 SLOT 02: Data Visualization (Python / AIML)

1️⃣ What is Data Visualization?
Answer:
Data visualization ka matlab data ko graph / chart ke form me dikhana.
👉 Numbers ko easily samajhne ke liye.

2️⃣ Why Visualization is Important?
Data easily samajh aata hai
Comparison easy hota hai
ML analysis me helpful

3️⃣ Introduction to Matplotlib
Matplotlib Python library hai jo graphs banane ke kaam aati hai.
🧑‍💻 Import:
Python
import matplotlib.pyplot as plt

4️⃣ Line Plot (Marks of Students)
🧑‍💻 Code:
Python
marks = [60, 70, 80, 90]
plt.plot(marks)
plt.show()
👉 Use: trend dikhane ke liye.

5️⃣ Bar Chart (Subject-wise Marks)
🧑‍💻 Code:
Python
subjects = ["Math", "Python", "DSA"]
marks = [80, 75, 90]

plt.bar(subjects, marks)
plt.show()
👉 Use: comparison ke liye.

6️⃣ Scatter Plot (Hours Studied vs Marks)
🧑‍💻 Code:
Python
hours = [1, 2, 3, 4, 5]
marks = [40, 50, 65, 75, 90]

plt.scatter(hours, marks)
plt.show()
👉 Use: relation dekhne ke liye.

🔁 Quick Revision
👉Stack → LIFO
👉Push → add element
👉Pop → remove element
👉Python list se stack ban sakta hai
👉Matplotlib → graphs banane ke liye
👉Line / Bar / Scatter → basic charts

Day 05 Completed Successfully 💯
