🧠 Day 23 Notes – Union-Find + Batch Normalization:

📌 SLOT 01: Union-Find (Disjoint Set Data Structure):

1️⃣ What is Union-Find?
Union-Find is a data structure used to manage disjoint sets and efficiently check whether two elements belong to the same set.
👉 Also called Disjoint Set Union (DSU)

2️⃣ Main Operations
Find(x) → Find representative (parent) of element
Union(x, y) → Merge two sets
👉 Used to detect connectivity

3️⃣ Where Union-Find is Used?
Cycle detection in graphs
Kruskal’s Algorithm (MST)
Network connectivity
⭐ Important for graph problems

4️⃣ Parent Array Idea
Each element initially points to itself.
When union happens → parent updates.
Example:
If parent[2] = 1
→ 2 belongs to set whose leader is 1

5️⃣ Path Compression
Optimization technique:
During find operation → directly attach node to root.
👉 Makes future operations faster

6️⃣ Union by Rank
Attach smaller tree under bigger tree.
👉 Keeps tree height small
👉 Improves efficiency
⭐ Memory Tip
Union-Find = Find leader + Merge groups

📌 SLOT 02: Batch Normalization (Deep Learning):

1️⃣ What is Batch Normalization?
Batch Normalization is a technique used to normalize layer inputs during training.
👉 Helps stabilize and speed up training

2️⃣ Why Batch Norm is Needed?
Reduces internal covariate shift
Allows higher learning rate
Makes training more stable

3️⃣ How It Works
For each mini-batch:
Compute mean
Compute variance
Normalize values
Formula idea:
(x - mean) / sqrt(variance + epsilon)

4️⃣ Benefits
Faster convergence
Reduces overfitting slightly
Less sensitive to initialization

5️⃣ Where Applied?
Usually applied after:
Linear layer or Convolution layer
Before activation function
⭐ Memory Tip
BatchNorm = Normalize → Stabilize → Accelerate

🔁 Quick Revision
⭐Union-Find → manage disjoint sets
⭐Find → get leader
⭐Union → merge sets
⭐Path compression → faster find
⭐BatchNorm → normalize activations
⭐Helps stable & fast training

Day 23 complete😍✅🚀😇(❁´◡`❁)
