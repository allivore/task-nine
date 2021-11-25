def sort_sentence(sentence=str):
    wordlist = sentence.split()
    length = len(wordlist)
    new_sentence = []

    for _ in range(length):
        longest_word = max(wordlist, key=len)
        new_sentence.append(longest_word)
        wordlist.remove(longest_word)

    return ' '.join(new_sentence).capitalize()
