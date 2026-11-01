from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import NoteDetailView, NoteListView


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("notes/<int:pk>/", NoteDetailView.as_view(), name="note_detail"),
    path("notes/", NoteListView.as_view(), name="note_list"),
]
