
phrase = "      spongebob squarepants said HELLO!! to squidward   "
print(phrase)

# Removes all whitespaces before and after the word
print(phrase.strip())

# Removes the space in front
print(phrase.lstrip())

# Removes the trailing space
print(phrase.rstrip())

# All uppercase
print(phrase.upper())

# All lowercase
print(phrase.lower())

# Capitalize the words
print('jellyfish'.capitalize())

# Fist index or -1
print(phrase.find('squidward'))
print(phrase.find('Patrick'))

# Starts with
print(phrase.startswith('squidward'))
print(phrase.startswith(' '))

# Ends with
print(phrase.endswith('squidward'))
print(phrase.endswith(' '))

# Split the String
print(phrase.split())
print(phrase.split('s'))

# All digits?
print('100'.isdigit())
print('1 0'.isdigit())

# All alphanumeric?
print('dfg 234'.isalnum())
print('asfdsgfh543121'.isalnum())
