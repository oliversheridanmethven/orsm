#!/usr/bin/env python3
import logging
import unittest

import numpy as np
from numpy import testing

from rubik import shapes
from rubik.colours.default_colours import Colours
from common.variables import variable_names_and_objects
import itertools
from common.cli import log, unit_test_parse
from common.arguments import all_combinations


class BasicProperties(unittest.TestCase):

    def setUp(self):
        self.kwargs = {"N": 3, "M": 4}
        self.args = []
        self.names_and_shapes_classes = variable_names_and_objects(shapes.Tile,
                                                                   shapes.Domino,
                                                                   shapes.Strip,
                                                                   shapes.Square,
                                                                   shapes.Grid,
                                                                   shapes.Sheet,
                                                                   shapes.Volume,
                                                                   shapes.Cube,
                                                                   shapes.Triangle,
                                                                   shapes.Tetrahedron,
                                                                   )

    def test_printing(self):
        """Should print a nicely coloured shape."""
        for name, shape_class in self.names_and_shapes_classes:
            log.debug(f"\nTrying to print a {name}")
            shape = shape_class(*self.args, **self.kwargs)
            log.debug(f"{shape!r}")
            log.debug(f"{shape}")
            log.debug(f"{shape = }")
            log.debug(f"The solved configuration is: {shape.solved_config(*self.args, **self.kwargs)}, and should look like {shape.clean_config(*self.args, **self.kwargs)}")
            self.assertEqual(shape, shape.clean_config(*self.args, **self.kwargs), "Shapes must always start in a clean configuration.")

    def test_unique_row_containers(self):
        """
        Some operations will be swapping rows and columns,
        and when we swap rows, we need to ensure the
        containers are different, and we don't have
        two duplicate rows where swapping elements in
        one would inadvertently affect the contents of the
        other. Hence we need each container to be unique.
        """

        def traverse_rows(faces, function):
            """Traverse the rows."""
            for face in faces:
                for row in face:
                    yield function(row)

        for name, shape_class in self.names_and_shapes_classes:
            shape = shape_class(*self.args, **self.kwargs)
            ids = list(traverse_rows(shape._faces, id))
            self.assertEqual(len(ids), len(set(ids)), f"There are duplicate memory locations used to store the tiles in {name}. Not suitable for swapping operations.")


