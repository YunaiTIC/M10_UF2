input_numbers = input("Introdueix 10 números separats per espais: ")
numbers_list = [int(num) for num in input_numbers.split()]
tuple_numbers = tuple(numbers_list)
sorted_tuple = tuple(sorted(tuple_numbers, reverse=True))

print("Tupla ordenada de major a menor:", sorted_tuple)
