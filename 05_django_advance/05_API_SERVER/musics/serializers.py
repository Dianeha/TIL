# 마치 forms 와 비슷함
from rest_framework import serializers
from .models import Artist, Music, Comment

class ArtistSerializer(serializers.ModelSerializer): # 마룬파이브 나올때
    class Meta:
        model = Artist
        fields = ('id', 'name', )

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ('id', 'title', 'artist_id', )

class ArtistDetailSerializer(ArtistSerializer): # 마룬파이브 노래 밑에 같이 나오도록 하기 위해 위에 것 상속
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('music_set', )

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'content', 'music_id')

class MusicDetailSerializer(MusicSerializer):
    comments = CommentSerializer(source='comment_set', many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ('comments', )