#!/usr/bin/env python3
import unittest


def act_on_shape(input_faces):
    faces = input_faces
    print(f"The original {faces = }")
    print(f"{type(faces) = }, {type(faces[0]) = }, {type(faces[0][0]) = }, {type(faces[0][0][0]) = }")
    faces2 = [[[0], [0]], [[1], [1]]]
    assert isinstance(faces, type(faces2))
    assert faces == faces2
    print(f"{faces = }")
    print(f"{faces2 = }")
    faces2[1][1][0], faces2[0][1][0] = faces2[0][1][0], faces2[1][1][0]
    faces[1][1][0], faces[0][1][0] = faces[0][1][0], faces[1][1][0]
    print("after swapping")
    print(f"{faces = }")
    print(f"{faces2 = }")
    assert faces == faces2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        class Shape:
            input_3 = [[[0], [0]], [[1], [1]]]

            def __init__(self):
                self.faces = []
                for value in [0, 1]:
                    self.faces.append([[value] for i in range(2)])
                self.input_4 = [[[0], [0]], [[1], [1]]]

        shape = Shape()
        self.input_1 = shape.faces
        self.input_2 = [[[0], [0]], [[1], [1]]]
        self.input_3 = Shape.input_3
        self.input_4 = [[[value] for i in range(2)] for value in [0, 1]]
        self.input_5 = [[[value]] * 2 for value in [0, 1]]

    def test_same_inputs(self):
        self.assertEqual(self.input_1, self.input_2)
        self.assertListEqual(self.input_1, self.input_2)

    def test_input1(self):
        act_on_shape(self.input_1)

    def test_input2(self):
        act_on_shape(self.input_2)

    def test_input3(self):
        act_on_shape(self.input_3)

    def test_input4(self):
        act_on_shape(self.input_4)

    def test_input5(self):
        act_on_shape(self.input_5)


if __name__ == '__main__':
    unittest.main()
