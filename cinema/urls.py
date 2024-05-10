from django.urls import path
from rest_framework.routers import DefaultRouter

from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet,
)

urlpatterns = [
    path("api/cinema/genres/", GenreList.as_view(), name="genre-list"),
    path("api/cinema/genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("api/cinema/actors/", ActorList.as_view(), name="actor-list"),
    path("api/cinema/actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("api/cinema/cinema_halls/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path(
        "api/cinema/cinema_halls/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema-hall-detail",
    ),
]

router = DefaultRouter()
router.register("api/cinema/movies", MovieViewSet, basename="movie")
urlpatterns += router.urls

app_name = "cinema"
