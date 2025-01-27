from extras import print_color
import ctypes

def run_strlcat_tests(lib):
    test_cases = [
        ("Hello, ", "world!", 20, "Hello, world!", 13),  # Normal case, enough space
        ("Hello, ", "world!", 10, "Hello, wor", 13),   # Buffer too small, only part of src is added
        ("Hello", "world!", 5, "Hello", 11),           # Buffer too small to append any characters
        ("", "world!", 10, "world!", 7),               # Empty dest, fits entirely into dest
        ("Hello", "", 10, "Hello", 5),                 # Empty src, dest stays the same
        ("Hello, ", "world!", 15, "Hello, world!", 13),  # Exact buffer size to hold full string
        ("ab", "cd", 3, "abc", 5),                     # Small buffer, part of src added
        ("abc", "defgh", 6, "abcdef", 9),              # Just enough space to fit one more char
    ]
    
    # Set the return type for ft_strlcat
    lib.ft_strlcat.restype = ctypes.c_uint
    
    for dest, src, size, expected_result, expected_length in test_cases:
        # Ensure `dest` is large enough to hold the concatenation
        dest = ctypes.create_string_buffer(dest.encode('utf-8'), size)
        
        # Call the `ft_strlcat` function
        result = lib.ft_strlcat(dest, src.encode('utf-8'), size)
        
        # Check if the result is as expected
        result_str = dest.value.decode('utf-8')
        
        if result_str != expected_result or result != expected_length:
            print_color(f"ERROR: ft_strlcat('{dest.value.decode('utf-8')}', '{src}', {size}) = '{result_str}', {result}, Expected: '{expected_result}', {expected_length}", "red")
        else:
            print_color(f"ft_strlcat('{dest.value.decode('utf-8')}', '{src}', {size}) = '{result_str}', {result}, Expected: '{expected_result}', {expected_length}", "green")
