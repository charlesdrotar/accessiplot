import re
from matplotlib.colors import get_named_colors_mapping, to_rgb

COLOR_MAPPING_DICTIONARY = get_named_colors_mapping()

def calculate_contrast_ratio(rgb1, rgb2):
    """
    Returns contrast ratio of two rgb values
    """

    l1 = calculate_relative_luminance(rgb1)
    l2 = calculate_relative_luminance(rgb2)

    if l1 > l2:
        return (l1 + 0.05) / (l2 + 0.05)
    else:
        return (l2 + 0.05) / (l1 + 0.05)


def convert_string_color_to_rgb(color:str, alpha=None):
    """
    Returns rgb tuple from string color
    """
    
    if color not in COLOR_MAPPING_DICTIONARY.keys():
        raise KeyError("This color doesn't exist in the matplotlib color mappings!")

    color_value = COLOR_MAPPING_DICTIONARY[color]

    if isinstance(color_value, tuple):
        return color_value
    elif isinstance(color_value, str):
        return to_rgb(color_value)

def calculate_relative_luminance(rgb:tuple):
    """
    Returns relative luminance of an rgb value. 
    This is used in the calculation of contrast ratios.
    """

    r,g,b = rgb
    # Check to make sure the appropriate normalized rgb value is passed in.
    if (not 0.0 <= r <= 1.0) or (not 0.0 <= g <= 1.0) or (not 0.0 <= b <= 1.0):
        raise ValueError(f"The values of r:{r}, g:{g}, or b:{b} are not all within [0,1]!")

    r = normalize(r)
    g = normalize(g)
    b = normalize(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def normalize(val:float):
    """
    Normalize the R, G, or B value using the WCAG 2.0 formula defined
    here - https://www.w3.org/TR/WCAG20/#relativeluminancedef
    """
    if val <= 0.03928:
        return val / 12.92
    else:
        return ((val + 0.055) / 1.055) ** 2.4

    