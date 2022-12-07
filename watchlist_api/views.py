from .models import Movie
from .serializers import MovieSerialser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

class MoviesList(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = MovieSerialser(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        movie_object = MovieSerialser(data=request.data)
        if movie_object.is_valid():
            movie_object.save()
            return Response(movie_object.data,status=status.HTTP_201_CREATED)
        else:
            return Response(movie_object.errors,status=status.HTTP_400_BAD_REQUEST)


class MovieUpdate(APIView):

    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serialize_data = MovieSerialser(movie)
            return Response(serialize_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'Error':'Unable to fetch the movie details'},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serialize_data = MovieSerialser(movie,data=request.data)
            if serialize_data.is_valid():
                serialize_data.save()
                return Response(serialize_data.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error':'Unable to fetch the movie details'},status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response(status=status.HTTP_301_MOVED_PERMANENTLY)
        except:
            return Response({'Error':'Unable to fetch the movie details'},status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         movieSerializer = MovieSerialser(movies,many=True)
#         return Response(movieSerializer.data)
    
#     if request.method == "POST":
#         serializer = MovieSerialser(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(["GET","PUT","DELETE"])
# def specific_movie(request,pk):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerialser(movie)
#             return Response(serializer.data)
#         except:
#             return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "PUT":
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerialser(movie,data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             else:
#                 return Response(serializer.errors)
#         except:
#             return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)

#     if request.method == "DELETE":
#         try:
#             movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response({'error':'movie not found'})