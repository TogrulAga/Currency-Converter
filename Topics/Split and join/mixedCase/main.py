string = input().split()

print(string[0].lower() + "".join([word.capitalize() for word in list(string[1:])]))
