import re

text = "Input 1' wenas"

res = re.search("([^'])*", text)

print(res)