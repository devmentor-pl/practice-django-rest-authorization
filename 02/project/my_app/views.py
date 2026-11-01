from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({'detail': "Dostęp przyznany (JWT OK)."})


@api_view(["POST"])
def logout_view(request):

    refresh_token = request.data.get(
        "refresh") if isinstance(request.data, dict) else None

    if not refresh_token:
        return Response(
            {"detail": "Pole refresh jest wymagane."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    try:
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"detail": "Pomyślnie wylogowano."}, status=status.HTTP_200_OK)

    except TokenError:
        return Response({"detail": "Token jest nieważny lub wygasł"}, status=status.HTTP_400_BAD_REQUEST)


# 200 vs 205?
# Wybrałem 200, bo chcę zwracać body. Wybrałbym 205, gdybym nie chciał zwracać body. Zwrócenie body w 205 to złamanie konwencji, ponieważ ten kod został stworzony, aby poinformować o konieczności wyczyszczenia widoku bez zwracania body.


# Czy endpoint powinien wymagać IsAuthenticated?
# Nie, bo unieważnienie refresh tokena został by niepotrzebnie utrudnione. W razie wygaśnięcia access tokena, musiałbym najpierw utworzyć nowy access token i dopiero zblacklistować refresh token. Po unieważnieniu refreshtoken haker ma jeszcze możliwość korzystać z accesss tokena, aż do końca jego czasu ważności.


# Co w logach chcesz zapisać (bezpieczeństwo vs. PII)?
# Należy logować informacje potrzebne do wykrycia problemów i ataków. Nie należy logować danych osobowych ani sekretów. Można: data, godzina, typ zdarzenia. Nie zaleca się: email, imię, nazwisko. Nie można: tokeny, api key.
