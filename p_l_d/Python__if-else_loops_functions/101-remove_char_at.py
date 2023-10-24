#!/usr/bin/python3
def remove_char_at(str, n):
    count = 0
    n_str = ""
    for c in str:
        if count == n:
            pass
        else:
            n_str += c
        count += 1

    return n_str

print(remove_char_at("Best School", 3))
print(remove_char_at("Chicago", 2))
print(remove_char_at("C is fun!", 0))
print(remove_char_at("School", 10))
print(remove_char_at("Python", -2))