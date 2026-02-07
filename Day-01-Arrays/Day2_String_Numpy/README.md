🧠 Day 02 – Strings (DSA) + NumPy Basics (AIML):

📌 SLOT. 01: String Basics (DSA)

(String = Text data)

1️⃣ What is a String?
✅ Answer:
A string is a collection of characters written inside quotes.

👉 Simple words:
Text jo " " ya ' ' ke andar ho.

🧑‍💻 Code:

name = "Raju"
city = "Jaipur"
print(name)
print(city)
📌 Output:
Raju
Jaipur

2️⃣ String Indexing?
✅ Answer:
Each character in a string has a position called index.
Index always starts from 0.

🧑‍💻 Code:

word = "CODE"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
📌 Output:
C
O
D
E


📌 Yaad rakho:

Index → 0  1  2  3
Value → C  O  D  E


3️⃣ Length of a String?
✅ Answer:
Length means total number of characters in a string.

🧑‍💻 Code:

text = "HELLO"
print(len(text))

📌 Output:
5


4️⃣ Traversing a String

✅ Answer:
Traversing means printing characters one by one using loop.

🧑‍💻 Code:

word = "RAM"
for ch in word:
    print(ch)
📌 Output:
R
A
M


5️⃣ Basic String Programs

🔹 Program 1: Reverse a String

s = "CODE"
rev = ""

for ch in s:
    rev = ch + rev

print(rev)

📌 Output:

EDOC


🔹 Program 2: Count vowels

word = "apple"
count = 0

for ch in word:
    if ch in "aeiou":
        count += 1

print(count)

📌 Output:

2


🔹 Program 3: Palindrome Check

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

📌 Output:

Palindrome

📌 SLOT. 02: NumPy Basics (Python for AIML)

6️⃣ What is NumPy?
✅ Answer:
NumPy is a Python library used for fast numerical calculations.
It is very important for Machine Learning & Data Science.

👉 Why NumPy?

Fast.
Works with arrays.
Used in AI / ML.


7️⃣ Creating NumPy Arrays

🧑‍💻 Code:

import numpy as np

arr = np.array([1, 2, 3])
print(arr)

📌 Output:
[1 2 3]


8️⃣ Shape of Array
✅ Answer:
Shape tells number of rows and columns.

🧑‍💻 Code:

arr2 = np.array([[1,2],[3,4]])
print(arr2.shape)

📌 Output:
(2, 2)


9️⃣ Basic NumPy Operations
import numpy as np

a = np.array([1, 2, 3])

print(np.sum(a))     # Sum
print(np.mean(a))    # Mean
print(a + 2)         # Add
print(a * 2)         # Multiply

📌 Output:
6
2.0
[3 4 5]
[2 4 6]

🔁 Quick Revision

✅String = text inside quotes.
✅Index starts from 0.
✅len() gives length.
✅Loop se string traverse hota hai.
✅NumPy = fast math library.
✅shape gives structure.



🎯 Day 02 Completed Successfully 🫡🥳
