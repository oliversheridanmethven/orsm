#!/usr/bin/env python3

from common.logger import log
from common.cli import setup_standard_parser
from itertools import product
from rubik.shapes import Volume, Domino, Square, Sheet, Cube
from common.variables import variable_names_and_objects

if __name__ == "__main__":

    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--single", help="Show single move combinations.", action="store_true")
    parser.add_argument("--double", help="Show double move combinations.", action="store_true")
    parser.add_argument("--shuffle", type=int, metavar="TURNS", help="Show some shuffles.")
    parser.add_argument("--shape", type=str, metavar="SHAPE", help="Which shape to demo.", default='Volume')
    kwargs = vars(parser.parse_args())

    for name, Shape in variable_names_and_objects(Volume, Domino, Square, Sheet, Cube):
        if name != kwargs["shape"]:
            continue
        shape = Shape()
        if kwargs["single"]:
            for move in shape.moves():
                log.info(f"Original: {shape = !s}")
                log.info(f"{move}: {shape.move(move) = !s}")
                # log.info(f"{move} (reversed): {shape.move(move, reverse=True)  = !s}\n\n")
        if kwargs["double"]:
            for move_1, move_2 in product(*[shape.moves() for i in range(2)]):
                log.info(f"Original: {shape  = !s}")
                moved = shape
                for step, move in enumerate([move_1, move_2]):
                    log.info(f"{step = } {move}")
                    moved = moved.move(move)
                    log.info(f"{moved  = !s}")
        turns = kwargs["shuffle"]
        if turns:
            shuffled, path = shape.shuffle(turns=turns)
            log.info(f"The target shuffled cube is: {shuffled}")
            log.info(f"Obtained by:")
            for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
                log.info(f"{turn = }: {move} {'in reverse' if reverse else ''}")

            moved = shape
            log.info(f"The starting configuration is: {moved}")
            for turn, (move, reverse) in enumerate(zip(path.moves, path.reverses)):
                log.info(f"{turn = }: {move} {'in reverse' if reverse else ''}")
                moved = moved.move(move, reverse=reverse)
                log.info(f"The moved configuration is: {moved}")
            log.info(f"The final moved configuration is: {moved}")
            log.info(f"The target configuration is: {shuffled}")
            assert moved == shuffled, f"We should have recovered our target configuration."
