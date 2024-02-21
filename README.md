# Budgeted Purchase Problem Solutions

This repository contains two Python implementations for solving the Budgeted Purchase Problem – one using the Iterative Deepening Algorithm and the other using the Hill Climbing Algorithm with Random Restarts.

## Description

The Budgeted Purchase Problem is a classic problem in computer science and artificial intelligence. It involves selecting items under a given budget constraint to maximize the total value. We have approached this problem using two different algorithms:

1. **Iterative Deepening Algorithm**: A depth-first search approach with increasing depth for systematic exploration.
2. **Hill Climbing Algorithm with Random Restarts**: A heuristic search technique with random restarts to avoid local maxima.

### Executing the Programs

1. **Iterative Deepening Algorithm**:
   - Place your input file (`testID.txt`) in the same directory as the script `Budget-ID.py`.
   - Run the script using Python:
     ```bash
     python Budget-ID.py
     ```
   - The script reads the input file, processes it, and prints the solution.

2. **Hill Climbing Algorithm with Random Restarts**:
   - Place your input file (`testHC.txt`) in the same directory as the script `Budget-HC.py`.
   - Run the script using Python:
     ```bash
     python Budget-HC.py
     ```
   - The script reads the input file, processes it, and prints the solution.

## Input File Format

- The first line should contain the target value, budget, and a flag ('V' for verbose, 'C' for compact). For the Hill Climbing algorithm, also include the number of restarts.
- Each subsequent line should list an object's name, value, and cost.
