from extras import print_color
import ctypes

def run_strcat_tests(lib):
    test_cases = [
        ("Hello, ", "World!", "Hello, World!"),  # Normal case
        ("", "Hello", "Hello"),  # Empty `dest`, non-empty `src`
        ("Hello", "", "Hello"),  # Non-empty `dest`, empty `src`
        ("", "", ""),  # Both empty
        ("abc", "def", "abcdef"),  # Concatenating non-empty strings
        ("foo", "barbaz", "foobarbaz"),  # Larger `src`
    ]
    
    # Set the return type for ft_strcat
    lib.ft_strcat.restype = ctypes.c_char_p
    
    for dest, src, expected in test_cases:
        # Ensure `dest` is large enough to hold the concatenation
        dest = ctypes.create_string_buffer(dest.encode('utf-8'))
        
        # Call the `ft_strcat` function
        result = lib.ft_strcat(dest, src.encode('utf-8'))
        
        # Check if the result is as expected
        result_str = result.decode('utf-8')  # Decode the byte string returned from C
        if result_str != expected:
            print_color(f"ERROR: ft_strcat('{dest.value.decode('utf-8')}', '{src}') = {result_str}, Expected {expected}", "red")
        else:
            print_color(f"ft_strcat('{dest.value.decode('utf-8')}', '{src}') = {result_str}, Expected: {expected}", "green")
