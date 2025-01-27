from extras import print_color
import ctypes

def run_strcmp_tests(lib):


    lib.ft_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.ft_strcmp.restype = ctypes.c_int

    test_cases = [
        ("hello", "hello", 0),  # Strings are identical, expected result is 0
        ("apple", "banana", -1),  # "apple" < "banana", expected result is negative
        ("cat", "bat", 1),  # "cat" > "bat", expected result is positive
        ("123", "1234", -1),  # "123" < "1234", expected result is negative
        ("abcd", "abc", 1),  # "abcd" > "abc", expected result is positive
        ("", "", 0),  # Empty strings, expected result is 0
        ("a", "", 1),  # "a" > "", expected result is positive
        ("", "b", -1),  # "" < "b", expected result is negative
    ]

    for s1, s2, expected in test_cases:
        result = lib.ft_strcmp(s1.encode("utf-8"), s2.encode("utf-8"))
        if result != expected:
            print_color(f"ERROR: ft_strcmp('{s1}', '{s2}') = {result}, Expected {expected}", "red")
        else:
            print_color(f"ft_strcmp('{s1}', '{s2}') = {result}, Expected: {expected}", "green")
