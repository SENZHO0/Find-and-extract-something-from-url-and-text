text = """The following example creates an ArrayList with a capacity of 50 elements.
Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."""

# ubah text jadi words
words = text.split()

# cek apakah dari a atau e atau tidak
target_words = []
for word in words:
    clean = word.strip(".,").lower()
    if clean.startswith('a') or clean.startswith('e'):
        target_words.append(clean)

print("Words starting with 'a' or 'e':")
for word in target_words:
    print("-", word)