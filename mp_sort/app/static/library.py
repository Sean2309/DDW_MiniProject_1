from org.transcrypt.stubs.browser import *
import random

def insertion_sort(array_list):
    for outer_index in range(1, len(array_list)):
        inner_index = outer_index
        while (inner_index > 0) and (array_list[inner_index] < array_list[inner_index-1]):
            array_list[inner_index -1], array_list[inner_index] = array_list[inner_index], array_list[inner_index-1]
            inner_index -= 1
    return array_list


def gen_random_int(number, seed):
    array = []
    for i in range(number):
        array.append(i)
    random.seed(seed)
    random.shuffle(array)
    return array

def convert_list_str_to_int(array):
    for i in range(len(array)):
        array[i] = int(array[i])
    return array

def gen_list_of_str(array):
    array_str = ""
    for i in array:
        array_str = array_str + str(i) + ","
    array_str = (array_str[:-1]) + "."
    return array_str

def generate():
    number = 10
    seed = 200
    array = gen_random_int(number, seed)
    array_str = gen_list_of_str(array)
    document.getElementById("generate").innerHTML = array_str


def sortnumber1():
    '''	This function is used in Exercise 1.
            The function is called when the sort button is clicked.

            You need to do the following:
            - get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
            - create a list of integers from the string of numbers
            - call your sort function, either bubble sort or insertion sort
            - create a string of the sorted numbers and store it in array_str
    '''
    array = document.getElementById("generate").innerHTML
    array = array.rstrip(".")
    array_l = array.split(",")
    array_l = convert_list_str_to_int(array_l)
    array_str = insertion_sort(array_l)
    document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
    ''' This function is used in Exercise 2.

    The function is called when the sort button is clicked.
    You need to do the following:
    - Get the numbers from a string variable "value".
    - Split the string using comma as the separator and convert them to
    a list of numbers
    - call your sort function, either bubble sort or insertion sort
    - create a string of the sorted numbers and store it in array_str
    '''
    value = document.getElementsByName("numbers")[0].value
    if value == "":
        window.alert("Your textbox is empty")
        pass
    else:
        string_list = value.split(',')
        int_list = convert_list_str_to_int(string_list)
        sorted_list = insertion_sort(int_list)
        array_str = gen_list_of_str(sorted_list)
    document.getElementById("sorted").innerHTML = array_str