"""Name: Dustin Barnes
Class: 2420-001
Project 7: Dictionaries"""

from hashmap import HashMap

def clean_line(raw_line):
    """"Removes all punctuation from input string and
    returns a list of all words which have a length greater than one."""
    if not isinstance(raw_line, str):
        raise ValueError("Input must be a string")
    line = raw_line.strip().lower()
    line = list(line)
    for index in range(len(line)): #pylint: disable=C0200
        if line[index] < 'a' or line[index] > 'z':
            line[index] = ' '
    cleaned = "".join(line)
    words = [word for word in cleaned.split() if len(word) > 1]
    return words

def main():
    """Main function that takes in the text of Alice in Wonderland
    and counts the words and prints the top 15 words."""
    hash_map = HashMap()
    with open("AliceInWonderland.txt", encoding='utf8') as input_file:
        for line in input_file:
            words = clean_line(line)
            for word in words:
                hash_map.set(word)
    sort_by_word_count = hash_map.sort_by_value()
    print("The most common words are:")
    for i in range(15):
        print(sort_by_word_count[i][0] + "\t\t" + str(sort_by_word_count[i][1]))

if __name__ == "__main__":
    main()
