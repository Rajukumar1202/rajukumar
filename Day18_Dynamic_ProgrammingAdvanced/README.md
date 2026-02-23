🧠 Day 18 Notes – Dynamic Programming (Advanced) + Optimizers:

📌 SLOT 01: Dynamic Programming (Advanced):

1️⃣ Memoization vs Tabulation

✅ Memoization (Top-Down)
Recursion use hota hai + result store hota hai
👉 Jab function call hota hai tab compute hota hai

✅ Tabulation (Bottom-Up)
Loop use hota hai + table fill hota hai
👉 Base case se start karke answer tak jate hain

👉 Simple rule:
Memoization = recursion + cache
Tabulation = loop + table

2️⃣ Space Optimization in DP

Kabhi full DP table ki zarurat nahi hoti.
Sirf last values se kaam chal jata hai.

👉 Example Fibonacci
Full array ki jagah 2 variables se kaam ho sakta hai.

👉 Benefit → memory kam lagti hai

3️⃣ Identify DP Pattern

DP use karne ka hint:
Problem optimization hai (min/max)
Same subproblem repeat ho raha
Recursive solution slow hai
👉 Tab DP apply karo

4️⃣ 0/1 Knapsack Idea

Items → weight + value
Goal → max value with limited capacity

👉 Decision: item lo ya skip karo.
👉 DP table se solve hota hai.

5️⃣ Longest Increasing Subsequence (LIS)

Array me longest increasing sequence find karna

👉 Example
[3, 10, 2, 11]
LIS → 3,10,11

👉 DP se easily solve hota hai

📌 SLOT 02: Optimization Algorithms (SGD, Adam):

1️⃣ What is Optimizer?

Optimizer neural network ka learning controller hota hai jo weights update karta hai.

👉 Goal → loss minimize karna

2️⃣ Stochastic Gradient Descent (SGD)

SGD ek simple optimizer hai jo har step par weight update karta hai.

👉 Simple
👉 Fast
👉 Noisy updates

👉 Real-life: thoda-thoda learning

3️⃣ Adam Optimizer

Adam advanced optimizer hai jo adaptive learning rate use karta hai.

👉 Stable
👉 Fast convergence
👉 Deep learning me most used

👉 Adam = smart SGD

4️⃣ Learning Rate Importance

Learning rate = step size

👉 Too high → overshoot
👉 Too low → slow learning

👉 Balanced LR best hota hai

5️⃣ Compare SGD vs Adam

SGD → simple, noisy
Adam → stable, fast

👉 Beginner projects → Adam best

🔁 Quick Revision

👉Memoization → recursion storage
👉Tabulation → loop table
👉Space optimization → memory save
👉Optimizer → weight update controller
👉Adam → smart optimizer

Day18 complete✅😍🚀(❁´◡`❁)
