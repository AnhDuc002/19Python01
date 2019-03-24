def read_file(str_file_path):
    '''
    Get all contents from text file path
    :param str_file_path: text file path
    :return: content from text file path
    '''
    file_read = open(str_file_path, 'r')
    content = file_read.read()
    file_read.close()
    return content

def write_file(str_file_path, content):
    '''
    Write content if file to text file path
    :param str_file_path: text file path to write
    :param content: content text
    '''
    file_write = open(str_file_path, 'w')
    file_write.write(content)
    file_write.close()

def get_word_of_file(str_file_path):
    '''
    Get number of line from file path
    :param str_file_path: text file path
    :return: word
    '''

    return read(str_file_path).split()

def get_number_of_line(str_file_path):
    '''
    Get number of line from file path
    :param str_file_path: text file path
    :return: number of line
    '''
    return len(read(str_file_path).split('\n'))

def get_number_of_word(str_file_path):
    '''
    Get number of word from file path
    :param str_file_path: text file path
    :return: Number of word
    '''
    return len(read(str_file_path).split())

def get_number_of_duplicate_word(str_file_path):
    '''
    Get number of characters from file path
    :param str_file_path: text file path
    :return: Number of non-duplicate character
    '''
    dictword = []
    dictword_dup = []
    for charss in get_word_of_file(str_file_path):
        dictword.append((charss, read(str_file_path).count(charss)))
    for i in range(len(dictword)):
        if int(dictword[i][1]) >= 2:
            dictword_dup.append(dictword[i][1])
    return len(dictword_dup)

def get_number_of_characters(str_file_path):
    '''
    Get number of characters from file path
    :param str_file_path: text file path
    :return: Number of character
    '''
    word = read(str_file_path)
    character = []
    for i in range(len(read(str_file_path))):
        if word[i] != '\n' and word[i] != ' ' and word[i] != '|' and word != '=' and word != '-' and word != '+' and word != '[' and word != ']':
            character.append(word[i])
    return len(character)

def get_character(str_file_path):
    '''
    Get number of character from file path
    :param str_file_path: text file path
    :return: character []
    '''
    text = read(str_file_path)
    character = []
    for i in range(len(read(str_file_path))):
        if text[i] != '\n' and text[i] != ' ' and text[i] != '|' and text != '=' and text != '-' and text != '+' and text != '[' and text != ']':
            character.append(text[i])
    return character


def get_the_number_of_duplicate_characters(str_file_path):
    '''
    Get number of character from file path
    :param str_file_path: text file path
    :return: Number of non-duplicate character
    '''
    text = get_character(str_file_path)
    dictword =[]
    for i in range(len(get_character(str_file_path))):
        if text[i] != '\n' and text[i] != ' ' and text[i] != '|' and text != '=' and text != '-' and text != '+' and text != '[' and text != ']' and text.count(text[i]) >= 2:
            dictword.append(text[i])
    return len(dictword)

def delete_content(str_file_path):
    '''
    Delete content of file
    :param str_file_path: text file path
    '''
    write(str_file_path, '')
