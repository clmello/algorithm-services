def fizz_buzz(size):
    output = []
    for number in range(1, size+1):
        if number % 3 == 0  and number % 5 == 0:
            output.append('fizz_buzz')
        elif number % 3 == 0:
            output.append('fizz')
        elif number % 5 == 0:
            output.append('buzz')
        else:
            output.append(number)
    return output