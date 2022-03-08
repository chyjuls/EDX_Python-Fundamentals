# In a heterogenous lists find average of even and odd integers and return aa tuple.


def even_odds(a_list):
    new_list = [value for value in a_list if isinstance(value, int)]
    even = list(filter(lambda elem: elem % 2 == 0, new_list))
    result = sum(even) / len(even)
    odd = list(filter(lambda elem: elem % 2 == 1, new_list))
    res = sum(odd) / len(odd)
    avg_tuple = (result, res)
    return avg_tuple


a_list = [1, 2, 3, 4, "cat", "dog", 5, 6]
print(even_odds(a_list))
