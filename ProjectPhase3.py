import sqlite3
from functools import lru_cache
from collections import defaultdict
import heapq

# Disk-Based Inverted Index
class DiskInvertedIndex:
    def __init__(self, db_path="inverted_index.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS inverted_index (
                word TEXT PRIMARY KEY,
                doc_ids TEXT
            )
        """)

    def add_document(self, doc_id, text):
        for word in text.split():
            word = word.lower()
            self.cursor.execute("SELECT doc_ids FROM inverted_index WHERE word=?", (word,))
            result = self.cursor.fetchone()
            if result:
                doc_ids = result[0] + f",{doc_id}"
                self.cursor.execute("UPDATE inverted_index SET doc_ids=? WHERE word=?", (doc_ids, word))
            else:
                self.cursor.execute("INSERT INTO inverted_index (word, doc_ids) VALUES (?, ?)", (word, str(doc_id)))
        self.conn.commit()

    @lru_cache(maxsize=100)
    def search(self, word):
        word = word.lower()
        self.cursor.execute("SELECT doc_ids FROM inverted_index WHERE word=?", (word,))
        result = self.cursor.fetchone()
        return set(map(int, result[0].split(","))) if result else set()

# Radix Tree for Autocomplete
class RadixTreeNode:
    def __init__(self, key=""):
        self.key = key
        self.children = {}
        self.is_end_of_word = False

class RadixTree:
    def __init__(self):
        self.root = RadixTreeNode()

    def insert(self, word):
        node = self.root
        while word:
            for char, child in node.children.items():
                if word.startswith(char):
                    node = child
                    word = word[len(char):]
                    break
            else:
                node.children[word] = RadixTreeNode(word)
                node.children[word].is_end_of_word = True
                break

    def autocomplete(self, prefix):
        node = self.root
        suggestions = []

        # Find node matching prefix
        while prefix:
            for char, child in node.children.items():
                if prefix.startswith(char):
                    node = child
                    prefix = prefix[len(char):]
                    break
            else:
                return suggestions  # No matching prefix
        
        # Perform DFS for suggestions
        def dfs(node, path):
            if node.is_end_of_word:
                suggestions.append(path)
            for key, child in node.children.items():
                dfs(child, path + key)
        
        dfs(node, prefix)
        return suggestions

# Priority Queue for Ranking (Basic Max-Heap)
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, score, doc_id):
        heapq.heappush(self.heap, (-score, doc_id))  # Use negative for max-heap

    def get_top(self, k):
        return [heapq.heappop(self.heap) for _ in range(min(k, len(self.heap)))]

# Example Usage
if __name__ == "__main__":
    # Initialize components
    index = DiskInvertedIndex()
    trie = RadixTree()
    ranking = PriorityQueue()

    # Add documents
    docs = {
        1: "search engines are important",
        2: "optimization is key in search engines",
        3: "python is a versatile language",
        4: "building scalable systems is essential",
    }
    for doc_id, text in docs.items():
        index.add_document(doc_id, text)
        for word in text.split():
            trie.insert(word.lower())

    # Query examples
    print("Search Results for 'search':", index.search("search"))
    print("Search Results for 'python':", index.search("python"))

    # Autocomplete example
    print("Autocomplete Suggestions for 'sc':", trie.autocomplete("sc"))

    # Ranking example
    ranking.insert(0.9, 1)  # Doc 1 with score 0.9
    ranking.insert(0.7, 2)  # Doc 2 with score 0.7
    ranking.insert(0.85, 3)  # Doc 3 with score 0.85
    print("Top Ranked Documents:", ranking.get_top(2))
