def count_words(sentence):
    # Bug: Incorrectly splits on spaces, which can lead to wrong word count
    return len(sentence.split(" "))

if _name_ == "_main_":
    test_sentence = "Hello, world! This is Feature 1."
    print("Word count:", count_words(test_sentence))  # Expected output: 5, but counts punctuation

    # Bug: Forgot to strip whitespace from sentence, so trailing spaces cause incorrect word count
    test_sentence_with_space = "  Hello, world! This is Feature 1.   "
    print("Word count with extra spaces:", count_words(test_sentence_with_space))  # Expected output: 5
