from django.http import JsonResponse
from .shared import *
from ..models import *
from .requestData import requestData

class transformData:
    
    def __init__(self, blockId, userId):
        self.blockId = blockId
        self.userId = userId
        self.block_index = BLOCK_ID.index(blockId)
        if (len(BLOCK_ID) > self.block_index + 1):
            self.nextBlockId = BLOCK_ID[self.block_index + 1]
        else:
            self.nextBlockId = 0
        self.question = QUESTION[self.block_index]
    
    def getJsonData(self):
        if self.block_index == 5:
            questions = Question.objects.all().filter(userId=self.userId)
            total = 0
            for question in questions:
                total = total+question.answer
            userTotal = User(userId=self.userId, total=total)
            userTotal.save()
            
            data = {
                "version": "2.0",
                "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "당신의 점수는 {} 입니다.".format(str(total))
                        },
                        
                    }
                ]
            }
            }
                
        else:
            data = {
                "version": "2.0",
                "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": self.question
                        },
                        
                    }
                ],
                "quickReplies": [
            {
                "messageText": ANSWER[0],
                "action": "block",
                "blockId": self.nextBlockId,
                "label": ANSWER[0]
            },
            {
                "messageText": ANSWER[1],
                "action": "block",
                "blockId": self.nextBlockId,
                "label": ANSWER[1]
            },
            {
                "messageText": ANSWER[2],
                "action": "block",
                "blockId": self.nextBlockId,
                "label": ANSWER[2]
            },
            {
                "messageText": ANSWER[3],
                "action": "block",
                "blockId": self.nextBlockId,
                "label": ANSWER[3]
            }
            ]
            }
            }
            
        return JsonResponse(data)
    def getJsonDumps(self):
        data = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "쓰레기값."
                        }
                    }
                ]
            }
        }
        return JsonResponse(data)