```
Course: CS420 - Artificial Intelligence
Class 15CTT – Term I/201 8 - 2019
```
# Lab 01

```
Your program should be programmed in C++ or Python. Write down your report on
a PDF File. Finally, submit your work to Moodle before
Oct. 2 8 th, 2018 , 23:
```
You are given a graph and a pair of **source** _–_ **destination** nodes. Write a program to find a
path from **source** to **destination** using the following search strategies
a. Breath-first search (BFS)
b. Depth-first search (DFS)
c. Uniform-cost search (UCS)
You are asked to collect **a set of at least 5 graphs** and then run the above search
strategies on the same graphs. Make a comprehensive comparison of these algorithms
according to the order of expanded nodes and the path returned.
_Hint:_

- _Some limits in terms of running time or maximum depth may be useful to prevent DFS_
    _from infinite loops when it is unable to find a solution with a reasonable cost._
- _Graphs demonstrating different types of path (i.e. the destination is near or far from_
    _the source) are useful for your analysis._
**1. Specifications**
- **Input:** the given graph is represented by its adjacency matrix, which is stored in the file
**input.txt**. The input file format is described as follows:
- The first line contains an integer N indicating the number of nodes in the graph.
- The second line stores three integers separated by white spaces. They represent
the indices of source and destination, and the search strategy (whose possible
values are 0 = BFS, 1 = DFS, and 2 = UCS), respectively.
- The N next lines represent the N  N adjacency matrix. Each line contains N
integers separated by white spaces. [i, j] = A > 0 (A is an integer) if there is a link
from node i to node j with a weight of A, and [i, j] = 0 otherwise.


- **Output** : the result is stored in the file **output.txt** , whose format is described as follows:
    - If a path from the source to the destination exists
       ▪ The first line contains the order of expanded nodes
       ▪ The second line show nodes in the path return by the strategy.
    - Otherwise: the first line contains an optional notification.
       ▪ The first line contains the order of expanded nodes
       ▪ The second line show a notification of search failure
    - Nodes are represented using their indices separated by white spaces.
- The **main function** must perform the following basic actions
    - Read the input data from the input file and store it in appropriate data
       structures.
    - Call the function **BFS** (or **DFS, UCS** ), which implements the Breadth-first search
       (or Depth-first search, Uniform-cost), to find a path from **source** to **destination**.
    - Show the outputs.
- When there are many candidate nodes with equal possibilities, **the algorithms must**
    **visit them following their ascending index ordering**.
- Use relative paths for the input and output file and do not change their names. Your
    program needs these requirements to be graded automatically.

An example of the input graph and its corresponding files **input.txt** and **output.txt**
Graph input.txt output.txt Note
5
0 3 0
0 2 0 0 1
0 0 5 0 6
0 0 0 3 0
0 1 0 0 0
0 0 0 1 0

0 1 4 2 3
0 4 3

Another example with the same input graph yet a different pair of source – destination and
a different search strategy.
Graph input.txt output.txt Note
5
**3 0 1**
0 2 0 0 1
0 0 5 0 6
0 0 0 3 0
0 1 0 0 0
0 0 0 1 0

 3 1 2 4
No path is found.


