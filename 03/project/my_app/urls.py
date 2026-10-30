from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]


#Dlaczego zmiana tokenu powoduje błąd integralności?
#Sygnatura jest wyliczana na podstawie header, payload i klucza na serwerze. Następnie wyliczona sygnatura jest porównywana z przesłaną sygnaturą w tokenie. Jeśli się nie zgadza, to znaczy, że jest błąd integralności, czyli ktoś zmodyfikował dowolny znak tokenu.


#Różnica między błędem integralności, a błędem wygaśnięcia.
#Błąd integralności to zmienione znaki w tokenie. Błąd wygaśnięcia, to po prostu upłynięcie czasu ważności tokena od momentu jego utworzenia(ustawionego w ACCESS_TOKEN_LIFETIME).