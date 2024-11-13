class InvertedIndex:
    def __init__(self):
        self.index = {}

    def add_document(self, doc_id, text):
        for word in text.split():
            word = word.lower()
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(doc_id)

    def search(self, keyword):
        return self.index.get(keyword.lower(), set())

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class AutocompleteTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def autocomplete(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            results.extend(self._collect_words(next_node, prefix + char))
        return results

import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item, priority):
        heapq.heappush(self.elements, (-priority, item))

    def pop(self):
        return heapq.heappop(self.elements)[1] if self.elements else None

class MetadataHashTable:
    def __init__(self):
        self.table = {}

    def add_metadata(self, doc_id, metadata):
        self.table[doc_id] = metadata

    def get_metadata(self, doc_id):
        return self.table.get(doc_id)
