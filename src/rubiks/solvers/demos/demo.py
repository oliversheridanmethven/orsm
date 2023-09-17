#!/usr/bin/env python3
from common.cli import setup_standard_parser
from rubiks.shapes import Volume
from common.profiling import profiler
from rubiks import solvers

if __name__ == "__main__":

    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--brute_force", help="Demo the brute force solver.", action="store_true")
    parser.add_argument("--meet_in_middle", help="Demo the meet in the middle solver.", action="store_true")
    parser.add_argument("--meet_in_middle_recursive", help="Demo the meet in the middle solver (recursive).", action="store_true")
    parser.add_argument("--shuffle", type=int, metavar="TURNS", help="The amount of turns to do.", default=10)
    parser.add_argument("--seed", type=int, metavar="INT", help="Seed the randomness.")
    parser.add_argument("--profile", help="Enable profiling.", action="store_true")
    kwargs = vars(parser.parse_args())
    if kwargs["profile"]:
        profiler.enable_by_count()
    shape = Volume()
    shuffled, shuffle_path = shape.shuffle(turns=kwargs["shuffle"], seed=kwargs["seed"])
    if kwargs["brute_force"]:
        solution_path = solvers.BruteForce().solve(start=shape, target=shuffled)
    if kwargs["meet_in_middle"]:
        solution_path = solvers.MeetInMiddle().solve(start=shape, target=shuffled)
    if kwargs["meet_in_middle_recursive"]:
        solution_path = solvers.MeetInMiddleRecursive().solve(start=shape, target=shuffled)
    if kwargs["profile"]:
        profiler.print_stats()
