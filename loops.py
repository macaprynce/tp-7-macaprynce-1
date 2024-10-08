def index_of_by_index(word, list, index):
    while index < len(list):
        if list[index] != word:
            index += 1
        else:
            return index
    return -1

def index_of_empty(list):
    for index, element in enumerate(list):
        if element == "":
            return index
        else:
            index += 1
    return -1

def index_of(word, list):
    index = 0
    while index < len(list):
        if list[index] != word:
            index += 1
        else:
            return index
    return -1

def put(word, list):
    for index, element in enumerate(list):
        if element == "":
            list[index] = word
            return index 
    return -1

def remove(word, list):
    eliminaciones = 0
    for index, element in enumerate(list):
        if element == word:
            list[index] = ""
            index += 1
            eliminaciones +=1 
        else:
            index += 1
    return eliminaciones
