def sort_sentence(sentence=str):
    wordlist = sentence.split()
    length = len(wordlist)
    new_sentence = []

    for _ in range(length):
        shortest_word = min(wordlist, key=len)
        new_sentence.append(shortest_word)
        wordlist.remove(shortest_word)

    return ' '.join(new_sentence).capitalize()