class Moves(unittest.TestCase):

    def test_single_moves_domino(self):
        shape = shapes.Domino()
        for move in shape.moves():
            shape_moved = shape.move(move)
            self.assertEqual(shape, shape.solved_config())
            self.assertNotEqual(shape_moved, shape)
            self.assertNotEqual(shape_moved, shape.solved_config())
            shape_reverted = shape_moved.move(move, reverse=True)
            self.assertEqual(shape_reverted, shape.solved_config())
            self.assertEqual(shape_reverted, shape)

    def test_single_moves_sheet(self):
        shape = shapes.Sheet()
        for move in shape.moves():
            shape_moved = shape.move(move)
            self.assertEqual(shape, shape.solved_config())
            self.assertNotEqual(shape_moved, shape)
            self.assertNotEqual(shape_moved, shape.solved_config())
            shape_reverted = shape_moved.move(move, reverse=True)
            self.assertEqual(shape_reverted, shape.solved_config())
            self.assertEqual(shape_reverted, shape)

    def test_double_moves_domino(self):
        shape = shapes.Domino()
        for move_1, move_2 in itertools.product(*[shape.moves() for i in range(2)]):
            shape_moved_once = shape.move(move_1)
            shape_moved_twice = shape_moved_once.move(move_2)
            log.debug(f"original = {shape} moved_once = {shape_moved_once} moved_twice = {shape_moved_twice}")
            self.assertEqual(shape_moved_twice, shape.solved_config())
            self.assertNotEqual(shape_moved_twice, shape_moved_once)
            shape_moved_twice_reverted = shape_moved_twice.move(move_2, reverse=True)
            self.assertEqual(shape_moved_twice_reverted, shape_moved_once)
            shape_reverted_in_order = shape_moved_twice.move(move_2, move_1, reverse=True)
            self.assertEqual(shape_reverted_in_order, shape)
            shape_reverted_out_of_order = shape_moved_twice.move(move_1, move_2, reverse=True)
            self.assertEqual(shape_reverted_out_of_order, shape)

    def test_same_moves_compare_equal(self):
        shape = shapes.Volume()
        for id_1, move_1 in enumerate(shape.moves()):
            for id_2, move_2 in enumerate(shape.moves()):
                if id_1 == id_2:
                    self.assertEqual(move_1, move_2)
                else:
                    self.assertNotEqual(move_1, move_2)

    def test_double_moves_volume(self):
        shape = shapes.Volume()
        for direction in [True, False]:
            other_direction = not direction
            for move_1, move_2 in itertools.product(*[shape.moves() for i in range(2)]):
                shape_moved_once = shape.move(move_1, reverse=direction)
                shape_moved_twice = shape_moved_once.move(move_2, reverse=direction)
                self.assertNotEqual(shape_moved_twice, shape.solved_config())
                self.assertNotEqual(shape_moved_twice, shape_moved_once)
                shape_moved_twice_reverted = shape_moved_twice.move(move_2, reverse=other_direction)
                self.assertEqual(shape_moved_twice_reverted, shape_moved_once)
                shape_reverted_in_order = shape_moved_twice.move(move_2, move_1, reverse=other_direction)
                self.assertEqual(shape_reverted_in_order, shape)
                shape_reverted_out_of_order = shape_moved_twice.move(move_1, move_2, reverse=other_direction)
                if move_1 == move_2:
                    self.assertEqual(shape_reverted_out_of_order, shape)
                else:
                    self.assertNotEqual(shape_reverted_out_of_order, shape)

    def test_rotational_symmetry(self):
        shape = shapes.Volume()
        for direction in [True, False]:
            other_direction = not direction
            for move in shape.moves():
                # The two-fold symmetry
                moved = shape.move(move, move, reverse=direction)
                moved_reverse = shape.move(move, move, reverse=other_direction)
                self.assertEqual(moved, moved_reverse)
                # The four-fold symmetry
                moved_fully = shape.move(move, move, move, move, reverse=direction)
                self.assertEqual(shape, moved_fully)

    def test_shuffle(self):
        for turns in range(10):
            shape = shapes.Volume()
            shuffled, path = shape.shuffle(turns=turns)
            log.info(f"The target shuffled cube is: {shuffled}")
            log.debug(f"Obtained by:")
            for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
                log.debug(f"{turn = }: {move} {'in reverse' if reverse else ''}")
            moved = shape
            log.info(f"The starting configuration is: {moved}")
            for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
                log.debug(f"{turn = }: {move} {'in reverse' if reverse else ''}")
                moved = moved.move(move, reverse=reverse)
                log.debug(f"The moved configuration is: {moved}")
            log.info(f"The final moved configuration is: {moved}")
            log.info(f"The target configuration is: {shuffled}")
            self.assertEqual(moved, shuffled, f"We should have recovered our target configuration.")
            reverted = moved
            for turn, (move, reverse) in reversed(list(enumerate(zip(path.moves, path.reverses)))):
                other_direction = not reverse
                log.debug(f"{turn = }: {move} {'in reverse' if other_direction else ''}")
                reverted = reverted.move(move, reverse=other_direction)
            self.assertEqual(reverted, shape)

    def test_moves_give_new_objects(self):
        shape = shapes.Volume()
        for moves in all_combinations(shape.moves()):
            for reverse in [True, False]:
                self.assertIsNot(shape, shape.move(*moves, reverse=reverse))

    def test_shuffles_give_new_objects(self):
        shape = shapes.Volume()
        for turns in range(5):
            self.assertIsNot(shape, shape.shuffle(turns))

    def test_shuffle_seeding(self):
        shape_1 = shapes.Volume()
        shape_2 = shapes.Volume()
        for seed in [False, 0]:
            while True:
                shuffle_1, path_1 = shape_1.shuffle(seed=seed)
                shuffle_2, path_2 = shape_2.shuffle(seed=seed)
                if shuffle_1 != shape_1 and shuffle_2 != shape_2:
                    break
            if seed or (isinstance(seed, int) and type(seed) != bool):
                self.assertEqual(path_1, path_2)
                self.assertEqual(shuffle_1, shuffle_2)
            else:
                self.assertNotEqual(path_1, path_2)


class Casting(unittest.TestCase):

    def test_array_casting(self):
        shape = shapes.Volume()
        faces_array = shape.to_array()
        self.assertIsInstance(faces_array, np.ndarray)
        self.assertEqual(len(faces_array.shape), 1, f"Our array must be one dimensional.")
        self.assertGreaterEqual(faces_array.size, 1, f"Our array must contain some elements.")
        shape_recovered = shape.from_array(array=faces_array)
        self.assertIsNot(shape_recovered, shape, f"These should be separate objects.")
        self.assertEqual(shape_recovered, shape, f"The shape recovered from the array conversion should match the original.")
        testing.assert_array_equal(faces_array, shape.to_array())
        faces_array[0] += 1
        with testing.assert_raises(AssertionError):
            testing.assert_array_equal(faces_array, shape.to_array(), f"Modifying the return should not change the original.")


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()
