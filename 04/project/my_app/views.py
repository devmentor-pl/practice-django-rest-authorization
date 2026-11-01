from .permissions import NoteACLPermission
from .models import Note
from .serializers import NoteSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [NoteACLPermission]


class NoteListView(ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [NoteACLPermission]

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
