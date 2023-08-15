#!/usr/bin/env python3
import logging
import unittest
from rubik.shapes import shape as Shape
from rubik.colours.default_colours import Colours
from common.variables import variable_names_and_objects
import itertools
from common.cli import log, unit_test_parse
from common.arguments import all_combinations


class BasicProperties(unittest.TestCase):

    def setUp(self):
        self.kwargs = {"N": 3, "M": 4}
        self.args = []
        self.names_and_shapes_classes = variable_names_and_objects(Shape.Tile,
                                                                   Shape.Domino,
                                                                   Shape.Strip,
                                                                   Shape.Square,
                                                                   Shape.Grid,
                                                                   Shape.Sheet,
                                                                   Shape.Volume,
                                                                   Shape.Cube,
                                                                   Shape.Triangle,
                                                                   Shape.Tetrahedron,
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
            ids = list(traverse_rows(shape.faces, id))
            self.assertEqual(len(ids), len(set(ids)), f"There are duplicate memory locations used to store the tiles in {name}. Not suitable for swapping operations.")


class Moves(unittest.TestCase):

    def test_single_moves_domino(self):
        shape = Shape.Domino()
        for move in shape.moves():
            shape_moved = shape.move(move)
            self.assertEqual(shape, shape.solved_config())
            self.assertNotEqual(shape_moved, shape)
            self.assertNotEqual(shape_moved, shape.solved_config())
            shape_reverted = shape_moved.move(move, reverse=True)
            self.assertEqual(shape_reverted, shape.solved_config())
            self.assertEqual(shape_reverted, shape)

    def test_double_moves_domino(self):
        shape = Shape.Domino()
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
        shape = Shape.Volume()
        for id_1, move_1 in enumerate(shape.moves()):
            for id_2, move_2 in enumerate(shape.moves()):
                if id_1 == id_2:
                    self.assertEqual(move_1, move_2)
                else:
                    self.assertNotEqual(move_1, move_2)

    def test_double_moves_volume(self):
        shape = Shape.Volume()
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
        shape = Shape.Volume()
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
            shape = Shape.Volume()
            shuffled, path = shape.shuffle(turns=turns)
            log.info(f"The target shuffled cube is: {shuffled}")
            log.debug(f"Obtained by:")
            for turn, (move, reverse) in enumerate(zip(path['moves'], path['reverses'])):
                log.debug(f"{turn = }: {move} {'in reverse' if reverse else ''}")
            moved = shape
            log.info(f"The starting configuration is: {moved}")
            for turn, (move, reverse) in enumerate(zip(path["moves"], path["reverses"])):
                log.debug(f"{turn = }: {move} {'in reverse' if reverse else ''}")
                moved = moved.move(move, reverse=reverse)
                log.debug(f"The moved configuration is: {moved}")
            log.info(f"The final moved configuration is: {moved}")
            log.info(f"The target configuration is: {shuffled}")
            self.assertEqual(moved, shuffled, f"We should have recovered our target configuration.")

    def test_moves_give_new_objects(self):
        shape = Shape.Volume()
        for moves in all_combinations(shape.moves()):
            for reverse in [True, False]:
                self.assertIsNot(shape, shape.move(*moves, reverse=reverse))

    def test_shuffles_give_new_objects(self):
        shape = Shape.Volume()
        for turns in range(5):
            self.assertIsNot(shape, shape.shuffle(turns))


if __name__ == '__main__':
    unit_test_parse()
    unittest.main()
