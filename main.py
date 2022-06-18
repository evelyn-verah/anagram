# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    splitted_words = [x for x in word]
    splitted_anagram = [b for b in anagram]
    # print(splitted_words)
    sorted_words = splitted_words.sort()
    sorted_anagram = splitted_anagram.sort()

    if sorted_words==sorted_anagram:
       return True
    else:
       return False
print(find_anagram("elbowls", "below"))

    

