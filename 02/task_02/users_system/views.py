from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "Token poprawny, dostep przyznany"}, status=200)


@api_view(["POST"])
# Tylko aktywny użytkownik z ważnym access tokenem powinien móc się wylogować
@permission_classes([IsAuthenticated])
def logout_view(request):
    refresh_token = request.data.get("refresh")
    if not refresh_token:
        return Response(
            {"message": "Refresh token wymagany"},
            status=400
        )
    token = RefreshToken(refresh_token)
    jti = token["jti"]

    # Dopisalem ten warunek, ale widze ze i tak blad automatycznie sie pojawia z informacja
    if BlacklistedToken.objects.filter(token__jti=jti).exists():
        return Response({"message": "ten token jest juz na czarnej liscie"},
                        status=400)

    token.blacklist()

    # Udalo się wykonac, uzytkownik powinien otrzymac "wyczyszona" strone
    return Response({"message": "Wylogowano uzytkownika"}, status=205)
