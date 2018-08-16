# fizz buzz
def fizz_buzz(size):
    output = []
    for number in range(1, size+1):
        if number % 3 == 0 and number % 5 == 0:
            output.append('fizz_buzz')
        elif number % 3 == 0:
            output.append('fizz')
        elif number % 5 == 0:
            output.append('buzz')
        else:
            output.append(number)
    return output


# binnary search
def binnary_search(numbers_list, number, left, right):
    if right >= left:
        # get middle of array
        middle = left + (right - left)/2
        middle = int(middle)

        if numbers_list[middle] == number:
            return middle

        # number searched is smaller than the number in the middle
        elif numbers_list[middle] > number:
            return binnary_search(numbers_list, number, left, middle-1)

        # number searched is bigger thant the number in the middle
        else:
            return binnary_search(numbers_list, number, middle+1, right)

    else:
        return -1
