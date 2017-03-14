from collections import defaultdict


class Trie:
    """Implement a trie with insert, search, and startsWith methods."""

    END = "_end"

    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        """Inserts a word into the trie."""
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault(Trie.END)

    def search(self, word):
        """Returns if the word is in the trie."""
        current = self.root

        for letter in word:
            if letter not in current:
                return False
            else:
                current = current[letter]

        if Trie.END in current:
            return True

        return False

    def starts_with(self, prefix):
        """Returns if there is any word in the trie that starts with the given prefix."""
        current = self.root

        for letter in prefix:
            if letter not in current:
                return False
            else:
                current = current[letter]

        return True

    def __str__(self):
        return str(self.root)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("s")
    trie.insert("ss")
    trie.insert("sss")
    trie.insert("ssss")
    trie.insert("sssss")

    print(trie.search("s"))

    print(trie.starts_with("s"))
    print(trie.starts_with("ss"))
    print(trie.starts_with("sss"))
    print(trie.starts_with("ssss"))
    print(trie.starts_with("sssss"))
    print(trie.starts_with("ssssss"))