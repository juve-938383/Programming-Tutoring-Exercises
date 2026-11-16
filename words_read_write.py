'''
Write a function words_read_write(inputfilename, outputfilename) that receives as input
- inputfilename: a string representing the pathname of a text file,
- outputfilename: a string representing the pathname of a text file.

The inputfile contains several lines of text with words separated by
any number of spaces (' '), commas (','), periods ('.').

The function returns a dictionary where:
- the keys are the words found in inputfilename, all in lowercase;
- the corresponding values are lists of numbers, representing the line
numbers in the input file where the words were found (case-insensitive,
first line of the file is line 0).

Moreover, the function must write in each line of outputfilename
one of the words found in inputfilename in lowercase, followed by
a space (' '), followed by the line numbers where the word appeared in
the input file separated by spaces.
Words in the output file must be ordered in descending order, while
the line numbers must be in ascending order.

Example, if the content of inputfilname is:
cat tacos Coast
coast toast
Tacos

TOAST caT costa
cOast toast
    
words_read_write(inputfilename, outputfilename) must return the dictionary
{'cat':[0,4], 'tacos':[0,2], 'coast':[0,1,5], 'toast':[1,4,5], 'costa':[4]}
and write the following in outputfilename:
toast 1 4 5
tacos 0 2
costa 4
coast 0 1 5
cat 0 4
'''

def words_read_write(inputfilename, outputfilename):

    with open(inputfilename, "r", encoding="utf-8") as f:
        inp = f.read()

    inp = inp.split("\n")
    for i in range(len(inp)):
        inp[i].replace(",", " ")
        inp[i].replace(".", " ")
        inp[i] = inp[i].split()
        inp[i] = list(map(str.lower, inp[i]))

    out_dict = dict()
    for i in range(len(inp)):
        for word in inp[i]:
            if word not in out_dict.keys():
                out_dict[word] = []
            out_dict[word].append(i)

    out_dict = dict(sorted(out_dict.items()))


    output = ""
    for t in out_dict.items():
        output += t[0]
        output += " "
        for v in t[1]:
            output += str(v)
            output += " "
        output += "\n"

    with open(outputfilename, "w", encoding="utf-8") as f:
        f.write(output)


if __name__ == "__main__":
    words_read_write("input.txt", "output.txt")

