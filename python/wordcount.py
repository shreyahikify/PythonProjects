def count_words():
    # Get a sentence from the user
    text = input("Enter a sentence or paragraph: ")
    
    # split() breaks the string into a list of words based on spaces
    words = text.split()
    
    # len() gives the total count of items in that list
    word_count = len(words)
    
    print(f"Total words: {word_count}")

count_words()