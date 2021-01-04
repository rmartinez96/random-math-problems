import func as f


# Header to make the script look nice.
def header():
    print('\n'
          'Random Stuff \n'
          'Enter an operating value listed below: \n'
          '\n'
          '0: Exit \n'
          '1: Factorial \n'
          '2: Sequence Sum \n'
          '3: Fibonnaci Sequence \n'
          '4: Pascal\'s Triangle \n')


# Footer to make the script look nice.
def footer():
    print('\n'
          '-------------------------')


if __name__ == "__main__":
    x = -1

    while x != 0:
        header()

        try:
            x = int(input('::\t'))

            if x > 0:
                try:
                    y = int(input(':|\t'))
                    if x == 1: print(':-\t', f.factorial(y))
                    if x == 2: print(':-\t', f.seq_sum(y))
                    if x == 3: print(':-\t', f.fib(y))
                    if x == 4: [print(f'{i}-\t', j, end = '\n') for i, j in enumerate(f.pascals_triangle(y))]

                except ValueError:
                    print("Input should be an integer greater than ZERO. ")

        except ValueError:
            print("Input should be an integer greater than ZERO. ")

        footer()