import re

def regex_strip(s, chars=None):
    if chars is None:
        # If no specific characters are provided, strip whitespace
        regex = re.compile(r'^\s+|\s+$')
    else:
        # If specific characters are provided, strip those characters
        regex = re.compile(f'^[{re.escape(chars)}]+|[{re.escape(chars)}]+$')

    return regex.sub('', s)

# Example usage:
text = "    Hello, world!    "
chars_to_strip = " !"
result_without_chars = regex_strip(text)  # Strips whitespace by default
result_with_chars = regex_strip(text, chars_to_strip)

print("Result without specific characters:", result_without_chars)
print("Result with specified characters:", result_with_chars)