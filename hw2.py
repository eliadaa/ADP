"""
● Să se scrie o funcție care primește un număr nedefinit de
parametrii și să se calculeze suma parametrilor care reprezintă
numere întregi sau reale.
○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).
○ your_function() va returna 0.
○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
● Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:
○ suma totală a numerelor
○ suma numerelor pare
○ suma numerelor impare
● Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează
valoarea 0
"""

# 1
def my_function(*args, **kwargs):
    sum = 0

    for arg in args:
        if type(arg) in (int, float):
            sum += arg

    # if keyword mattered:
    # for value in kwargs.values():
    #     if type(value) in (int, float):
    #         sum += value

    print(sum)
    return sum

my_function(1, 5, -3, 'abc', [12, 56, 'cad'] )# va returna 3 (1 + 5 - 3).
my_function() # va returna 0.
my_function(2, 4, 'abc', param_1=2) # va returna 6 (2 + 4).

# 2
# ● Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează:
# ○ suma totală a numerelor
# ○ suma numerelor pare
# ○ suma numerelor impare
# recursive, sum

def my_sum(my_list, total_sum=0, even_sum=0, odd_sum=0):
    if not my_list:
        return total_sum, even_sum, odd_sum

    current_number = my_list[0]

    total_sum += current_number

    if current_number % 2 == 0:
        even_sum+=current_number
    else:
        odd_sum+=current_number

    return my_sum(my_list[1:], total_sum, even_sum, odd_sum)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total, even, odd = my_sum(my_list)
print("total sum: ", total)
print("even sum: ", even)
print("odd sum: ", odd)


# 3
# ● Să se scrie o funcție care citește de la tastatură și returnează valoarea
# dacă aceasta este un număr întreg, altfel returnează
# valoarea 0
def read_int():
    try:
        my_input = input("please enter a number: ")
        value = int(my_input)
        return value
    except ValueError:
        # if the conversion to int fails, return 0
        print("not an integer!")
        return 0

print("result: ", read_int())
