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
        with open(path) as f:
            file_content = f.read().strip()
            print('\n', file_content, '\n')
            return file_content
    except:
        raise FileNotFoundError(f"({path}) was not found")
