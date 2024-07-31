def remove_trailing_whitespace(input_string):
    return input_string.rstrip()

example_string = "Hello, World!   "
print(f"Original: '{example_string}'")
print(f"Trimmed: '{remove_trailing_whitespace(example_string)}'")
