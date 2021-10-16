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
    sympoles = list(re.findall(r'{(.*?)}', word))
    text = re.sub('{.*?}', '{}', word)
    return text, sympoles
