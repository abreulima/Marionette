from extras import print_color
import ctypes

def run_strncat_tests(lib):
    test_cases = [
        ("Hello, ", "World!", 3, "Hello, Wor"),  # Normal case with limit
        ("", "Hello", 3, "Hel"),  # Empty `dest`, limit 3
        ("Hello", "", 3, "Hello"),  # Empty `src`, limit 3
        ("", "", 3, ""),  # Both empty, limit 3
        ("abc", "def", 4, "abcdef"),  # Limit exceeds `src` length
        ("foo", "barbaz", 2, "fooba"),  # Limit smaller than `src`
        ("abcdef", "ghi", 0, "abcdef"),  # Limit 0, `dest` should stay the same
    ]
    
    # Set the return type for ft_strncat
    lib.ft_strncat.restype = ctypes.c_char_p
    
    for dest, src, nb, expected in test_cases:
        # Ensure `dest` is large enough to hold the concatenation
        dest = ctypes.create_string_buffer(dest.encode('utf-8'))
        
        # Call the `ft_strncat` function
        result = lib.ft_strncat(dest, src.encode('utf-8'), nb)
        
        # Decode the result from the C function
        result_str = result.decode('utf-8')
        
        # Check if the result is as expected
        if result_str != expected:
            print_color(f"ERROR: ft_strncat('{dest.value.decode('utf-8')}', '{src}', {nb}) = {result_str}, Expected {expected}", "red")
        else:
            print_color(f"ft_strncat('{dest.value.decode('utf-8')}', '{src}', {nb}) = {result_str}, Expected: {expected}", "green")
