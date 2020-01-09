from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .mango.requestData import requestData
from .mango.shared import *
from .mango.transformdata import transformData
from .models import *
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
        if utterance == ANSWER[0]:
            answer = 0
        elif utterance == ANSWER[1]:
            answer = 1
        elif utterance == ANSWER[2]:
            answer = 2
        else:
            answer = 3
        # 동작하는 사용자가 기존에 사용한 적 있는 user인지 아닌지 검사 
        # 만약 user아니면 
        user = User(userId=userId)
        user.save()
        question = Question(question=block_name, answer=answer, userId=user)
        question.save()
        # 응답 보내주기
        data = transformData(block_id, userId).getJsonData()
    else:
        data = transformData(block_id, userId).getJsonDumps()
    return data 

