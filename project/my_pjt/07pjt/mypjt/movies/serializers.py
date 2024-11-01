from rest_framework import serializers
from .models import Actor, Movie, Review

class ActorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializers(serializers.ModelSerializer):
    class MovieTitleSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)

    movies = MovieTitleSerializers(read_only=True, many=True)

    class Meta:
        model = Actor
        fields = '__all__'
        

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content',)

class MovieSerializers(serializers.ModelSerializer):
    class ActorNameSerializers(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = ('name', )

    actors = ActorNameSerializers(read_only=True, many=True)

    review_set = ReviewListSerializers(read_only=True, many=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class MovieTitleSerializers(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('title',)
    
    movie = MovieTitleSerializers(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class MovieSearchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'release_date', 'poster_path',)