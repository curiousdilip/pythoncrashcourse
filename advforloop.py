string = "exampleString"
List = ['apple', 'banana', 'strawberry', 'melon']

for char in string:
    print(char)

for element in List:
    print(element)

# some no. from user and seperate in into no. ans string
string = input("")
chars = ""
nums = ""
for char in string:
    if char.isdigit():
        nums = nums + char
    else:
        chars = chars + char
print(f"Characters: {chars}, Numbers: {nums}")
