
def calculate_structure_sum(data_structure):
    counter = 0
    def counter_sum(data):
        nonlocal counter
        if (isinstance(data, list)
                or isinstance(data, tuple)
                or isinstance(data, set)):
            for i in data:
                counter_sum(i)
        elif isinstance(data, dict):
            counter_sum(list(data.items()))

        elif isinstance(data, str):
            counter += len(data)
        elif isinstance(data, int):
            counter += data
    counter_sum(data_structure)
    print(counter)
    return counter


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

calculate_structure_sum(data_structure)