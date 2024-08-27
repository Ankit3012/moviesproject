# Movie Review and Recommendation API

## Project Overview

The Movie Review and Recommendation API is a Django-based application that integrates with The Movie Database (TMDb) API to manage movie data and user reviews. It provides endpoints for creating, reading, updating, and deleting movie reviews, and offers a recommendation system based on user reviews and ratings.

## Features

- **User Authentication**: Register, log in, and manage user sessions.
- **Movie Management**: Fetch and store movie information from TMDb.
- **Review Management**: Create, read, update, and delete reviews.
- **Recommendation System**: Get movie recommendations based on user reviews and ratings.
- **API Documentation**: Detailed API documentation and example requests.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- Django REST Framework
- Postman (for testing)

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Ankit3012/moviesproject
   cd moviesproject

   Create and Activate a Virtual Environment


python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
Install Dependencies


pip install -r requirements.txt
Apply Migrations


python manage.py migrate
Create a Superuser


python manage.py createsuperuser
Run the Development Server


python manage.py runserver



Register User
Endpoint: POST /api/v1/auth/register/

{
  "username": "testuser",
  "password1": "your_password",
  "password2": "your_password"
}


Log In
Endpoint: POST /api/v1/auth/login/

{
  "username": "testuser",
  "password": "your_password"
}


Get Movies
Endpoint: GET /api/v1/movies/


Create Review
Endpoint: POST /api/v1/reviews/

Headers:

Authorization: Token your_token_here
Request Body:

{
  "movie": 1,
  "rating": 5,
  "comment": "Great movie!"
}

