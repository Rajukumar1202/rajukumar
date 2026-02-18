🧠 Day 13 – Two Pointer + Naive Bayes:

📌 SLOT 1: Two Pointer Technique (DSA):

1️⃣ What is Two Pointer Technique?
Definition: Two Pointer technique is a problem-solving method where we use two indexes (pointers) to traverse an array or string.

👉 Simple words:
Ek left se chalega, ek right se chalega.
Instead of nested loops (O(n²)),
we reduce it to O(n).

2️⃣ When to Use It?
Use when:
Array is sorted
Pair sum problems
Reverse problems
Remove duplicates
Compare elements from both ends

3️⃣ Left & Right Pointer Concept
Imagine:

arr = [1, 2, 3, 4, 5]
       L           R
L = 0
R = last index
We move:
L → forward
R → backward

4️⃣ Time Complexity Idea
Without two pointer: O(n²)
With two pointer: O(n)
👉 Faster. Cleaner. Efficient.
🔥 Example 1: Reverse Array Using Two Pointers
Python
arr = [1, 2, 3, 4, 5]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
Output:

[5, 4, 3, 2, 1]
✅ Practice Question 1:
If array = [10, 20, 30],
after reversing, what will be output?
🔥 Example 2: Pair With Given Sum (Sorted Array)
Python
arr = [1, 2, 4, 6, 8]
target = 10

left = 0
right = len(arr) - 1

while left < right:
    s = arr[left] + arr[right]

    if s == target:
        print("Pair Found:", arr[left], arr[right])
        break
    elif s < target:
        left += 1
    else:
        right -= 1

✅ Practice Question 2:
Why must array be sorted in this method?
🔥 Example 3: Remove Duplicates (Sorted Array)
Python
arr = [1,1,2,2,3,4,4]
result = []

left = 0

while left < len(arr):
    if arr[left] not in result:
        result.append(arr[left])
    left += 1

print(result)
Better optimized version exists, but this is beginner friendly.

📌 SLOT 2: Naive Bayes (Machine Learning)

1️⃣ What is Naive Bayes?
Naive Bayes is a classification algorithm based on probability.
👉 It predicts class using probability.
Used in:
Spam detection
Sentiment analysis
Text classification

2️⃣ Bayes Theorem (Basic Idea)
Formula:

P(A|B) = (P(B|A) * P(A)) / P(B)
Don't panic.
Simple meaning:
Posterior = (Likelihood × Prior) / Evidence

3️⃣ Prior & Posterior
Prior → Probability before seeing data
Posterior → Probability after seeing data
Example:
If 70% emails are spam → Prior
After seeing word "Free" → Posterior changes

4️⃣ Why Called "Naive"?
Because it assumes:
All features are independent.
Which is not always true.
But works surprisingly well.

5️⃣ Spam Detection Example
Dataset:
Message
Label
Free money
Spam
Hi friend
Not Spam
Win cash
Spam

🔥 Train Naive Bayes Model
Python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = ["Free money", "Hi friend", "Win cash"]
labels = [1, 0, 1]   # 1 = Spam, 0 = Not Spam

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

new_text = ["Free cash"]
new_X = vectorizer.transform(new_text)

prediction = model.predict(new_X)

print(prediction)

✅ Practice Question 3:
Why is Naive Bayes good for text data?

🔁 Quick Revision
Two Pointer:
Two indexes
O(n)
Good for sorted arrays
Naive Bayes:
Based on probability
Used for classification
Day 13 complete 😍
Assumes feature independence
🧠 Now Tell Me:
What is time complexity of two pointer method?
What is Prior probability?
Why is it called Naive?
Answer these first.
Fir next level questions karenge 💪
