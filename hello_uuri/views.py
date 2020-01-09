from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .mango.requestData import requestData
from .mango.shared import *
from .mango.transformdata import transformData
from .models import *
from django.http import JsonResponse
# Create your views here.

@csrf_exempt
def hello(request):
    rData = requestData(request)
    userId = rData.getUserId()
    print(userId)
    utterance = rData.getUtterance()
    print(utterance)
    block_name = rData.getBlockName()
    print(block_name)
    block_id = rData.getBlockId()
    print(block_id)
    
    if(ANSWER.__contains__(utterance)):
        # 답에 따른 다른 값 설정 
        answer = 0
        if utterance == ANSWER[2]:
            answer = 1
        elif utterance == ANSWER[3]:
            answer = 2
        elif utterance == ANSWER[4]:
            answer = 3
        else:
            answer = 0
        # 동작하는 사용자가 기존에 사용한 적 있는 user인지 아닌지 검사 
        # 만약 user아니면 
        user = User.objects.get(userId=userId)
        if user is None:
            user = User(userId=userId, total=0)
            user.save()
        question = Question(question=block_name, answer=answer, userId=user)
        question.save()
        if block_id == '5e173c58ffa7480001c2a095':
            total = 0
            for que in question:
                total = total + que.answer
            userTotal = User(userId=user, total=total)
            userTotal.save()
            return JsonResponse(
                {
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
                )
        else:
        # 응답 보내주기
            data = transformData(block_id).getJsonData()
    else:
        data = transformData(block_id).getJsonDumps()
    return data 

