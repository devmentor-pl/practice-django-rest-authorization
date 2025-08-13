> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e04-django-rest-authorization` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#03` JWT: Weryfikacja integralności

**Cel:** sprawdzić, jak API reaguje na różne typy tokenów – poprawny, zmodyfikowany i przeterminowany – oraz zrozumieć rolę **podpisu** w JWT.

---

## Ważne!

💡 **Dla utrwalenia pracy z Django i DRF, za każdym razem twórz nowy projekt w osobnym katalogu dla danego zadania.**



## Zakres zadania

1. Upewnij się, że w projekcie działa endpoint do weryfikacji tokenu (`/api/token/verify/`).
2. Wygeneruj parę tokenów (`access` + `refresh`) dla zalogowanego użytkownika.
3. Przetestuj **trzy scenariusze**:

   * **Poprawny token** – wywołanie `/api/token/verify/` powinno zwrócić odpowiedź potwierdzającą ważność.
   * **Zmanipulowany token** – ręcznie zmień w nim jeden znak (np. w sekcji payload lub signature) i spróbuj ponownie go zweryfikować; oczekiwany jest błąd integralności.
   * **Przeterminowany token** – skróć czas życia `ACCESS_TOKEN_LIFETIME` w konfiguracji, wygeneruj nowy token, poczekaj aż wygaśnie i spróbuj go zweryfikować lub użyć na chronionym endpointzie; oczekiwany jest błąd o wygaśnięciu.

---

## Wymagania funkcjonalne

* **Poprawny token** – potwierdzenie ważności (status 200).
* **Zmanipulowany token** – błąd weryfikacji (status 401 lub 422 w zależności od konfiguracji).
* **Przeterminowany token** – błąd wygaśnięcia (status 401 i komunikat o nieważnym lub wygasłym tokenie).

---

## Wskazówki

* Token JWT składa się z trzech części oddzielonych kropkami: **header.payload.signature**. Zmiana nawet jednego znaku w **signature** lub **payload** powoduje błąd weryfikacji.
* W Simple JWT `TokenVerifyView` obsługuje weryfikację podpisu i daty ważności (`exp`).
* Testowanie możesz wykonać w Postmanie, curl lub interfejsie DRF.

---

## Kryteria akceptacji

* [ ] Wszystkie trzy scenariusze zostały przetestowane i ich wynik jest zgodny z oczekiwaniami.
* [ ] Kursant potrafi wyjaśnić, dlaczego zmiana tokenu powoduje błąd integralności.
* [ ] Kursant potrafi opisać różnicę między błędem integralności a błędem wygaśnięcia (`exp`).


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-authorization)*

> :arrow_left: [*poprzednie zadanie*](./../02) | [*następne zadanie*](./../04) :arrow_right:
