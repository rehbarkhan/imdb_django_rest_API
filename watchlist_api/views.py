from .models import Watchlist,StreamPlatform
from .serializers import WatchlistSerializer,StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class StreamPlatformList(APIView):
    def get(self,request):
        stream_platfrom = StreamPlatform.objects.all()
        stream_serializer = StreamPlatformSerializer(stream_platfrom,many=True)
        return Response(stream_serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        stream_plaform = StreamPlatformSerializer(data=request.data)
        if stream_plaform.is_valid():
            stream_plaform.save()
            return Response(stream_plaform.data,status=status.HTTP_201_CREATED)
        else:
            return Response(stream_plaform.errors,status=status.HTTP_400_BAD_REQUEST)

class Watchlist(APIView):

    def get(self,request):
        movies = Watchlist.objects.all()
        serializer = WatchlistSerializer(movies,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        movie_object = WatchlistSerializer(data=request.data)
        if movie_object.is_valid():
            movie_object.save()
            return Response(movie_object.data,status=status.HTTP_201_CREATED)
        else:
            return Response(movie_object.errors,status=status.HTTP_400_BAD_REQUEST)


class WatchlistUpdate(APIView):

    def get(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
            serialize_data = WatchlistSerializer(movie)
            return Response(serialize_data.data,status=status.HTTP_200_OK)
        except:
            return Response({'Error':'Unable to fetch the movie details'},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
            serialize_data = WatchlistSerializer(movie,data=request.data)
            if serialize_data.is_valid():
                serialize_data.save()
                return Response(serialize_data.data,status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serialize_data.errors,status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'Error':'Unable to fetch the movie details'},status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,pk):
        try:
            movie = Watchlist.objects.get(pk=pk)
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