# python_escape_characters.py

"""
A quick reference for Python escape sequences.
Useful for string manipulation, regex, and encoding tasks.
Save this file and import or open it whenever needed.
"""

ESCAPE_CHARACTERS = {
"\n": "New line",
"\t": "Horizontal tab",
"\r": "Carriage return",
"\b": "Backspace",
"\f": "Form feed",
"\v": "Vertical tab",
"\\": "Backslash character (\)",
"\'": "Single quote (')",
'\"': 'Double quote (")',
"\a": "Bell (alert sound)",
"\N{name}": "Unicode character by name",
"\uXXXX": "Unicode character (16-bit, e.g., \u03A9 for Ω)",
"\UXXXXXXXX": "Unicode character (32-bit, e.g., \U0001F600 for 😀)",
"\xhh": "Character with hex value (e.g., \x41 for 'A')",
"\ooo": "Character with octal value (e.g., \101 for 'A')"
}

def show_escape_characters():
"""Print all escape characters with their descriptions."""
print("\nPython Escape Character Reference:\n")
for seq, desc in ESCAPE_CHARACTERS.items():
print(f"{seq:15} -> {desc}")

if **name** == "**main**":
show_escape_characters()
