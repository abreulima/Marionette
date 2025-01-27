def print_color(message, color_code):
    """Prints message in the specified color.
    color_code: 'green' for success, 'red' for error
    """
    colors = {
        "green": "\033[92m",  # Green text
        "red": "\033[91m",  # Red text
        "reset": "\033[0m",  # Reset to default color
    }

    print(f"{colors[color_code]}{message}{colors['reset']}")
