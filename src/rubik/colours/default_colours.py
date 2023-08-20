#!/usr/bin/env python3
"""
Some basic colours and generators to use.
"""
from enum import Enum
import termcolor
from termcolor import colored
from common.logger import log
from common.cli import standard_parse


# class syntax
class Colours(Enum):
    red = 0
    yellow = 1
    blue = 2
    green = 3
    white = 4
    light_yellow = 5

    @classmethod
    def colour_to_term_colour(cls, desired_name):
        matching_colours = {}
        unmatched_colours = {}
        for colour in cls:
            name = colour.name
            if name in termcolor.COLORS.keys():
                matching_colours[name] = name
            else:
                unmatched_colours[name] = None
        unused_colours = [name for name in termcolor.COLORS.keys() if name not in matching_colours]
        for name in unmatched_colours.keys():
            matching_colours[name] = unmatched_colours[name] = unused_colours.pop()
        for name, colour in unmatched_colours.items():
            assert colour is not None, f"The colour {name} should have been matched."
            assert name in matching_colours.keys(), f"The colour {name} should be in our collection of matched colours."
            assert matching_colours[name] is not None, f"The colour {name} should designated."
        return matching_colours[desired_name]

    def colour(self, string, /, *args, background=False, **kwargs):
        assert isinstance(background, bool), f"Whether to colour the background or not must be a boolean value."
        term_colour = self.colour_to_term_colour(self.name)
        background_kwargs = {} if not background else {"on_color": f"on_{term_colour}"}
        return colored(string, color=term_colour, **background_kwargs)


if __name__ == "__main__":
    standard_parse(description=__doc__)
    for colour in Colours:
        log.print(f" {colour.colour('My colour is ' + colour.name)}, {colour.value = }")
        log.print(f" {colour.colour('My colour is ' + colour.name, background=True)}, {colour.value = }")
