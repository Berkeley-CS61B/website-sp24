---
layout: page
title: "Asymptotics Solutions - Lab 7: BSTMap"
categories: lab
released: true
searchable: true
---

## Asymptotics Problems Solutions

1. False. Worst case is $\Theta(N)$, for a spindly BST
2. False. Worst case is $\Theta(N)$
3. False. Best case is $\Theta(\log(N))$, for a bushy BST
4. True
5. True (remember that big-O need not be tight unless otherwise specified!)
6. False. In the best case, these nodes are near the root. Note that if `C` and `K` are randomly chosen, then this is True in the amortized case, since the depth of the average node in the tree is given by the sum
   $$ \sum\_{h=1}^{\lg n} \frac{h2^h}{N} \in \Theta(\log N)$$

{:start="7"} 7. `mystery` finds the `z`th largest element in the BST (indexed from 1). It does this by calculating the number of elements in the left subtree, then going to the right or left subtree depending on whether we have too many elements in the left subtree or not enough. Note that `numLeft` will take proportional time to the number of nodes in the left subtree, so the amount of work in one recursive subcall is $\Theta(\text{number of nodes in left subtree})$.

There are no conditions on the tree, so we must consider when the tree is bushy,
left-spindly, and right-spindly. The best-case will be when the root of the tree is exactly the `z`th largest element, in which case it will take $\Theta(\text{number of nodes in left subtree})$ time (because there is no recursive call).

- Bushy Tree: There are $\frac{N}{2} - 1$ nodes in the left subtree,
  so the runtime is $\Theta(N)$ in the best case (when `z == N / 2`).
- Spindly Tree (Left): There are $N - 1$ nodes in the left subtree,
  so the runtime is $\Theta(N)$ in the best case (when `z == N`).
- Spindly Tree (Right): There are $0$ nodes in the left subtree, so the runtime is $\Theta(1)$ in the best case (when `z == 1`).

Hence the best-case runtime is $\Theta(1)$.

The worst case occurs when we have to traverse all the way down to the leaves of the tree.

- Bushy Tree: For the first recursive call, there are about $\frac{N}{2}$ nodes in the left subtree, then there will be about $\frac{N}{4}$ nodes in the left subtree of the second recursive call, and so on, until we hit a leaf. This means that the worst-case runtime is $\frac{N}{2} + \frac{N}{4} + \frac{N}{8} + \dots + 1 \in \Theta(N)$ (when `z == 1`).
- Spindly Tree (Left): In this case, each recursive call will have one less node in the left subtree as the parent node. This yields a sum of $N + (N-1) + (N-2) + \dots + 1 \in \Theta(N^2)$ (when `z == 1`).
- Spindly Tree (Right): There are $0$ nodes in the left subtree at each recursive call, and the height of the tree is $N$, so the worst-case runtime is $\Theta(N)$ (when `z == N`).

From the above cases, we see that the worst-case runtime is $\Theta(N^2)$.

Summary: Best-case: $\Theta(1)$. Worst-case: $\Theta(N^2)$.
