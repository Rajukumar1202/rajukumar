🧠 Day 15 – Greedy Algorithm Practice & PCA (DSA + ML):

📌 SLOT 01: Greedy Algorithms (Practice Focus):

1️⃣ What is Greedy Algorithm? (Recap)
Greedy algorithm ek aisa approach hai jisme har step par locally best choice li jati hai.

👉 Simple words
Har step par jo best lagta hai wahi choose karo.

Example:
Coin change → sabse bada coin pehle lo.

2️⃣ Greedy Choice Property
Meaning:
Agar har step ka best decision future solution ko disturb nahi kare → greedy work karega.

👉 Important exam point ⭐
Greedy tab work karega jab local best = global best.

3️⃣ When Greedy Works / Fails
✅ Works:
Activity selection
Fractional knapsack
Huffman coding
❌ Fails:
0/1 knapsack
Some coin change cases

👉 Kyuki future impact ignore hota hai.

4️⃣ Greedy vs Dynamic Programming
Greedy
👉Dynamic Programming
👉Local decision
👉Global decision
👉Fast
👉Slow but optimal
👉Easy
👉Complex
👉Not always correct
👉Always optimal

👉 Exam favourite comparison ⭐

5️⃣ Coin Change (Greedy Idea)
Coins = [10, 5, 2, 1]
Amount = 18
👉 Greedy solution
10 → 5 → 2 → 1
🧑‍💻 Code (concept)
Python
coins = [10,5,2,1]
amount = 18
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)

6️⃣ Activity Selection Problem
👉 Goal → maximum activities choose without overlap
Logic:
Activity finish time sort
Jo earliest finish kare → choose
👉 Greedy works ⭐

7️⃣ Fractional Knapsack
👉 Item ko break kar sakte ho
👉 Value/weight ratio highest → pick first
👉 Greedy works because fractional allowed.

📌 SLOT 02: PCA – Principal Component Analysis:

1️⃣ What is Dimensionality Reduction?
Features kam karna but information maintain karna.
👉 Example
100 columns → 10 columns
👉 Model fast + overfitting kam

2️⃣ Why PCA is Used
Feature reduction
Noise removal
Visualization
Faster ML training
👉 Exam line ⭐

3️⃣ Variance Concept
Variance = data spread
👉 PCA high variance direction choose karta hai
Kyuki usme information jyada hoti hai.

4️⃣ Eigenvector Idea (Simple)
👉 Direction jisme data sabse jyada spread hai
👉 PCA → best direction find karta hai
Bas itna samajhna enough ⭐

5️⃣ Feature Reduction Concept
👉 PCA features combine karta hai
Example: Height + Weight + BMI
→ 1 component
👉 Information compress ho jati hai.

6️⃣ Mini PCA Example
Python
from sklearn.decomposition import PCA
import numpy as np

data = np.array([[2,3],[3,4],[4,5],[5,6]])

pca = PCA(n_components=1)
reduced = pca.fit_transform(data)

print(reduced)
👉 2D → 1D convert

🔁 Quick Revision
📌Greedy → local best choice
📌Greedy works when local = global
📌Fractional knapsack → greedy
📌DP → global optimal
📌PCA → dimensionality reduction
📌Variance → information measure
📌Eigenvector → max spread direction
🧪 Coding Practice Questions (with Answer)

✅ Q1 Coin Change Greedy
Question: Count minimum coins for amount 27 (10,5,2,1)
Python
coins = [10,5,2,1]
amount = 27
count = 0

for coin in coins:
    count += amount // coin
    amount %= coin

print(count)
✅ Q2 Activity Selection (Basic Logic)
Question: Print activities that can be selected
Python
start = [1,3,0,5]
finish = [2,4,6,7]

last_finish = 0

for i in range(len(start)):
    if start[i] >= last_finish:
        print(i)
        last_finish = finish[i]
✅ Q3 PCA Reduction
Python
from sklearn.decomposition import PCA
import numpy as np

data = np.array([[1,2],[2,3],[3,4]])
pca = PCA(n_components=1)

print(pca.fit_transform(data))

Day 15 complete ✅🚀😍(❁´◡`❁)
