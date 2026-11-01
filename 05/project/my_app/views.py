from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PayloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        payload = request.auth.payload
        return Response({"token_payload": payload})
