"""
Handling output.
"""

import py

class Supressor(object):
    """A class to suppress printing output."""
    def __init__(self, suppress_output=False):
        self.suppress_output = suppress_output

    def __enter__(self):
        if self.suppress_output:
            self.capture = py.io.StdCaptureFD()  # This seems to be the best way to capture, including for C extension modules.
        return self.capture

    def __exit__(self, *args):
        self.capture.reset()
