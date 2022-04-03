
def test(numbers):
    return numbers.count(55) == 2 and numbers.count(18) >= 3

numbers = [55,55,15,43,3,54,534,654, 5435,7656,3535,3,6546,367,63,56,36,36,7,64,7,4,64,74,6,46,47,4,7,3456]
print("Original list:")
print(numbers)

print("Check three simliar numbers of 55 and at least four occurrences of 18 in the given list:")
print(test(numbers))

nums = [432,4,5,524,52,5,34,6,345,2,5,3,6,35,2,5,2,534,5435435,456,34,5,3,534,53,46,54,645,63,635,353]
print("\nOriginal list:")
print(numbers)

print("Check three simliar numbers of 55 and at least four occurrences of 18 in the given list:")
print(test(numbers))

numbers = [23,424,24,235,25,3,425,36,4635,645,63,53,45,45,74,6,36,3534,45,6,475,65,456,35,336]
print("\nOriginal list:")
print(numbers)

print("Check three simliar numbers of 55 and at least four occurrences of 18 in the given list:")
print(test(numbers))
