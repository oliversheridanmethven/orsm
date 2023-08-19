# Rubik

Here we collect together some code which solves Rubik style
puzzles. 

## Solving the 2x2 Rubik Cube

For the 2x2 Rubik cube (which we call a "`Volume`"), we can
usually solve this in about 1-2 seconds, (it also depends how many
checks and assertions our code has in its hot path):
```
(venv) oliver testing $ multitime -n 50  src/rubik/solvers/demo.py --meet_in_middle 
===> multitime results                                                                                                                                                                              
1: src/rubik/solvers/demo.py --meet_in_middle
            Mean                Std.Dev.    Min         Median      Max
real        1.253+/-0.3383      0.929       0.222       0.713       3.965  
```