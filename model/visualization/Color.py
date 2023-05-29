import numpy as np
import colorsys

class Color():
    """
        A class for handling colors in RGB format.

        This class provides a list of predefined colors as well as methods for creating gradient color spectrums.

    """

    RED : tuple = (255, 0, 0)
    BLUE : tuple = (25, 133, 240)
    GREEN : tuple = (45, 225, 63)
    BLACK : tuple = (0, 0, 0)
    WHITE : tuple = (255, 255, 255)
    GRAY : tuple = (97, 93, 93)

    # Créer une liste contenant le dégradé de couleurs
    def gradient_rgb_spectrum(self, size) -> list:
        """
            Creates a list containing a gradient color spectrum.

            Args:
                size: The size of the spectrum.

            Returns:
                A list of RGB tuples representing the gradient color spectrum.

        """
        spectrum = []
        for i in range(size):
            hue = i / size
            red, green, blue = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
            spectrum.append((int(red*255), int(green*255), int(blue*255)))
        return spectrum

    # Affiche le dégradé dans la console
    def display_colors(self, colors):
        """
            Displays a list of colors in the console.

            Args:
                colors: A list of RGB tuples representing the colors to display.

        """
        for color in colors:
            print("\033[48;2;" + str(color[0]) + ";" + str(color[1]) + ";" + str(color[2]) + "m " + "  " + "\033[0m")