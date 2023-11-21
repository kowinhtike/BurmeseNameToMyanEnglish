import json
file_path = "word_data.json"
with open(file_path, "r") as json_file:
    data = json.load(json_file)

while True:
    check = input("Type burmese name : ")
    ans = check
    for d in data:
      for x in d:
          if x in ans:
              ans = ans.replace(x," "+d[x])

    print(ans)
