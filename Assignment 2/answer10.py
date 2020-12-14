# Write a function that takes camel-cased strings (i.e.ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.
def change_case(str, separator):
    res = [str[0].lower()]
    res1 = [separator[0].lower()]
    for data in str[1:] and separator[1:]:
        if data in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res1.append('-')
            res.append(data.lower())
            res1.append(data.lower())
        else:
            res.append(data)
            res1.append(data)
    return ''.join(res) + "\n" + ''.join(res1)


result = change_case("ThisIsCamelCased", "ThisIsCamelCased")
print(result)
