from collections import defaultdict


class CountWordsTrie:
    END = "_end"
    COMPLETE_WORDS = "complete_words"

    def __init__(self):
        self.root = defaultdict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        At the same time increases a counter at each node, of the complete words inserted
        """
        current = self.root
        for letter in word:
            current = current.setdefault(letter, {})

            if CountWordsTrie.COMPLETE_WORDS in current:
                current[CountWordsTrie.COMPLETE_WORDS] += 1
            else:
                current[CountWordsTrie.COMPLETE_WORDS] = 1

        current.setdefault(CountWordsTrie.END)

    def search(self, word):
        """Returns if the word is in the trie."""
        current = self.root

        for letter in word:
            if letter not in current:
                return False
            else:
                current = current[letter]

        if CountWordsTrie.END in current:
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

    def count_complete_words_start_with(self, prefix):
        current = self.root

        for letter in prefix:
            if letter not in current:
                return 0
            else:
                current = current[letter]

        return current[CountWordsTrie.COMPLETE_WORDS]

    def __str__(self):
        return str(self.root)

if __name__ == "__main__":
    trie = CountWordsTrie()
    trie.insert("s")
    trie.insert("ss")
    trie.insert("sss")
    trie.insert("ssss")
    trie.insert("sssss")

    print(trie)

    print(trie.count_complete_words_start_with("s"))
    print(trie.count_complete_words_start_with("ss"))
    print(trie.count_complete_words_start_with("sss"))
    print(trie.count_complete_words_start_with("ssss"))
    print(trie.count_complete_words_start_with("sssss"))
    print(trie.count_complete_words_start_with("ssssss"))
