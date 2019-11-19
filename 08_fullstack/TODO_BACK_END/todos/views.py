from django.shortcuts import get_object_or_404

from rest_framework.response import Response # JSON 응답 생성기
from rest_framework.decorators import api_view # require_methods 와 비슷

from .models import Todo
from .serializers import TodoSerializer

# @api_view(['GET'])
# def todo_list(request):
#     serializer = TodoSerializer()

@api_view(['POST']) # POST 요청에 대해서만 동작할 것임
def create_todo(request):
    # request.POST 는 form-Data (Form 태그로 날라온 요청) 만 잡음 >> 대신 request.data 이것을 쓴다.
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(status=400, data=serializer.errors)

@api_view(['PATCH', 'DELETE'])
def update_delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'PATCH':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)
    
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)

