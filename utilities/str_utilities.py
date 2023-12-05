VOWELS = "aeiouy"

def count_vowels(word):
    
    count = 0
    for vowel in VOWELS:
        count += word.count(vowel)
    return count

        