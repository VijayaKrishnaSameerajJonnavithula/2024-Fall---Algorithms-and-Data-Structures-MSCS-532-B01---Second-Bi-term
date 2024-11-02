class InvertedIndex:
    def __init__(self):
        """Initialize the inverted index as a dictionary."""
        self.index = {}

    def add_document(self, doc_id, text):
        """
        Add a document to the inverted index.

        :param doc_id: Unique identifier for the document.
        :param text: Text content of the document.
        """
        for word in text.split():
            word = word.lower()  # Normalize to lower case
            if word not in self.index:
                self.index[word] = []
            self.index[word].append(doc_id)

    def search(self, keyword):
        """
        Search for documents containing the keyword.

        :param keyword: The keyword to search for.
        :return: List of document IDs containing the keyword.
        """
        return self.index.get(keyword.lower(), [])

class TrieNode:
    def __init__(self):
        """Initialize a Trie node with children and frequency."""
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class AutocompleteTrie:
    def __init__(self):
        """Initialize the Trie for autocomplete."""
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.

        :param word: The word to insert.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1  # Increase frequency count for autocomplete relevance

    def autocomplete(self, prefix):
        """
        Retrieve autocomplete suggestions for a given prefix.

        :param prefix: The prefix to search for.
        :return: List of words that match the prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        suggestions = []
        self._find_words(node, prefix, suggestions)
        return suggestions

    def _find_words(self, node, prefix, suggestions):
        """Helper method to find words in the Trie."""
        if node.is_end_of_word:
            suggestions.append(prefix)
        for char, child_node in node.children.items():
            self._find_words(child_node, prefix + char, suggestions)

import heapq

class PriorityQueue:
    def __init__(self):
        """Initialize the priority queue."""
        self.elements = []

    def push(self, item, priority):
        """
        Add an item to the priority queue with a given priority.

        :param item: The item to add.
        :param priority: The priority of the item.
        """
        heapq.heappush(self.elements, (-priority, item))  # Use negative priority for max-heap

    def pop(self):
        """
        Remove and return the highest priority item.

        :return: The item with the highest priority.
        """
        return heapq.heappop(self.elements)[1]

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.elements) == 0

class MetadataHashTable:
    def __init__(self):
        """Initialize the metadata hash table."""
        self.table = {}

    def add_metadata(self, doc_id, metadata):
        """
        Add metadata for a document.

        :param doc_id: Unique identifier for the document.
        :param metadata: Metadata associated with the document.
        """
        self.table[doc_id] = metadata

    def get_metadata(self, doc_id):
        """
        Retrieve metadata for a document.

        :param doc_id: Unique identifier for the document.
        :return: Metadata associated with the document.
        """
        return self.table.get(doc_id)

# Example Usage
if __name__ == "__main__":
    # Create and populate InvertedIndex
    inverted_index = InvertedIndex()
    inverted_index.add_document(1, "Python is great for data structures")
    inverted_index.add_document(2, "Data structures are essential for algorithms")
    
    print("Inverted Index Search for 'data':", inverted_index.search("data"))

    # Create and populate AutocompleteTrie
    autocomplete_trie = AutocompleteTrie()
    words = ["python", "pythonic", "java", "javascript", "jazz", "jargon"]
    for word in words:
        autocomplete_trie.insert(word)

    print("Autocomplete Suggestions for 'ja':", autocomplete_trie.autocomplete("ja"))

    # Create and use PriorityQueue
    priority_queue = PriorityQueue()
    priority_queue.push("doc1", 5)
    priority_queue.push("doc2", 10)
    priority_queue.push("doc3", 1)

    print("Priority Queue Pop:", priority_queue.pop())
    print("Priority Queue Pop:", priority_queue.pop())

    # Create and use MetadataHashTable
    metadata_table = MetadataHashTable()
    metadata_table.add_metadata(1, {"title": "Python Basics", "url": "http://example.com/python"})
    print("Metadata for doc 1:", metadata_table.get_metadata(1))
