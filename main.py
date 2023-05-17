def fizzbuzz():
    for i in range(1, 101):
        if ((i % 3) + (i % 5)) != 0:
            if i % 3 == 0:
                print('Fizz')
            elif i % 5 == 0:
                print('Buzz')
        else:
            print('FizzBuzz')


def sort_array(a: list[int], b: list[int]):
    b_dict = {}

    for i in range(0, len(b)):
        b_dict[i] = b[i]

    values = sorted(b_dict.values())
    sorted_b_dict = {}

    for i in values:
        for k in b_dict.keys():
            if b[k] == i:
                sorted_b_dict[k] = b_dict[k]
                break

    a = [a[i] for i in sorted_b_dict.keys()]
    return a


def roman_number(string):
    roman_num, pre_num, num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0, 0
    for i in string:
        val = roman_num[i]
        if val > pre_num:
            num += val - 2 * pre_num
        else:
            num += val
        pre_num = val
    return num


def main():
    fizzbuzz()
    print(sort_array([1, 4, 6], [11, 33, 22]))
    print(roman_number("MCMXCIVIX"))


if __name__ == "__main__":
    main()


















