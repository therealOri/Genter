import os
import numpy as np



def clear():
    os.system("clear||cls")

def check_type(thing):
    print(f'{thing}\n{type(thing)}')


def sys_check():
    if os.name == 'nt':
        return None
    elif os.name == 'darwin':
        return None
    else:
        return 200



def randint(min_num, max_num, how_many=1):
    check = sys_check()
    random_ints=[]
    if not check:
        for i in range(how_many):
            random_bytes = os.urandom(8192)
            random_int = int.from_bytes(random_bytes)
            random_int = random_int % (max_num - min_num) + min_num
            random_ints.append(random_int)
    else:
        with open("/dev/urandom", "rb") as f:
            for i in range(how_many):
                random_bytes = f.read(8192)
                random_int = int.from_bytes(random_bytes, byteorder='big')
                random_int = random_int % (max_num - min_num + 1) + min_num
                random_ints.append(random_int)
    if len(random_ints) < 2:
        return random_int
    else:
        return random_ints






#NOTE
#https://stackoverflow.com/a/65499571/15114290  |  True == 1 when working with sets.
#Sets are also ordered from boolean, ints, strings
def choice(list_of_data):
    maximum = len(list_of_data)-1
    #for example lets say "list_of_data" is 11 items long, we need to account for index 0, 0 is the minimum so now there are 10 index spots to choose from, not 11.
    #we will get an "index out of range" error without "-1".
    index = randint(0, maximum, 1)

    #List or tuple
    if isinstance(list_of_data, (list, tuple, str)):
        option = list_of_data[index]
        return option

    #Dictionary
    elif isinstance(list_of_data, dict):
        keys = list(list_of_data.keys())
        selected_key = keys[index]
        selected_value = list_of_data[selected_key]
        selected_dict = {selected_key: selected_value}
        return selected_dict #type dictionary

    #Set
    elif isinstance(list_of_data, set):
        set_list = list(list_of_data)
        set_option = set_list[index]
        return set_option
    else:
        raise ValueError('\nUnable to make a choice. The data provided is not a list, tuple, set, or dictionary.')





def shuffle(list_of_data):
    if isinstance(list_of_data, list):
        random_numbers = [num for num in randint(0, len(list_of_data)-1, len(list_of_data))]
        for i, j in enumerate(random_numbers):
            list_of_data[i], list_of_data[j] = list_of_data[j], list_of_data[i]
        return list_of_data

    elif isinstance(list_of_data, tuple):
        list_of_data = list(list_of_data)
        random_numbers = [num for num in randint(0, len(list_of_data)-1, len(list_of_data))]
        for i, j in enumerate(random_numbers):
            list_of_data[i], list_of_data[j] = list_of_data[j], list_of_data[i]
        return tuple(list_of_data)

    elif isinstance(list_of_data, dict):
        list_of_data = list(list_of_data.items())
        random_numbers = [num for num in randint(0, len(list_of_data)-1, len(list_of_data))]
        for i, j in enumerate(random_numbers):
            list_of_data[i], list_of_data[j] = list_of_data[j], list_of_data[i]
        return dict(list_of_data)

    elif isinstance(list_of_data, str):
        random_numbers = [num for num in randint(0, len(list_of_data)-1, len(list_of_data))]
        chars = list(list_of_data)
        for i, j in enumerate(random_numbers):
            chars[i], chars[j] = chars[j], chars[i]
        list_of_data = ''.join(chars)
        return list_of_data
    else:
        raise ValueError('\nUnable to shuffle data. The data provided is not a list, tuple, or dictionary.')












if __name__ == '__main__':
    clear()
    print("uwu")
