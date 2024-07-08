## unitfractionexpansions.py

Version 0.2  
Date: July 8, 2024  
Author: Joel Louwsma, jlouwsma@niagara.edu  

This file contains Python code to produce all solutions of $\displaystyle\sum_{i=1}^n 1/x_i = 1$ in integers $x_i = 2^{a_i} k^{b_i}$ with $x_1 \leq \cdots \leq x_n$. Here $k$ is any positive integer that is not a power of $2$, the $a_i$ are elements of $\lbrace 0,1,2 \rbrace$ that can vary with $i$, and the $b_i$ are nonnegative integers that can vary with $i$. The algorithm is described in [this paper](https://arxiv.org/abs/2402.09515) by Joel Louwsma, and solutions are stored as arrays as described there.

Changes for version 0.2: Extend functionality by allowing k to be any positive integer that is not a power of 2 rather than an odd integer at least 3. These changes correspond to the changes from arXiv version 1 to arXiv version 2 of the corresponding paper.

### Functionality

* **FindSolutions(k,n)** returns a list of solutions for k with n terms  
* **CountSolutions(k,n)** returns the number of solutions for k with n terms  
* **FindNontrivialSolutions(k,n)** returns a list of nontrivial (some $b_i \geq 1$) solutions for k with n terms  
* **CountNontrivialSolutions(k,n)** returns the number of nontrival (some $b_i \geq 1$) solutions for k with n terms  
* **FindDistinctSolutions(k,n)** returns a list of solutions for k with n terms where the $x_i$ are distinct  
* **CountDistinctSolutions(k,n)** returns the number of solutions for k with n terms where the $x_i$ are distinct  
* **FindNontrivialDistinctSolutions(k,n)** returns a list of nontrivial (some $b_i \geq 1$) solutions for k with n terms where the $x_i$ are distinct  
* **CountNontrivialDistinctSolutions(k,n)** returns the number of nontrivial (some $b_i \geq 1$) solutions for k with n terms where the $x_i$ are distinct  
