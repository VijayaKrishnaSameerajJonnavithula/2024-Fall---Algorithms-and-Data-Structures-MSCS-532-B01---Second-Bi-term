# Import your implemented classes
from ProjectPhase3 import DiskInvertedIndex, RadixTree, PriorityQueue

# Initialize data structures
index = DiskInvertedIndex()  # Disk-based inverted index
radix_tree = RadixTree()  # Radix tree for autocomplete
priority_queue = PriorityQueue()  # Priority queue for ranking

# Adding documents to the inverted index
print("Adding documents to the inverted index...\n")
documents = {
    1: "search engine optimization techniques",
    2: "data structures and algorithms",
    3: "search engine architecture",
    4: "optimization strategies for large datasets"
}

for doc_id, text in documents.items():
    index.add_document(doc_id, text)  # Add document to inverted index
    words = text.split()  # Split the text into words
    for word in words:
        radix_tree.insert(word)  # Insert each word into the Radix Tree

# Retrieve and display all terms in the inverted index
print("Inverted Index Content:")
all_terms = index.retrieve_all_terms()
for term, doc_ids in all_terms.items():
    print(f"{term}: {doc_ids}")

# Test case 1: Searching for a term
search_term = "engine"
print(f"\nSearch results for term '{search_term}':")
print(index.search(search_term))

# Test case 2: Autocomplete
prefix = "opt"
print(f"\nAutocomplete results for prefix '{prefix}':")
print(radix_tree.search(prefix))

# Test case 3: Ranking documents using a priority queue
print("\nRanking documents based on relevance scores...")
priority_queue.insert(10, "Doc1")
priority_queue.insert(20, "Doc2")
priority_queue.insert(5, "Doc3")

print("Ranked results:")
while not priority_queue.is_empty():
    print(priority_queue.pop())

# Test case 4: Scalability demonstration
print("\nScalability Demonstration: Adding more documents...")
additional_documents = {
    5: "advanced techniques in machine learning",
    6: "search engine ranking algorithms",
    7: "efficient data management for large datasets"
}

for doc_id, text in additional_documents.items():
    index.add_document(doc_id, text)
    words = text.split()
    for word in words:
        radix_tree.insert(word)

# Display updated inverted index
print("\nUpdated Inverted Index Content:")
all_terms = index.retrieve_all_terms()
for term, doc_ids in all_terms.items():
    print(f"{term}: {doc_ids}")

# Perform search after adding new documents
search_term = "techniques"
print(f"\nSearch results for term '{search_term}' after adding new documents:")
print(index.search(search_term))
