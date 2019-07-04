

def my_func(x, y, z=20):
    return x, y, z

list = ["first", "2nd", "3rd"]
dict = {"x": 13, "y": 14, "z": 15}

return_val = my_func(*list)
print(f"calling with *args: {return_val}")

return_val = my_func(**dict)
print(f"calling with **kwargs: {return_val}")
print()
