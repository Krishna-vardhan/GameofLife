# GameofLife
Game of Life - Python Implementation

This project implements Conway's Game of Life in Python. It is a zero-player game that simulates cellular automaton evolution based on simple rules. The game evolves over generations on a 20x20 grid, with each cell either alive (*) or dead ( ). You can choose one of the predefined patterns to begin and watch it evolve over time.

Features:

20x20 board for simulation

Three built-in initial patterns to choose from

Implements Conway's Game of Life rules:

  Underpopulation: Live cell with fewer than 2 live neighbors dies
  
  Survival: Live cell with 2 or 3 live neighbors lives
  
  Overpopulation: Live cell with more than 3 live neighbors dies
  
  Reproduction: Dead cell with exactly 3 live neighbors becomes alive
  
Toroidal (wrap-around) grid boundary

Text-based visualization of live (*) and dead ( ) cells

Interactive game loop that continues until the user decides to stop
