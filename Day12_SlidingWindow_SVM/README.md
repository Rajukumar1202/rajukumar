🧠 Day 12 – Sliding Window & Support Vector Machine (DSA + ML):

📌 SLOT 01: Sliding Window Technique (DSA):

1️⃣ What is Sliding Window?
Definition: Sliding Window is a technique used to reduce nested loops into a single loop by maintaining a window (range) over data.

👉 Simple words:
Ek chhota sa frame (window) data par slide karta rehta hai.

2️⃣ Why It Is Used?
Reduces time complexity
Avoids recalculating same values
Converts O(n²) → O(n) in many problems
Example: Instead of checking every subarray again and again, we update only the changed element.

3️⃣ Fixed Window vs Variable Window
🔹 Fixed Window
Window size fixed hota hai (like size K).
Example: Maximum sum subarray of size K.
🔹 Variable Window
Window size change hota hai condition ke hisaab se.
Example: Longest substring without repeating characters.

4️⃣ Time Complexity Idea
Without Sliding Window → O(n²)
With Sliding Window → O(n)
👉 Less loops = faster code.

✅ Example 1: Maximum Sum Subarray of Size K
Python
arr = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(arr[:k])
max_sum = window_sum

for i in range(k, len(arr)):
    window_sum = window_sum + arr[i] - arr[i-k]
    max_sum = max(max_sum, window_sum)

print("Maximum Sum:", max_sum)

✅ Example 2: Longest Substring Without Repeating Characters
Python
s = "abcabcbb"
left = 0
seen = set()
max_length = 0

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left += 1
    seen.add(s[right])
    max_length = max(max_length, right - left + 1)

print("Longest Length:", max_length)

🔥 Practice Question
If array = [1,2,3,4,5] and K = 2
What is maximum sum subarray?

🔁 Quick Revision (DSA)
🔹Sliding Window reduces time complexity
🔹Fixed window → size constant
🔹Variable window → size changes
🔹Two-pointer approach helpful
🔹Used in substring / subarray problems

📌 SLOT 02: Support Vector Machine (SVM – ML)

1️⃣ What is SVM?
SVM is a supervised learning algorithm used for classification and regression.
👉 Main idea: Separate data using the best possible line.

2️⃣ Classification Concept
Example: Marks → Pass / Fail
Height, Weight → Category
Model learns boundary between classes.

3️⃣ Hyperplane Idea
Hyperplane = Decision boundary line.
In 2D → Line
In 3D → Plane
SVM tries to find: 👉 The line that separates classes best.

4️⃣ Margin Concept
Margin = Distance between hyperplane and nearest data points.
SVM tries to: 👉 Maximize margin.
Bigger margin = Better generalization.

5️⃣ Kernel Trick (Basic Idea)
Sometimes data is not linearly separable.
Kernel helps to: 👉 Convert data into higher dimension
So it becomes separable.
Common kernels:
Linear
Polynomial
RBF
No deep math needed now.

✅ Mini Example – Train SVM
Python
from sklearn import svm

# Small dataset
X = [[2, 3], [1, 1], [2, 1], [3, 2]]
y = [1, 0, 0, 1]

model = svm.SVC(kernel='linear')
model.fit(X, y)

prediction = model.predict([[2,2]])
print("Prediction:", prediction)

🔁 Compare with Logistic Regression
Logistic Regression → Probability based
SVM → Margin maximization
SVM better for small datasets sometimes
🔥 Practice Question
What happens if margin is very small?
Is model strong or weak?

Day 12 complete ✅🚀
