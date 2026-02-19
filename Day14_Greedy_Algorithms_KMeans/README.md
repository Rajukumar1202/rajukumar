🧠 Day 14 – Greedy Algorithms & K-Means Clustering (DSA + ML):

📌 SLOT 01: Greedy Algorithms (DSA):

1️⃣ What is Greedy Algorithm?

A Greedy Algorithm is an approach where we choose the best option at the current step to get an overall optimal solution.

👉 Simple words:
Har step par best choice karo → final answer mil jayega.

Example idea:
Agar tum shortest time me kaam complete karna chahte ho → har time smallest task pehle karoge.

2️⃣ Greedy Choice Property

Meaning:
Problem aisi honi chahiye jahan local best choice → global best result de.
👉 Har greedy problem me ye property hoti hai.

3️⃣ When Greedy Works and When Fails

✅ Works:

Activity Selection

Fractional Knapsack

Minimum coins (some cases)

❌ Fails:

0/1 Knapsack

Some coin systems

👉 Kyuki local best → global best nahi deta.

4️⃣ Greedy vs Dynamic Programming (Basic)
Greedy	Dynamic Programming
Local best choice	All possibilities check
Fast	Slower
Simple	Complex
Not always optimal	Always optimal

👉 Memory trick:
Greedy = shortcut
DP = full calculation

5️⃣ Example – Coin Change (Basic Greedy)

Goal: minimum coins use karna.

Coins: 10, 5, 1
Amount: 16

👉 10 + 5 + 1 = 3 coins

Greedy → largest coin first.

6️⃣ Activity Selection Problem

Goal: maximum activities select karna without overlap.

👉 Activity ko finish time ke basis par sort karo
👉 Earliest finish wali choose karo

👉 Greedy working example.

7️⃣ Fractional Knapsack Concept

👉 Item ko fraction me le sakte ho
👉 Highest value/weight ratio wala item first

👉 Greedy works ✔

🔥 Practice Question

Why greedy fails in 0/1 knapsack?

📌 SLOT 02: K-Means Clustering (Machine Learning):

1️⃣ Recap – What is Clustering?

Clustering = similar data ko group karna.

👉 Example: customer groups

2️⃣ What is K-Means?

K-Means is an unsupervised ML algorithm that divides data into K clusters.

👉 K = number of groups

3️⃣ How K-Means Works (Step-by-Step)

👉Choose K
👉Select random centroids
👉Assign points to nearest centroid
👉Update centroid
👉Repeat until stable
👉 Ye loop hi K-Means ka core hai.

4️⃣ Choosing Value of K (Elbow Method)

Idea:
Different K try karo → error plot karo

👉 Jahan curve bend kare → best K

👉 Isko elbow bolte hain.

5️⃣ Mini Example – Apply K-Means
from sklearn.cluster import KMeans
import numpy as np

data = np.array([[1,2],[1,4],[1,0],[10,2],[10,4],[10,0]])

model = KMeans(n_clusters=2)
model.fit(data)

print(model.labels_)


👉 Output → cluster labels

6️⃣ Visualization of Clusters
import matplotlib.pyplot as plt

plt.scatter(data[:,0], data[:,1], c=model.labels_)
plt.show()


👉 Scatter me clusters dikhenge.

🔥 Practice Question

What happens if K is chosen too large?

🔁 Quick Revision

1️⃣Greedy → local best choice

2️⃣Works only when greedy property holds

3️⃣Activity selection → greedy example

4️⃣K-Means → clustering algorithm

5️⃣Steps → assign → update → repeat

6️⃣Elbow → best K selection

✅ Status

Day 14 Completed Successfully 💯
