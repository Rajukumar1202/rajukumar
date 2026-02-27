🧠 Day 22 Notes – A Search Algorithm + Transfer Learning*

📌 SLOT 01: A Search Algorithm (Graph Search)*

1️⃣ What is A Algorithm?*
A* (A-star) is a graph search algorithm used to find the shortest path efficiently using both actual cost and heuristic estimate.
👉 Combines Dijkstra + Greedy Search

2️⃣ Where A is Used?*
GPS navigation
Game pathfinding
Robotics movement
⭐ Important real-world algorithm

3️⃣ A Evaluation Function*
A* uses formula:
👉 f(n) = g(n) + h(n)
Where:
g(n) → actual cost from start
h(n) → heuristic estimate to goal
👉 f(n) → total estimated cost

4️⃣ Heuristic Function
Heuristic gives idea of remaining distance.
Examples:
Manhattan distance
Euclidean distance
👉 Good heuristic → faster search

5️⃣ Working Idea
Steps:
Start node open list me add
Lowest f(n) node choose
Neighbors explore
Goal mile → stop
👉 Priority queue used internally
⭐ Memory Tip
A = Actual cost + Guess cost*

📌 SLOT 02: Transfer Learning (Deep Learning):

1️⃣ What is Transfer Learning?
Transfer learning means using a pre-trained model and adapting it to a new task.
👉 Already learned knowledge reuse

2️⃣ Why Transfer Learning is Used?
Less data required
Faster training
Better performance
⭐ Very practical ML technique

3️⃣ Example
ImageNet trained model → new image task
👉 Just last layers retrain

4️⃣ Feature Extraction
Model early layers freeze
Only final layers train
👉 Extract features from pretrained network

5️⃣ Fine Tuning
Some deeper layers also retrain
👉 Model adapts better to new task

6️⃣ Popular Transfer Learning Models
VGG
ResNet
MobileNet
EfficientNet
👉 Widely used CNN backbones

🔁 Quick Revision
👉A* → shortest path using heuristic
👉f(n) = g(n) + h(n)
👉Heuristic → estimated cost
👉Transfer learning → reuse pretrained model
👉Feature extraction → freeze layers
👉Fine tuning → retrain layers

Day 22 complete🚀✅😍(❁´◡`❁)
