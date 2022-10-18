import random
"""
        The array is virtually split into a sorted and an unsorted part. 
        Values from the unsorted part are picked and placed at the correct position in the sorted part.      
"""
def insert_sort(array : list, step : int):
    step_counter = 0
    for i in range(1, len(array)):
        auxiliary = array[i]
        position = i - 1
        if (step_counter == step):
            print(array)
            step_counter = 0
        if (position < 0 or array[position] < auxiliary):
            step_counter = step_counter + 1
        while (position >= 0 and array[position] > auxiliary):
            array[position + 1] = array [position]
            position = position - 1
            array[position + 1] = auxiliary
            step_counter = step_counter + 1
            if (step_counter == step):
                print(array)
                step_counter = 0


"""
    Stooge Sort is a recursive sorting algorithm.
    It generally divides the array into two overlapping parts (2/3 each). 
    After that it performs sorting in first 2/3 part and then it performs sorting in last 2/3 part. 
    And then, sorting is done on first 2/3 part to ensure that the array is sorted.
"""
def stooge_sort(array : list, step : int):
    left = 1                    #left is the lower bound of the subarray which needs to be sorted
    right = len(array)          #right is the upper bound of the subarray that needs to be sorted
    step_counter = 0            #step_counter retains the number of operations or passes did by the program.
                                # This is further compared to 'step' tp verify whether we need to display the partially sorted array or not.
    sort_with_stooge(array, left, right, step, step_counter)


def sort_with_stooge(array : list, left : int, right : int, step : int, step_counter : int):
    if (left > right):          #if our lower bound goes over the upper one, it means that the subarray is sorted
        step_counter = step_counter + 1
        if (step_counter == step):
            print(array)
            step_counter = 0
        return
    """
    If the first element is greater than the last one, we swap them
    """

    if (array[left] > array[right]):
        auxiliary = array[left]
        array[left] = array[right]
        array[right] = auxiliary
        step_counter = step_counter + 1

    if (step_counter == step):
        print(array)
        step_counter = 0
        """
        If there are more than 2 elements in the subarray that need to be sorted, we split the subarray again, using the same algorithm
        """
    if (right - left + 1 > 2):
          third_part_of_array = (int)((right - left + 1) / 3)
          sort_with_stooge(array, left, right - third_part_of_array, step, step_counter)        #we sort the first 2/3 part of the array
          sort_with_stooge(array, left + third_part_of_array, right, step, step_counter)        #we sort the last 2/3 part of the array
          sort_with_stooge(array, left, right - third_part_of_array, step, step_counter)        #we resort the first 2/3 part of the array to ensure that the whole array is sorted

def GenerateListOfNRandomNumbers(arraylenght):
    ListOfRandomNo = []
    for i in range(arraylenght):
        ListOfRandomNo.append(random.randint(0,100))
    return ListOfRandomNo

def menu():
    while True:
        print("Generate a list of `n` random natural numbers. Generated numbers must be between `0` and `100`.")
        array = []
        arraylenght = int(input("Introduce in the menu-driven console application the lenght of the list:"))
        array = GenerateListOfNRandomNumbers(arraylenght)
        print("1. Sort the list using the insert sort algorithm.")
        print("2. Sort the list using the stooge sort algorithm.")
        print("3. Exit the program")

        chosen_option = 0
        chosen_option = int(input("Choose an option between 1 and 3:"))

        if (chosen_option < 1 or chosen_option > 3):
            while (chosen_option < 1 or chosen_option > 3):
                print("The option introduced is invalid. Please introduce a different option. It must be between 1 and 3.")
                chosen_option = int(input())

        if (chosen_option == 1 or chosen_option == 2):
            print(("'Step' is a parameter that tells the program to display the partially sorted list on the console each time it makes `step` operations or passes, depending on the algorithm."))
            step = int(input("Introduce the value for 'step':"))

        if (chosen_option == 1):
            insert_sort(array, step)
        else:
            if (chosen_option == 2):
                stooge_sort(array, step)
            else:
                if (chosen_option == 3):
                    break

def main_program():
    menu()

main_program()