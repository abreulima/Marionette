from extras import print_color
import ctypes

def run_strlcat_tests(lib):
    test_cases = [
        ("Born to code", "1337 42", 20, "1337 42Born to code", 19),
        ("", "", 10, "", 0),
        ("hello", "", 10, "hello", 5),          
        ("", "world!", 10, "world!", 6),               
        ("Test", "Test", 10, "TestTest", 8),  
        ("Born to code", "1337 42", 7, "Born to code", 14),                
    ]
    
    # Set the return type for ft_strlcat
    lib.ft_strlcat.restype = ctypes.c_uint
    
    for dest, src, size, expected_result, expected_length in test_cases:
        # Ensure the destination string doesn't exceed the buffer size
        dest_encoded = dest.encode('utf-8')
        if len(dest_encoded) > size:
            dest_encoded = dest_encoded[:size]
        
        # Create the string buffer with a size that can hold the encoded string
        dest_buffer = ctypes.create_string_buffer(dest_encoded, size)
        
        # Call the `ft_strlcat` function
        result = lib.ft_strlcat(dest_buffer, src.encode('utf-8'), size)
        
        # Check if the result is as expected
        result_str = dest_buffer.value.decode('utf-8')
        
        if result_str != expected_result or result != expected_length:
            print_color(f"ERROR: ft_strlcat('{dest_buffer.value.decode('utf-8')}', '{src}', {size}) = '{result_str}', {result}, Expected: '{expected_result}', {expected_length}", "red")
        else:
            print_color(f"ft_strlcat('{dest_buffer.value.decode('utf-8')}', '{src}', {size}) = '{result_str}', {result}, Expected: '{expected_result}', {expected_length}", "green")

