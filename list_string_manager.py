'''
Write functions to process a list of words entered by the user as a single string.
The words may be separated by commas, spaces, tabs, semicolons, or any combination of these delimiters.
Your program should:
- Convert the input string into a list of clean words split by any of these delimiters.
- Use a while loop to repeatedly ask the user to enter new words to add to the list until the user enters 'stop'.
- After each addition, convert the updated list back into a comma-separated string and print it.
- Finally, return the concatenated comma-separated string.

Example:
Initial input: apple, banana;cherry\tdate
User adds: elderberry
Current list string: apple,banana,cherry,date,elderberry
User adds: fig
Current list string: apple,banana,cherry,date,elderberry,fig
User inputs: stop
Final list string: apple,banana,cherry,date,elderberry,fig

Functions:
- get_initial_input: Ask the user to enter a string of words separated by commas, spaces, tabs, or semicolons. Return the list of words.
- add_word_to_list: Take the current list and a new word, add the word to the list.
- list_to_comma_string: Convert a list of words to a comma-separated string.
- list_string_manager: Main function using a while loop to add words until 'stop' is entered, printing the list string after each addition.
'''

def get_initial_input():
    in_str = input("Initial input:")
    in_str = in_str.replace(";", " ")
    in_str = in_str.replace(",", " ")
    in_str = in_str.replace("\\t", " ")
    in_str = in_str.split()
    return in_str

def add_word_to_list(words_list, new_word):
    words_list.append(new_word)

def list_to_comma_string(words_list):
    return ",".join(words_list)

def list_string_manager():
    in_str = get_initial_input()
    while(True):
        new_str = input("User adds: ")
        if new_str == "stop":
            break
        add_word_to_list(in_str, new_str)
        print(list_to_comma_string(in_str))


if __name__=="__main__":
    list_string_manager()

   
        