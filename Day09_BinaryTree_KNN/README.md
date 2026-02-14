🧠 Day 09 – Binary Tree & KNN (DSA + AIML):

📌 SLOT 01: Binary Tree Basics (DSA):

1️⃣ What is a Tree?
A Tree is a non-linear data structure used to store hierarchical data.

👉 Simple words:
Family tree jaisa structure.

2️⃣ Basic Terms
Root → Top node of tree
Node → Each element in tree
Leaf → Node with no children
Example:

A
       / \
      B   C
Root → A
Leaf → B, C

3️⃣ What is a Binary Tree?
A Binary Tree is a tree where each node can have at most 2 children:
Left child
Right child

4️⃣ Tree Traversals
Traversal means visiting every node.

✅ Inorder (Left → Root → Right)
✅ Preorder (Root → Left → Right)
✅ Postorder (Left → Right → Root)

5️⃣ Basic Recursion Idea in Tree
Tree traversal works using recursion.
Because: Each node again behaves like a small tree.

6️⃣ Simple Binary Tree Code (Python)
Python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")

7️⃣ Traversal Code
Inorder
Python
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)
Preorder
Python
def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)
Postorder
Python
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)
        
🔁 Quick Revision (Tree)
👉Tree = Hierarchical structure
👉Binary Tree = Max 2 children
👉Inorder = L R
👉Preorder = R first
👉Postorder = Root last
👉Recursion used in traversal

📌 SLOT 02: K-Nearest Neighbors (KNN – ML)

1️⃣ What is KNN?
KNN is a supervised learning algorithm used for classification.
👉 It predicts based on nearest neighbors.

2️⃣ Supervised Learning
Means: We train model using labeled data.
Example:
Height | Weight | Category
160 | 50 | Slim
180 | 80 | Fit

3️⃣ Distance Calculation (Euclidean Distance)
Formula:

√((x1 - x2)^2 + (y1 - y2)^2)
👉 Distance between two points.

4️⃣ Choosing K
K = number of nearest neighbors
Small K → sensitive
Large K → smooth but slow
Usually odd number choose karte hain (3,5,7)

5️⃣ How Prediction Works
Step 1 → Calculate distance
Step 2 → Find nearest K points
Step 3 → Majority voting
Step 4 → Predict class

6️⃣ Simple KNN Example (Python)
Python
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Dataset
X = np.array([[160,50],[170,65],[180,80]])
y = ["Slim","Fit","Fit"]

# Model
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X,y)

# Prediction
print(model.predict([[175,70]]))

🔁 Quick Revision (KNN)

👉KNN = Supervised algorithm
👉Uses distance
👉K = neighbors
👉Majority voting
👉Used in classification

✅ Status

Day 09 Completed Successfully 💯🔥
