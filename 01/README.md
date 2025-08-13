> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{module-code}-{module-name}` (dotyczy [mentee](https://devmentor.pl/mentoring/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;


# `#01` JWT

Twoim zadaniem jest skonfigurowanie w projekcie Django REST Framework mechanizmu JWT przy użyciu biblioteki **Simple JWT** oraz utworzenie endpointu logowania zwracającego parę tokenów: **access** i **refresh**.

To ćwiczenie pozwoli Ci przećwiczyć:

* instalację i konfigurację `djangorestframework-simplejwt`,
* utworzenie endpointu `token/` zgodnego ze specyfikacją JWT,
* poprawne generowanie tokenów dla uwierzytelnionego użytkownika.

---

## Wymagania wstępne

* Działający projekt Django + DRF.
* Istniejący użytkownik w bazie (np. stworzony przez `createsuperuser`).

---

## Zakres zadania

1. **Instalacja paczki:**

   ```bash
   pip install djangorestframework-simplejwt
   ```

2. **Konfiguracja DRF – `settings.py`:**
   Dodaj JWT jako domyślną autentykację:

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework_simplejwt.authentication.JWTAuthentication',
       ],
   }
   ```
3. **Routing endpointów tokenów – `urls.py`:**


4. **(Opcjonalnie) Testowy zasób chroniony – `views.py` + `urls.py`:**

   * `views.py`:

     ```python
     from rest_framework.decorators import api_view, permission_classes
     from rest_framework.permissions import IsAuthenticated
     from rest_framework.response import Response

     @api_view(['GET'])
     @permission_classes([IsAuthenticated])
     def protected_view(request):
         return Response({'message': 'Dostęp przyznany (JWT OK).'})
     ```
   * `urls.py`:

     ```python
     from django.urls import path
     from .views import protected_view

     urlpatterns += [
         path('api/secure/', protected_view, name='secure'),
     ]
     ```

---

## Wymagania funkcjonalne

* `POST /api/token/` z poprawnymi danymi (`username`, `password`) zwraca:

  ```json
  {
    "access": "<ACCESS_TOKEN>",
    "refresh": "<REFRESH_TOKEN>"
  }
  ```
* `POST /api/token/` z błędnymi danymi zwraca `401 Unauthorized`.
* Zasób chroniony (`/api/secure/`) wymaga nagłówka:

  ```
  Authorization: Bearer <ACCESS_TOKEN>
  ```

  i zwraca `200 OK` przy poprawnym tokenie lub `401` w przeciwnym wypadku.

---

## Wskazówki

* Użyj wbudowanego `TokenObtainPairView` – nie musisz pisać własnego widoku logowania.
* W razie potrzeby dekoduj i podglądaj payload na **jwt.io** (pamiętaj, by nie udostępniać sekretnych kluczy).

---

## Testowanie

1. **Pobierz parę tokenów:**

   * `POST /api/token/`

     ```json
     { "username": "twoj_login", "password": "twoje_haslo" }
     ```
   * Odbierz `access` i `refresh`.

2. **Wywołaj zasób chroniony:**

   * `GET /api/secure/` z nagłówkiem
     `Authorization: Bearer <ACCESS_TOKEN>` → `200 OK`.

3. **Sprawdź brak autoryzacji:**

   * `GET /api/secure/` bez nagłówka lub z niepoprawnym tokenem → `401 Unauthorized`.

&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-{module-name})*

> :arrow_left: ~~*poprzednie zadanie*~~ | [*następne zadanie*](./../02) :arrow_right:
