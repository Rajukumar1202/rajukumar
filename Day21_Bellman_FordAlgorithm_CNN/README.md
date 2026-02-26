🧠 Day 21 Notes – Bellman-Ford Algorithm + CNN Optimization:

📌 SLOT 01: Bellman-Ford Algorithm (Graph Shortest Path):

1️⃣ What is Bellman-Ford?
Bellman-Ford is a graph algorithm used to find the shortest path from a single source to all other vertices.
👉 Main advantage → works with negative edge weights

2️⃣ When Bellman-Ford is Used?
Graph contains negative weights
Network routing problems
Currency exchange modeling
⭐ Important exam point

3️⃣ Working Idea of Bellman-Ford
Steps:
Initialize distance array
Relax all edges
Repeat relaxation V-1 times
👉 V = number of vertices

4️⃣ Relaxation Concept
Relaxation means updating distance when a better path is found.
If current distance > new computed distance
→ update distance
👉 Simple idea → keep improving path

5️⃣ Negative Cycle Detection
Bellman-Ford performs one extra iteration:
👉 If distance still decreases → negative cycle exists
⭐ Unique feature of Bellman-Ford
⭐ Memory Tip
Bellman-Ford = Handles negative edges

📌 SLOT 02: CNN Optimization Techniques:

1️⃣ Why Optimization is Needed?
During CNN training, the goal is to minimize loss.
👉 Optimization helps the model learn better weights

2️⃣ Gradient Descent Recap
Gradient descent updates weights step-by-step to reduce error.
👉 Moves in direction of minimum loss

3️⃣ Learning Rate Concept
Learning rate controls the size of weight updates.
Too high → unstable training
Too low → slow learning

4️⃣ Optimizers in CNN
Common optimizers:
SGD
Adam
RMSProp
👉 Adam is most widely used

5️⃣ Batch vs Mini-Batch Training
Batch → full dataset used
Mini-batch → small subset used
👉 Mini-batch gives faster and stable training

6️⃣ Regularization Techniques
Used to reduce overfitting:
Dropout
Weight decay
👉 Helps model generalize better

🔁 Quick Revision
👉Bellman-Ford → shortest path with negative edges
👉Relaxation → distance update
👉Negative cycle → extra iteration detection
👉Optimizer → minimizes loss
👉Learning rate → step size control
👉Adam → popular optimizer

Day 21 complete😇✅(❁´◡`❁)
