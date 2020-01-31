# Sort of War

## Description

This is a small terminal program that does a basic step-by-step visualization of some sorting algorithms (currently Bubble sort, Insertion sort, Quick sort, and Selection sort). On top of this, they are shown as tug of war teams, where loser has to advance towards the middle.

## Features

The program randomly chooses two algorithms from a preconfigured list of many algorithms. Then, the simulation starts, where every step of swapping or iterating through a list is shown. Once the sorting is done, the tug of war part of the program adjusts the view, where the losing side has to advance a random amount of cells (1-3). The program will keep running until someone loses. The program adjusts to the size of the current terminal window, with minimum requirement being 36 by 17. Depending on the size of the terminal, the program will display a suitable amount of players on each side. For example, if the terminal is of the minimum size, only 1 person on each side will be drawn.

### Note

Of course, no algorithms were born equal (apart from insertion and bubble sorts), so the execution will always be heavily skewed towards one side, practically making the outcome 100% predictable every time. However, it was fun coding it. 😊

## Screenshots

1. Horizontal terminal orientation

![alt text](./img/1.png "Horizontal")

2. Vertical terminal orientation

![alt text](./img/2.png "Vertical")

## Requirements

- Python 3

## How to Run

In the root directory of the project:

`python start.py`