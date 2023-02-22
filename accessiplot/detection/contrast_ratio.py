from matplotlib.colors import to_rgb


def is_contrast_ratio_below_threshold(plt, contrast_ratio:float, threshold:float=2.5):
    """
    Pass in a contrast ratio and it will detect if it is below a limit.
    """
    #TODO: This needs a bit more love to detect what threshold to use automatically by context
    if contrast_ratio < threshold:
        return True
    else:
        return False


def calculate_contrast_ratios_from_plt(plt):
    """
    Generate a dictionary of contrast ratios from a plt object
    1) Get axes object from plot object
    2) Get color of all lines as rgb and append to list
    3) Get color of the background and append to list
    4) Do an n**2 comparison of colors in the above list and generate contrast ratios
    These are stored as key/value mappings where the key is 
    `<index_color1>_<index_color2>`.
    """
    axes_object = plt.gca()
    lines_colors = [to_rgb(line.get_color()) for line in axes_object.lines]
    lines_colors.append(to_rgb(axes_object.get_facecolor()))

    contrast_ratios_by_index = {}
    detections = {}

    for i in range(len(lines_colors)):
        for j in range(len(lines_colors)):
            contrast_ratios_by_index[f'{i}_{j}'] = \
                calculate_contrast_ratio(lines_colors[i], lines_colors[j])
    
    for key in contrast_ratios_by_index.keys():
        line1_ind_str, line2_ind_str = key.split("_")
        line1_ind, line2_ind = int(line1_ind_str), int(line2_ind_str)
        if line1_ind == line2_ind:
            continue # Don't do analysis on contrast ratio against itself.
        print("=" * 15)
        print(line1_ind, lines_colors[line1_ind])
        print(line2_ind, lines_colors[line2_ind])
        print(contrast_ratios_by_index[key])
        if is_contrast_ratio_below_threshold(plt, contrast_ratios_by_index[key]): #TODO: Need to do better handling of threshold based on plot
            detections[key] = contrast_ratios_by_index[key]


    return contrast_ratios_by_index, lines_colors, detections


def calculate_contrast_ratio(rgb1, rgb2):
    """
    Returns contrast ratio of two rgb values
    using the relative luminances.
    """

    l1 = calculate_relative_luminance(rgb1)
    l2 = calculate_relative_luminance(rgb2)

    if l1 > l2:
        return (l1 + 0.05) / (l2 + 0.05)
    else:
        return (l2 + 0.05) / (l1 + 0.05)


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
