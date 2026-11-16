'''
Define the function func1(file_in : str) -> list[str], which takes a
string containing the path to a text file and returns a list of strings.

The function opens the text file, extracts all the words, and converts
them to lowercase.

Return a list of the unique words found in the text file, sorted in
**alphabetical order**.

Example:
If file_in refers to 'txt/in_01.txt', the function returns:
expected = ['bat', 'car', 'cat', 'condor', 'rat']

Note: When extracting words, consider only alphabetic characters.
Examples:
- The string '7od842m3m\t7gbe' becomes 4 words: ['od', 'm', 'm', 'gbe'].
- The string 'And I to him: "Poet, I ask you'
  becomes ['and', 'i', 'to', 'him', 'poet', 'i', 'ask', 'you'].
'''

def func1(file_in : str) -> list[str]:
    with open(file_in, "r", encoding="utf8") as f:
        text = f.read().lower()

    word = ""
    word_list = []

    for character in text:
        if character.isalpha():
            word += character
        elif word != "":  # in case the character is not part of a word AND we have a word
            word_list.append(word)
            word = ""


    if word:
        word_list.append(word)

    

    word_set = set(word_list)
    return sorted(word_set)