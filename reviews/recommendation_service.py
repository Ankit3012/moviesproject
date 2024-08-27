import numpy as np
from .models import Review

class RecommendationService:

    @staticmethod
    def recommend_movies(user):
        reviews = Review.objects.all()
        user_reviews = reviews.filter(user=user)

        other_reviews = reviews.exclude(user=user)
        recommended_movies = []

        for review in other_reviews:
            if not user_reviews.filter(movie=review.movie).exists():
                recommended_movies.append(review.movie)

        return recommended_movies
