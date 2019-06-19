from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
      # >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]

    """
    def title(dictionary):
        if 'name' in dictionary:
            dictionary['name'] = dictionary['name'].title()
        return dictionary
    return(list(map(title, data)))



def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """

    def remove(data):
        for key in set(data.keys()) & set(redundant_keys):
            del data[key]
        return data

    return list(map(remove, data))


def task_3_find_item_via_value(data: DT, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return (list(filter(lambda data_1: value in data_1.values(), data)))



def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """

    if not data:
        return None
    return min(data)


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    return min([str(a) for a in data],key=len,default=None)




def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:

    """
    return min(filter(lambda x: key in x, data), key=lambda x: x[key])

def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    s = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            s.append(data[i][j])
    return max(s)


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    a=[sum(ord(x) for x in text)]
    return a[0]


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for i in range(1, 201):
        a = 0
        for j in range(1, 201):
            if i % j == 0:
                a += 1
        if a == 2:
            yield (i)


def task_11_create_list_of_random_characters() -> List[str]:
    """
    Create list of 20 elements where each element is random letter from latin alphabet

    """
    import random
    a = []
    for letter in range(ord('a'), ord('z') + 1):
        while len(a)<20:
            a.append((chr(letter)))
    random.shuffle(a)
    return(a)