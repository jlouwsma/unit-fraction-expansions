The file unitfractionexpansions.py contains Python code to produce all solutions of $\sum_{i=1}^n 1/x_i = 1$, where the $x_i$ are positive integers of the form $x_i = 2^{a_i} k^{b_i}$ with $x_1 \leq \cdots \leq x_n$.  

Here $k$ is any odd positive integer at least $3$, the $a_i$ are elements of $\{0,1,2\}$ that can vary with $i$, and the $b_i$ are nonnegative integers that can vary with $i$.  

Version 0.1; Date: February 11, 2024  
Author: Joel Louwsma, jlouwsma@niagara.edu  

This implements the algorithm described in "On solutions of $\sum_{i=1}^n 1/x_i = 1$ in integers of the form $2^a k^b$, where $k$ is a fixed odd positive integer" by Joel Louwsma  

A solution is called *nontrivial* if $b_i \geq 1$ for some $i$.  

FindSolutions(k,n) returns a list of solutions for k with n terms  
CountSolutions(k,n) returns the number of solutions for k with n terms  
FindNontrivialSolutions(k,n) returns a list of nontrivial solutions for k with n terms  
CountNontrivialSolutions(k,n) returns the number of nontrival solutions for k with n terms  
FindDistinctSolutions(k,n) returns a list of solutions for k with n terms where the $x_i$ are distinct  
CountDistinctSolutions(k,n) returns the number of solutions for k with n terms where the $x_i$ are distinct  
FindNontrivialDistinctSolutions(k,n) returns a list of nontrivial solutions for k with n terms where the $x_i$ are distinct  
CountNontrivialDistinctSolutions(k,n) returns the number of nontrivial solutions for k with n terms where the $x_i$ are distinct  
