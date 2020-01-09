import json

class requestData:
    def __init__(self, userRequest):
        self.received_json_data = json.loads(userRequest.body.decode('utf-8'))
    def getBlockId(self):
        return self.received_json_data['userRequest']['block']['id']
    def getBlockName(self):
        return self.received_json_data['userRequest']['block']['name']
    def getUtterance(self):
        return self.received_json_data['userRequest']['utterance']
    def getUserId(self):
        return self.received_json_data['userRequest']['user']['id']
    
