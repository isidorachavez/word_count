"""Count words in file."""
import sys
file = open(sys.argv[1])


#def word_count(phrase):
def tokenize(file):
    tokens = []
    for line in file:
        line = line.rstrip()
        split_file = line.split(' ')
        tokens.append(split_file)
    return tokens

def count_words(words):
    word_count = {}
     
    # for lst in words:
    for word in words:
        word_count[word] = word_count.get(word,0) + 1
    
    return word_count

def print_word_counts(word_count):
    for word, count in word_count.items():
        print(f"{word}  {count}")

def normalize_words(words):
    normalized = []
    
    for lst in words:
        for word in lst:
            clean_word = ""
            for char in word:   
                if char.isalpha():
                    clean_word += char
            normalized.append(clean_word.lower())
    return normalized    

    
tokens = tokenize(file)
normalized = normalize_words(tokens)
word_count = count_words(normalized)
print_word_counts(word_count)