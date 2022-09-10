from styles import Styles

from ascii_magic import from_image_file, init_terminal

from os import getlogin

class PyCLogo:
    """PyCLogo - Simple but powerful re-make of neofetch, that allows you to create similar neofetch windows."""

    PY_C_LOGO_VERSION = 1.

    image = None
    info = {}

    def add_info(self, key: str, val: str) -> None:
        """Add info to window."""
        self.info[key] = val

    def update_image(self, new_image: str) -> None:
        """Update image on window."""
        self.image = new_image

    def print_window(self, _keys_color: str):
        """Print window. Prints image & info."""
        if self.image is None:
            raise RuntimeError("Image is None. Specify it via `update_image`.")

        keys_color = None

        try:
            keys_color = eval(f'Styles.{_keys_color.upper()}')
        except Exception:
            raise RuntimeError("Error due setuping keys color. Possible it's unknown color.")

        username = getlogin().split('\\')[-1]

        _ascii_image = from_image_file(self.image, columns=45)

        init_terminal()

        ascii_image = None

        ascii_image_lines = _ascii_image.split('\n')

        ascii_image_lines[1] += f" {Styles.BOLD}{keys_color}@{username}{Styles.END}"

        ascii_image_line_pos = 3

        for key in self.info.keys():
            ascii_image_lines[ascii_image_line_pos] += f" {Styles.BOLD}{keys_color}{key}{Styles.END} - {Styles.BOLD}{self.info[key]}{Styles.END}"

            ascii_image_line_pos += 1

        ascii_image = '\n'.join(ascii_image_lines)

        print(ascii_image)
