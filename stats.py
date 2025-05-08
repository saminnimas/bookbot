def count_words(text: str):
    count = len(text.split())
    return count


def count_characters(text: str):
    char_count = {}
    preprocess_text_tolower = text.lower()

    for k in preprocess_text_tolower:
        if k not in char_count:
            char_count[k] = 1
        else:
            char_count[k] += 1
    return char_count


def create_report_dict(char_count_dict: dict):
    list_of_dict = []

    for k, v in char_count_dict.items():
        if k.isalpha():
            list_of_dict.append({"char": k, "num": v})

    return list_of_dict


def sort_report_dict(list_of_dicts):
    list_dict = list_of_dicts


    def sort_on(dict):
        return dict["num"]
    

    list_dict.sort(reverse=True, key=sort_on)
    return list_dict



if __name__ == '__main__':
    temp = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}
    temp_list = create_report_dict(temp)
    def sort_on(dict):
        return dict["num"]
    temp_list.sort(reverse=True, key=sort_on)
    print(temp_list)
    # print(len(sys.argv))