from ProjectPhase2 import InvertedIndex, AutocompleteTrie, PriorityQueue, MetadataHashTable

if __name__ == "__main__":
    # Inverted Index Demonstration
    inverted_index = InvertedIndex()
    inverted_index.add_document(1, "Python is great for data science")
    inverted_index.add_document(2, "Data structures are essential")
    print("Search for 'data':", inverted_index.search("data"))

    # Autocomplete Trie Demonstration
    trie = AutocompleteTrie()
    for word in ["python", "java", "javascript", "pythonic"]:
        trie.insert(word)
    print("Autocomplete for 'py':", trie.autocomplete("py"))

    # Priority Queue Demonstration
    pq = PriorityQueue()
    pq.push("doc1", 5)
    pq.push("doc2", 10)
    print("Highest priority:", pq.pop())

    # Metadata Hash Table Demonstration
    metadata = MetadataHashTable()
    metadata.add_metadata(1, {"title": "Python Basics", "url": "http://example.com"})
    print("Metadata for doc 1:", metadata.get_metadata(1))
