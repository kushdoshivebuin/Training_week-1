import sys

my_list = [i for i in range(10000)]
print(sum(my_list))  
print(sys.getsizeof(my_list), "bytes")  # Memory size of the list

# Generator expression to create a generator containing numbers from 0 to 9999
my_gen = (i for i in range(10000))  # Generators are used to save memory, values are computed lazily
print(sum(my_gen))  
print(sys.getsizeof(my_gen), "bytes")  # Memory size of the generator
