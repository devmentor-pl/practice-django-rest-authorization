from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TokenView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = request.auth
        if token is None:
            return Response({"error": "Brak tokenu"}, status=401)

        payload = token.payload
        return Response({"token_payload": payload}, status=200)
