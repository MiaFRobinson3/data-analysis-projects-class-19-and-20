proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
has_commas = ',' in strings
if has_commas:
    print ("The list has commas")
has_semicolons = ';' in strings
if has_semicolons:
    print("The list has semicolons")
has_spaces = ' ' in strings
if has_spaces:
    print("This list has spaces")
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
new_list = proto_list1.split(',')
print(new_list)
reversed_entries = new_list[::-1]
print(reversed_entries)
new_string = (",").join(reversed_entries)
print(new_string)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
new_list2 = proto_list2.split(';')
print(new_list2)
new_list2.sort()
print(new_list2)
new_string2 = "-".join(new_list2)
print(new_string2)

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
new_list3 = proto_list3.split(' ')
print(new_list3)
new_list3.sort(reverse=True)
print(new_list3)

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
new_list4 = proto_list4.split(', ')
print(new_list4)
reversed_entries2 = new_list4[::-1]
print(reversed_entries2)
new_string4 = ",".join(reversed_entries2)
print(new_string4)