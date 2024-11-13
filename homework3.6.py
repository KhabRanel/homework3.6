def calculate_structure_sum(*args):
    global summ
    for x in args:
        if isinstance(x, dict):
            calculate_structure_sum(*(x.items()))
        elif isinstance(x, tuple):
            calculate_structure_sum(list(x))
        elif isinstance(x, set):
            calculate_structure_sum(list(x))
        elif isinstance(x, str):
            summ += len(x)
        elif isinstance(x, int):
            summ += x
        elif isinstance(x, list):
            for i in x:
                if isinstance(i, dict):
                    calculate_structure_sum(*(i.items()))
                elif isinstance(i, tuple):
                    calculate_structure_sum(list(i))
                elif isinstance(i, set):
                    calculate_structure_sum(list(i))
                elif isinstance(i, list):
                    calculate_structure_sum(i)
                elif isinstance(i, int):
                    summ += i
                elif isinstance(i, str):
                    summ += len(i)
    return summ


summ = 0
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(*data_structure)
print(result)
