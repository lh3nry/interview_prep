def number_needed(a, b):
    count = [0] * 26
    for char in a:
        count[ord(char)-97] += 1
    for char in b:
        count[ord(char)-97] -= 1


    result = 0
    for i in count:
        result += abs(i)
    return result

# print number_needed('bcadeh', 'hea')
# print number_needed('h', 'hea')
# print number_needed('', 'hea')
# print number_needed('abc', 'cde')
print number_needed('tttttttttttttttttttttttttttttttttttttsssssssssssssssss', 'sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss')




# lst = [0] * 26
# print lst