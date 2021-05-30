# write your code here
with open("users.json") as json_file:
    string = json.load(json_file)

print(len(string["users"]))
