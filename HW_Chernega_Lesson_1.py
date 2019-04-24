"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List
import string


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second




def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second)




def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return id(first) == id(second)



def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    c=0
    if (type(first_value) == int) and (type(second_value) == int):
        c = int(first_value) * int(second_value)
    if type(first_value) != int:
        raise ValueError
        #            c = int(first_value) * int(second_value)
    if type(second_value) != int:
        raise ValueError
        #           c = int(first_value) * int(second_value)
    return  c




def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        a = int(first_value)*int(second_value)

    except  ValueError:
        print("Not valid input data")
    return a


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    i = 0
    c = 0
    b = int(len(text))
    for i in range(b):
        if word[0:len(word)] == text[i:(i + len(word))]:
            c += 1
        if word[0:len(word)] != text[i:(i + len(word))]:
            pass
        i += 1
    if c>0:
        return True
    else:
        return False
def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    i = 0
    a = []
    while i < 13:
        a = a + [i]
        i += 1
    a.remove(a[6])
    a.remove(a[6])
    return a

def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    i=0
    while i < (len(data) + 1):
        if i == len(data):
            break
        if data[i] < 0:
            data.remove(data[i])
            i = i - 1
        else:
            pass
        i += 1
    return data


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    alphabet = {}
    j = 1
    for i in string.ascii_lowercase:
        alphabet[j] = i
        j += 1
    return alphabet


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    #data = [2, 4, 3, 6, 5, 7, 4, 9]
    i = 0
    while i < (len(data) - 1):
        j = 0
        while j < (len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
            j += 1
        i += 1
    return data


