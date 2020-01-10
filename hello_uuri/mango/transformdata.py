from django.http import JsonResponse
from .shared import *
from ..models import *
from .requestData import requestData

class transformData:
    
    def __init__(self, blockId, user):
        self.blockId = blockId
        self.user = user
        self.block_index = BLOCK_ID.index(blockId)
        if (len(BLOCK_ID) > self.block_index + 1):
            self.nextBlockId = BLOCK_ID[self.block_index + 1]
        else:
            self.nextBlockId = 0
        self.question = QUESTION[self.block_index]
    
    def getJsonData(self):
        if self.block_index == 5:
            total = 0
            user = self.user
            questions = Question.objects.all().filter(userId=user)
            for question in questions:
                total = total + question.answer
            userTotal = User.objects.all().filter(userId=user)
            userTotal.total = total
            userTotal.save()
            data = {
                "version": "2.0",
                "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "점수는 {} 입니다.".format(str(total))
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
                "messageText": "완전 좋아",
                "action": "block",
                "blockId": self.nextBlockId,
                "label": "완전 좋아"
            },
            {
                "messageText": "괜찮아",
                "action": "block",
                "blockId": self.nextBlockId,
                "label": "괜찮아"
            },
            {
                "messageText": "별로야",
                "action": "block",
                "blockId": self.nextBlockId,
                "label": "별로야"
            },
            {
                "messageText": "대박 싫어",
                "action": "block",
                "blockId": self.nextBlockId,
                "label": "대박 싫어"
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