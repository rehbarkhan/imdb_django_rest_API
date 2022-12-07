from .models import Movie
from .serializers import MovieSerialser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status



@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movieSerializer = MovieSerialser(movies,many=True)
        return Response(movieSerializer.data)
    
    if request.method == "POST":
        serializer = MovieSerialser(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(["GET","PUT","DELETE"])
def specific_movie(request,pk):
    if request.method == "GET":
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerialser(movie)
            return Response(serializer.data)
        except:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "PUT":
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerialser(movie,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except:
            return Response({'error':'movie not found'})