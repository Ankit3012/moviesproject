from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from .recommendation_service import RecommendationService
import requests
from datetime import datetime


class TMDbService:
    @staticmethod
    def fetch_movie(tmdb_id):
        url = "https://movies-and-tv-shows-api.p.rapidapi.com/movies"
        payload = {"tmdbId": tmdb_id}
        headers = {
            "x-rapidapi-key": "8770f6244dmsh1bd7a026e257ea8p1632dbjsned987d24e059",
            "x-rapidapi-host": "movies-and-tv-shows-api.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200 and 'results' in response_data:
            return response_data['results'][0]
        else:
            raise Exception("Failed to fetch movie data")


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        tmdb_id = self.request.data['tmdb_id']
        movie_data = TMDbService.fetch_movie(tmdb_id)

        # Extract the date portion from the full timestamp
        release_date_str = movie_data.get('creadetAt', '')
        if release_date_str:
            release_date = datetime.strptime(release_date_str, '%Y-%m-%dT%H:%M:%S.%f%z').date()
        else:
            release_date = None

        # Map the fetched data to your Movie model fields
        serializer.save(
            title=movie_data.get('id', ''),
            description=movie_data.get('fullUrl', ''),
            release_date=release_date,
            genre=movie_data.get('provider', ''),
            poster=movie_data.get('sourceUrlSubtitles', '')
        )


class ReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MovieRecommendationView(APIView):
    def get(self, request):
        recommended_movies = RecommendationService.recommend_movies(request.user)
        serializer = MovieSerializer(recommended_movies, many=True)
        return Response(serializer.data)
