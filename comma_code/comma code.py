spam = ['apple',"pineapple","banana"]

def comma(list_value):
    if len(list_value) == 0:
        return ''
    elif len(list_value) == 1:
        return (spam[0])
    else:
        return (",".join(list_value[:-1]) + " and " + list_value[-1])

print(comma(spam))


