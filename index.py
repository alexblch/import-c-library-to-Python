import ctypes
a = 8
b = 7
lib = ctypes.cdll.LoadLibrary('./libadd.so') # Load the shared library into c types.

lib.add.argtypes = (ctypes.c_int, ctypes.c_int) # Set the argument types of the function.
lib.add.restype = ctypes.c_int # Set the return type of the function.

result = lib.add(a,b)
result2 = lib.multiplicate(a,b)
print(f'Sum is {result}')
print(f'Product is {result2}')