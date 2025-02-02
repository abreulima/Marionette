from extras import print_color
import ctypes

def run_strcmp_tests(lib):


    lib.ft_strcmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    lib.ft_strcmp.restype = ctypes.c_int

    test_cases = [
        ("hello", "hello", 0),  # Strings are identical
        ("apple", "banana", -1),  # "apple" < "banana"
        ("cat", "bat", 1),  # "cat" > "bat"
        ("123", "1234", -1),  # "123" < "1234"
        ("abcd", "abc", 100),  # "abcd" > "abc"
        ("", "", 0),  # Empty strings
        ("a", "", 97),  # "a" > ""
        ("", "b", -98),  # "" < "b"
    ]

    for s1, s2, expected in test_cases:
        result = lib.ft_strcmp(s1.encode("utf-8"), s2.encode("utf-8"))
        if result != expected:
            print_color(f"ERROR: ft_strcmp('{s1}', '{s2}') = {result}, Expected {expected}", "red")
        else:
            print_color(f"ft_strcmp('{s1}', '{s2}') = {result}, Expected: {expected}", "green")
