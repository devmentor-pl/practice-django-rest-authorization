> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e04-django-rest-authorization` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#05` JWT: Ręczne odczytywanie payloadu tokenu w widoku


**Cel:** nauczyć się ręcznie odczytywać informacje zapisane w **payloadzie JWT** w kodzie widoku oraz wykorzystać je w logice aplikacji.

## Zakres zadania

1. Stwórz nowy projekt Django + DRF z obsługą JWT (Simple JWT).
2. W `settings.py` upewnij się, że masz ustawioną autoryzację JWT w `REST_FRAMEWORK`.
3. Utwórz widok DRF (funkcyjny lub klasowy), który:
   - wymaga zalogowania (`IsAuthenticated`),
   - pobiera **payload tokenu** z obiektu `request.auth`,
   - zwraca go w odpowiedzi JSON (np. `{ "token_payload": { ... } }`).
4. Przetestuj zachowanie dla poprawnego i niepoprawnego tokenu.

---

## Wymagania funkcjonalne

- **Poprawny token** → widok zwraca status `200 OK` oraz JSON z pełnym payloadem tokenu.
- **Brak lub niepoprawny token** → status `401 Unauthorized`.
- Payload zawiera zarówno domyślne pola Simple JWT (`exp`, `user_id`, `token_type`), jak i dodatkowe, jeśli zostały dodane w Twoim projekcie.

---

## Wskazówki

- W Simple JWT po uwierzytelnieniu przez `JWTAuthentication`, obiekt `request.auth` zawiera zweryfikowany **payload tokenu** w postaci słownika.
- Możesz użyć tego mechanizmu do uzyskania informacji takich jak `user_id` itp.
---

## Kryteria akceptacji

- [ ] Projekt utworzony w osobnym katalogu z pełną konfiguracją JWT.
- [ ] Widok poprawnie zwraca payload tokenu w odpowiedzi JSON.
- [ ] Odpowiedź API różni się w przypadku braku lub błędnego tokenu (`401 Unauthorized`).


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-authorization)*

> :arrow_left: [*poprzednie zadanie*](./../04) | ~~*następne zadanie*~~ :arrow_right:
