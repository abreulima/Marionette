from extras import print_color
import ctypes

def run_strncmp_tests(lib):

    lib.ft_strncmp.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint]
    lib.ft_strncmp.restype = ctypes.c_int

    test_cases = [
        # (input_string1, input_string2, n, expected_result)
        ("hello", "hello", 5, 0),  # Strings are identical, compare up to 5 characters
        ("apple", "banana", 5, -1),  # "apple" < "banana", compare up to 5 characters
        ("cat", "bat", 3, 1),  # "cat" > "bat", compare up to 3 characters
        ("123", "1234", 3, 0),  # "123" == "123", compare up to 3 characters
        ("abcd", "abc", 4, 1),  # "abcd" > "abc", compare up to 4 characters
        ("", "", 0, 0),  # Both are empty, compare up to 0 characters
        ("a", "", 1, 1),  # "a" > "", compare 1 character
        ("", "b", 1, -1),  # "" < "b", compare 1 character
        ("hello", "hell", 4, 0),  # "hello" == "hell" when comparing 4 characters
        ("hello", "hell", 5, 1),  # "hello" > "hell", compare 5 characters (extra 'o' in "hello")
    ]

    for s1, s2, n, expected in test_cases:
        result = lib.ft_strncmp(s1.encode("utf-8"), s2.encode("utf-8"), n)

        if result != expected:
            print_color(f"ERROR: ft_strncmp('{s1}', '{s2}', {n}) = {result}, Expected {expected}", "red")
        else:
            print_color(f"ft_strncmp('{s1}', '{s2}', {n}) = {result}, Expected: {expected}", "green")
