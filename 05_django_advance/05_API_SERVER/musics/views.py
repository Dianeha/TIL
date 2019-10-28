from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Artist, Music, Comment
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer

from IPython import embed
# 달라  써라    수정   삭제
# Read  Create Update Delete
# GET   POST   PATCH  DELETE

@api_view(['GET'])
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)
    # dataset = []
    # for artist in artists:
    #     d = {
    #         "id": artist.id,
    #         "name": artist.name
    #     }
    #     dataset.append(d)
    
    # # 딕셔너리나 리스트는 파이썬 세상에만 있다. 웹세상의 공용어 == string 로 바꾼다 (Serialization 직렬화)
    # # json 형태의 string으로 보내야 해
    # res_data = json.dumps(dataset)
    # print(type(res_data), res_data)
    # return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def music_detail(request, music_id):
    musics = get_object_or_404(Music, id=music_id)
    ser = MusicDetailSerializer(musics)
    return Response(ser.data)

@api_view(['POST'])
def create_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)

    ser = CommentSerializer(data=request.data) # request.POST vs request.data
    if ser.is_valid(raise_exception=True):
        ser.save(music_id=music.id) # 저장 완료
    return Response(ser.data) # 저장한 데이터