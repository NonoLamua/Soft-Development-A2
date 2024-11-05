import re

def count_words(sentence):
    # Use regular expressions to split on any sequence of non-word characters, 
    # which removes extra spaces and punctuation
    words = re.findall(r'\b\w+\b', sentence)
    return len(words)

if _name_ == "_main_":
    test_sentence = "Hello, world! This is Feature 1."
    print("Word count:", count_words(test_sentence))  # Expected output: 5

    test_sentence_with_space = "  Hello, world! This is Feature 1.   "
    print("Word count with extra spaces:", count_words(test_sentence_with_space))  # Expected output: 5import re
