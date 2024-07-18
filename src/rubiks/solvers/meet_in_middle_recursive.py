#!/usr/bin/env python3

from rubiks.paths.path import Path
from rubiks.solvers.solver import Solver, check_solver_inputs, next_generation_of_shapes_without_paths
from common.logger import log
from common.variables import variable_names_and_objects


class MeetInMiddleRecursive(Solver):
    """
    A "meet in the middle" solver using a recursive structure.

    The recursive structure means we only need to store the shapes encountered,
    and not the paths' histories used to generate them. This means we will have to
    do a little bit more work when we connect the intermediate shapes to reconstruct
    the path, but has the benefit of much less storage, and allowing us
    to store the shapes in a wider variety of containers (sets have fast lookups, vectors
    are contiguous, we can sort and pre-allocate, etc.) and see which is optimal.
    """

    def _intermediate_shape_and_turns(self, *args, start, target, **kwargs):
        """
        Finds an intermediate shape inbetween the start and target shapes, returning
        how many turns it takes to reach from the respective shapes.
        """
        turns = 0
        shape_fronts = [set([endpoint]) for endpoint in [target, start]]
        while True:
            shape_front_1, shape_front_2 = shape_fronts
            if (overlaps := shape_front_1 & shape_front_2):
                log.trace(f"We have found {len(overlaps)} solutions with {turns = }.")
                break
            shape_fronts = shape_fronts[::-1]
            shape_fronts[0] = next_generation_of_shapes_without_paths(shape_fronts[0])
            turns += 1

        turns_from_start = (turns + 1) // 2
        turns_from_target = turns // 2
        assert turns_from_start >= turns_from_target, f"We expect equal or more turns from the starting shape than from the target."
        for name, turn_amount in variable_names_and_objects(turns_from_start, turns_from_target):
            assert turn_amount >= 0, f"The {name} must be positive, not {turn_amount = }"
        assert turns_from_start + turns_from_target == turns, f"We have not correctly split the turns: {turns = }, {turns_from_start = }, {turns_from_target = }"
        overlap = overlaps.pop()
        log.trace(f"The item that overlaps from both sets is {overlap = !s}")
        return overlap, turns_from_start, turns_from_target

    @check_solver_inputs
    def solve(self, *args, start, target, **kwargs):
        """
        Solves by a recursive meet in the middle.

        Initially:
            [start, target]
        Find an intermediate point.
            [start --- K moves ---> intermediate --- K' moves ---> target]
        Then for each interval repeat this until there is a chain of intermediate targets
        only one away from each other, forming a chain from the start to the end.
            [start --- 1 move ---> intermediate_N --- 1 move ---> intermediate_M ...  intermediate_K --- 1 move ---> target]
        Then form the solution by quickly finding the connecting route.
        """

        shapes = [start, target]
        distances = [None]

        def _distance_not_final(distance):
            """Final distances are 1 or zero and None if they're unknown."""
            assert distance is None or isinstance(distance, int), f"The distance is the wrong type, {distance = } {type(distance)}."
            if distance is not None:
                assert distance >= 0, f"Distances can't be negative, {distance = }."
            return distance is None or distance > 1

        while any([_distance_not_final(distance) for distance in distances]):
            index_start = next(i for i, distance in enumerate(distances) if _distance_not_final(distance))
            index_intermediate = index_start + 1
            intermediate_shape, distance_start, distance_target = self._intermediate_shape_and_turns(start=shapes[index_start], target=shapes[index_intermediate])
            distances[index_start] = distance_start
            distances.insert(index_intermediate, distance_target)
            shapes.insert(index_intermediate, intermediate_shape)

        assert len(distances), f"We expect there to be some distances."
        assert all([distance in [0, 1] for distance in distances]), f"All the distances must be one, not {distances = }."
        assert len(shapes) > 2, f"We are expecting some intermediate shapes."
        assert len(shapes) == len(distances) + 1

        # Now we clean up the distances and shapes, removing zero distance steps.
        # We remove redundant entries from the target towards the start, hence we
        # reverse the containers to "right/end-align" the indices.
        shapes = shapes[::-1]
        distances = distances[::-1]
        shapes = [shapes[i] for i, distance in enumerate(distances) if distance] + shapes[-1:]
        distances = [distance for distance in distances if distance]
        shapes = shapes[::-1]
        distances = distances[::-1]

        if distances:
            assert all([distance == 1 for distance in distances]), f"All the distances must be one, not {distances = }."
        assert shapes, f"We are expecting some shapes."
        assert len(shapes) == len(set(shapes)), f"All our intermediate shapes must be unique."
        assert len(shapes) == len(distances) + 1, f"There is a mismatch between our shapes and our distances."

        # Now we reconstruct the path.
        path = Path(start)
        for shape, next_shape in zip(shapes[:-1], shapes[1:]):
            for move in shape.moves():
                moved = shape.move(move)
                if moved == next_shape:
                    path = path.add(move=move, reverse=False)
                    break
            else:
                assert False, f"We should have found the {next_shape = } when searching through the moves generated from {shape = }."
        log.debug(f"The solution path we found was: {path = !s}")
        return path


if __name__ == "__main__":
    pass
