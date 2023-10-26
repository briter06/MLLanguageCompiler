import re
import json


class Tokenizer():
    def __init__(self):
        self.data = json.load(open('regex.json'))

    def tokenize(self, text):
        val = 0
        result = []
        while len(text) != 0:
            found = False
            for reg in self.data.keys():
                res = re.search(self.data[reg]['regex'], text)
                if res:
                    start, end = res.span()
                    # if reg == "FreeText_Token":
                    #     print(text)
                    #     print(start)
                    #     print(end)
                    #     print("=============")
                    if start == 0 and len(res.group().strip()) != 0:
                        lexema = res.group().strip()
                        transform = res.group().index(lexema)
                        start = start+transform
                        token = self.data[reg]['value']
                        result.append([lexema, reg, token, val])
                        val += end
                        text = text[end:]
                        text = text.strip()
                        found = True
                        break
            if found == False:
                result = []
                break
        return [result, text]
