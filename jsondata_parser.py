import json

class JsonData_Parser():
    def parse(self, jsonStr):
        res = {}
        jsonObj = json.loads(jsonStr)
        hotComments = jsonObj['hotComments']
        for comment in hotComments:
            nickname = comment['user']['nickname']
            com = comment['content']
            res[nickname] = com
        return res