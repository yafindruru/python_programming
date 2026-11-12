# The name includes a tab (\t), a newline (\n), and some extra spaces.
name = "\t\n  Kentza  \n\t"

# Print original with whitespace
print("Original:")
print(name)

# Print with left spaces removed
print("\nUsing lstrip():")
print(name.lstrip())

# Print with right spaces removed
print("\nUsing rstrip():")
print(name.rstrip())

# Print with all surrounding spaces removed
print("\nUsing strip():")
print(name.strip())

nama = "\t\nKentza\n\t"
print(nama)
print(nama.lstrip())
print(nama.rstrip())
print(nama.strip())