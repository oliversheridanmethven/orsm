# Rubik

Here we collect together some code which solves Rubik style
puzzles. 

## Turning conventions

### Invariants

#### Faces and underlying arrays

We generally allow two methods for describing arrays.

1. **Faces:**
    For a better user experience we have the faces syntax, 
    where for a given face on our shape, we split this up into
    rows and columns, where these are stored in nested lists.
    These can be accessed via the syntax:
    ```python
    shape[face][row][column] = <tile_value>
    ```
    We keep this for a kinder user experience when printing objects,
    debugging, and as a slight artifact of the first implementations.

2. **Arrays:**
    The various nested lists that form the faces description can be flattened
    to a single contiguous array of the tile values. This array 
    representation is used internally to store the tile values, and
    perform the various moves which permute the tiles. 

!!! note "Only the arrays are guaranteed to be correct"
    When we perform the various permuting moves, we only
    shuffle the values stored in the underlying array. We do not 
    touch the values in the nest list faces variable. This is for
    performance reasons. Only when we go to do a few operations
    (such as printing) will we update and correct the faces variable.
    Otherwise consider these to be "outdated" unless you explicitly 
    request for them to be updated. 

#### Invariant pieces

By construction, we define all our moves from the frame of reference
of the piece whose tile is at the `[0][0][0]` faces position. This 
means that none of the moves are allowed to move this piece.  

### Reversibility

All the moves must be reversible. The reverse of one move can
(and almost surely will be) on of the other possible moves.

> If we were to allow moves which are not trivially reversible, then
> this would at least require that the "reverse" of one move must
> be able to be mapped to another one of the moves. (In fact, for
> performance this might be the best implementation as it avoids
> conditional code execution, at the expense of holding one tiny array
> in memory).

### Counting quarter turns and half turns

Considering the standard Rubik cube, there is a counting issue
about whether to allow a half rotation as a single move, or two count
it as two quarter rotations. 

For our purposes, we consider it a separate move. This generally
means that when we iterate through what possible configurations
can be achieved, our search space grows quicker, but should
generally require fewer iterations. The benefit of fewer iterations
is that the frequency with which we collide with previously 
encountered configurations should be less. 

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