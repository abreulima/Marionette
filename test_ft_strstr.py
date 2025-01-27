from extras import print_color
import ctypes

def run_strstr_tests(lib):
    test_cases = [
        ("Hello, world", "world", "world"),  # Basic case, found
        ("Hello, world", "Hello", "Hello"),  # Needle is at the beginning
        ("Hello, world", "world!", None),   # Needle is not found
        ("", "world", None),  # Empty haystack, needle can't be found
        ("Hello, world", "", "Hello, world"),  # Empty needle, should return the whole haystack
        ("abc", "d", None),  # Needle doesn't exist in haystack
        ("haystack", "stack", "stack"),  # Needle is at the end of the haystack
        ("ab", "ab", "ab"),  # Needle is the entire haystack
    ]
    
    # Set the return type for ft_strstr
    lib.ft_strstr.restype = ctypes.c_char_p
    
    for haystack, needle, expected in test_cases:
        # Call the `ft_strstr` function
        result = lib.ft_strstr(haystack.encode('utf-8'), needle.encode('utf-8'))
        
        if expected is None:
            # If expected is None, we expect the result to be NULL (None in Python)
            if result is not None:
                print_color(f"ERROR: ft_strstr('{haystack}', '{needle}') = {result.decode('utf-8')}, Expected None", "red")
            else:
                print_color(f"ft_strstr('{haystack}', '{needle}') = {result}, Expected: None", "green")
        else:
            # If expected is not None, we expect the result to be the substring found
            result_str = result.decode('utf-8') if result else None
            if result_str != expected:
                print_color(f"ERROR: ft_strstr('{haystack}', '{needle}') = {result_str}, Expected {expected}", "red")
            else:
                print_color(f"ft_strstr('{haystack}', '{needle}') = {result_str}, Expected: {expected}", "green")
