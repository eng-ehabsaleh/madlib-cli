import re


print(
    """
    ********************************
    **** Welcome to Madlib Game ****
    ********************************
    *                              *
    *                              *
    *    Please fill the blanks    *
    ********************************
    """)


def read_template(path):
    """
    read_template function takes a path for text file and then open it and read it and if the path was not correct the function will raise a FileNoyFoundError.
    """

    try:
        file = open(path)
        file_content = file.read().strip()
        print('\n', file_content, '\n')
        file.close()
        return file_content
    except:
        raise FileNotFoundError(f"({path}) was not found")


def parse_template(word):
    """
    parse function takes in string and search of curly bracies  and return list of curly prasies content found and the text without the content of curly prasies 
    """
    words = list(re.findall(r'{(.*?)}', word))
    text = re.sub('{.*?}', '{}', word)
    return text, words


def merge(text, word):
    """
    merge function that takes in a “bare” template and a list of user entered language parts,
    and returns a string with the language parts inserted into the template.
    """
    merged_text = text.format(*word)
    with open('assets/the modified text.txt', 'w') as result:
        result.write(merged_text)
        print(merged_text)
    return merged_text


if __name__ == "__main__":

    file = read_template("assets/test.txt")
    text, words = parse_template(file)
    result = []
    for i in words:
        user_input = input(f"Enter {i}> ")
        result.append(user_input)
    madlib_result = merge(text, result)
