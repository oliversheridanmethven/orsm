#!/usr/bin/env python3
"""
A small curses window to display images and ascii videos.

Because this is a curses application, any output and logs will
be written to files rather than shown to the screen.
"""

from media.images import ImageParser
from media.images import add_parser_optional_arguments as add_image_parser_arguments
from cv2 import VideoCapture
from time import sleep
import datetime as dt
from common.logger import log, redirect_logging_to_file, suppress_console_output, set_logging_level
import curses
from textwrap import dedent
from common.cli import setup_standard_parser


def ascii_from_camera(*args, camera, retries=0, **kwargs):
    """
    Produces an ASCII image from camera.
    """
    remaining_attempts = retries + 1
    successful = False
    attempt = 0
    while not successful:
        attempt += 1
        if not remaining_attempts:
            raise RuntimeError(f"We have failed to read from the camera too many times ({retries = }).")
        successful, image_array = camera.read()
        if not successful:
            log.warning(f"We have failed to read from the camera on {attempt = }")
        remaining_attempts -= 1
    parser = ImageParser(image=image_array)
    parser.resize(*args, **kwargs)
    return parser.as_ascii(*args, **kwargs)


def stream_from_camera(*args, camera, timeout=None, **kwargs):
    """
    Generate a stream of ASCII images from the webcam.
    """
    if not camera:
        error_message = f"Unable to capture the video from the webcam."
        log.warning(error_message)
        raise RuntimeError(error_message)
    sleep(0.1)  # The webcam take a small time interval to warm up, else it returns black images.
    try:
        start = dt.datetime.now()
        while (timeout is None or dt.datetime.now() - start < dt.timedelta(seconds=timeout)):
            ascii_string = ascii_from_camera(*args, camera=camera, **kwargs)
            yield ascii_string
    except RuntimeError as e:
        log.warning(f"{str(e)}")
        raise e
    except Exception as e:
        log.warning(f"An unexpected error has occurred: {str(e)}")
        raise e
    finally:
        camera.release()


def curses_main(stdscr, *args, abs_width=None, border=None, **kwargs):
    curses.start_color()

    stdscr.addstr(0, 0, dedent(
        """\
        Press the < SPACE > key to start streaming from the webcam.
        
        Press the < CTRL + C > to exit the program.
        """))
    warning_start = curses.LINES - 5
    warning_end = curses.LINES - 1

    def display_warning(user_warning):
        log.warning(user_warning)
        stdscr.addstr(warning_start, 0, f"{user_warning}\n", curses.A_REVERSE)

    webcam_start = stdscr.getyx()[0] + 1
    border_padding = len(border)
    webcam_end = warning_start - 2 * border_padding
    max_lines = webcam_end - webcam_start - 2 * border_padding
    max_width = stdscr.getmaxyx()[1] - 2 * border_padding
    if abs_width is None:
        abs_width = max_width
    if border is not None:
        abs_width -= 2 * border_padding
    if 0 < abs_width <= max_width:
        message = f"The desired image width {abs_width} is invalid. ({max_width = })."
        log.debug(message)

    default_camera_index = 0
    camera = VideoCapture(default_camera_index)
    webcam_streamer = stream_from_camera(*args, camera=camera, abs_width=abs_width, border=border, **kwargs)
    test_ascii_fits = True
    while True:
        user_char = stdscr.get_wch()
        if user_char == " ":
            log.info("The user is starting the webcam.")
            for ascii_image in webcam_streamer:
                if test_ascii_fits:
                    lines = len(ascii_image.split("\n"))
                    line = ascii_image.split("\n")[0]
                    log.debug(f"The number of lines in our image is: {lines} and our {max_lines = }")
                    log.debug(f"The number of columns in our image is: {len(line)} and our {max_width = }")
                    user_warning = ""
                    if lines > max_lines:
                        user_warning = f"The image is too tall for the window. The image contains {lines = } but can only fit {max_lines = }. Consider using a taller or thinner window."
                        display_warning(user_warning)
                    elif len(line) > max_width:
                        user_warning = f"The image is too wide for the window. The image contains {len(line) = } but can only fit {max_width = }. Consider using a shorter or fatter window."
                        display_warning(user_warning)

                    if user_warning:
                        stdscr.addstr(*stdscr.getyx(), f"Press any key to continue and we will exit the program.")
                        stdscr.get_wch()
                        raise RuntimeError(user_warning)

                    test_ascii_fits = False
                stdscr.addstr(webcam_start, 0, ascii_image)
                stdscr.refresh()
        else:
            display_warning(f"Warning: The user provided an unknown key pattern character {user_char = }.")
            stdscr.addstr(*stdscr.getyx(), f"Please try again.")
            continue
        for line in range(warning_start, warning_end):
            stdscr.move(line, 0)
            stdscr.clrtoeol()
    return 0


def main():
    parser = setup_standard_parser(description=__doc__)
    parser.add_argument("--timeout", type=int, metavar="SECONDS", help="Whether to timeout streaming from the webcam")
    add_image_parser_arguments(parser=parser)
    kwargs = vars(parser.parse_args())
    set_logging_level(level=log.TRACE)
    redirect_logging_to_file()
    suppress_console_output()
    return curses.wrapper(curses_main, **kwargs)


if __name__ == "__main__":
    main()
