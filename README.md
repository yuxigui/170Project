# CS 170 Project Fall 2020

<!-- ABOUT THE PROJECT -->
## About The Project
2020 has been a stressful year, and CS 170 course staff is trying to reduce student stress and increase student happiness
as much as possible. Since school has been reduced to a series of awkward Zoom breakout rooms, we figured this is
a good place to start. We noticed that student stress and happiness fluctuate greatly depending on how they are split
into breakout rooms, so we are looking to find a way to divide up stressed 170 students to make them a little happier.
However, this sounds like a really difficult task, so we decided to outsource this to you. 

Project Spec: https://cs170.org/assets/pdf/project_spec.pdf

## Algorithm
For small inputs of size 5, we used brute force to solve them to guarantee accuracy since each input takes about 1 minute to solve using brute force. For inputs of size 10 and 20, we wrote a greedy algorithm along with a backtracking approach that approximately gives the optimal solution. Each input takes about 1-2 minute to solve using this greedy backtracking approach.

## Instructions
You'll only need to install networkx to work with the starter code. For installation instructions, follow: https://networkx.github.io/documentation/stable/install.html

## Files
- `parse.py`: functions to read/write inputs and outputs
- `solver.py`: where you should be writing your code to solve inputs
- `utils.py`: contains functions to compute cost and validate NetworkX graphs

### Built With
* [Python](https://www.python.org/)

