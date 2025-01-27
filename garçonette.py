import os
import ctypes
import subprocess

from test_ft_strcmp import run_strcmp_tests
from test_ft_strncmp import run_strncmp_tests
from test_ft_strcat import run_strcat_tests
from test_ft_strncat import run_strncat_tests
from test_ft_strstr import run_strstr_tests
from test_ft_strlcat import run_strlcat_tests

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


files = [
    "ex00/ft_strcmp.c",
    "ex01/ft_strncmp.c",
    "ex02/ft_strcat.c",
    "ex03/ft_strncat.c",
    "ex04/ft_strstr.c",
    "ex05/ft_strlcat.c"]

for f in files:
    isFile = os.path.isfile(f)

    if isFile:
        ex = f.split("/")[1]
        print(f"Testing {ex}")

        out = "test.so"
        result = subprocess.run(
            ["gcc", "-shared", "-o", out, "-fPIC"] + [f for f in files if os.path.isfile(f) and f.endswith('.c')],            
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        if os.path.isfile(out):
            lib = ctypes.CDLL("./test.so", mode=ctypes.RTLD_GLOBAL)

            if ex == "ft_strcmp.c":
                run_strcmp_tests(lib)

            elif ex == "ft_strncmp.c":
                run_strncmp_tests(lib)

            elif ex == "ft_strcat.c":
                run_strcat_tests(lib)

            elif ex == "ft_strncat.c":
                run_strncat_tests(lib)

            elif ex == "ft_strstr.c":
                run_strstr_tests(lib)

            elif ex == "ft_strlcat.c":
                run_strlcat_tests(lib)


        else:
            print("Failed to create file")

        

