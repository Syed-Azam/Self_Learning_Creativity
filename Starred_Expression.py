# Starred Expression to Unpack a list or dictionary

# print(*[1, 2, 3]) -----> print(1, 2, 3)
# type(*[1, 2, 3]) -----> type(1, 2, 3) ---> error
# a,*b,c = (1, 2 , 3, 4) ----> a = 1, b = [2, 3], c = 3
# print(**{"a": 1}) ----> print(a = 1) ----> error
# print(*[1, 2, 3],**{'sep': '0', 'end': '_'}) ----> 10203_