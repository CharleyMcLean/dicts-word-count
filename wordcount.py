# put your code here.
def word_count(a_file):
    """
    Rem
    """

    test_file = open(a_file)
    word_list = []
    for line in a_file:
        poem_line = line.split(" ")
        word_list.append(poem_line)
    counts = {}
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1

    return counts

print word_count("test.txt")