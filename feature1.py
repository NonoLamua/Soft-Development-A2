def count_words(sentence):
    # Bug: Incorrectly splits on spaces, which can lead to wrong word count
    return len(sentence.split(" "))

if _name_ == "_main_":
    test_sentence = "Hello, world! This is Feature 1."
    print("Word count:", count_words(test_sentence))  # Expected output: 5, but counts punctuation
