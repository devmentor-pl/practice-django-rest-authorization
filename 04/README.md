> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `{module-code}-{module-name}` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;

# `#04` JWT: Prosty helper ACL (Access Control List)


**Cel:** poznać i zastosować w praktyce podstawy kontroli dostępu opartej na logice w Pythonie i klasach uprawnień DRF.


## Wprowadzenie

ACL (*Access Control List*) to mechanizm kontroli dostępu, który pozwala decydować, **kto** i **jakie akcje** może wykonać na danym zasobie.  
W kontekście Django REST Framework oznacza to np. określenie, czy dany użytkownik może edytować lub usuwać konkretny obiekt.

📚 **Do poczytania przed rozpoczęciem:**  
- Oficjalna dokumentacja DRF — *Custom permissions*:  
  https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions  
- Wprowadzenie do ACL w aplikacjach webowych:  
  https://en.wikipedia.org/wiki/Access-control_list


## Zakres zadania

1. Stwórz nowy projekt Django + DRF z obsługą JWT (Simple JWT).
2. Utwórz aplikację z prostym modelem, np. `Note` (pole `owner` typu ForeignKey do `User`, oraz np. `title` i `content`).
3. Zaimplementuj **helper ACL** w osobnym pliku, np. `acl.py`.  
   Funkcja powinna przyjmować użytkownika, obiekt i typ akcji (np. `'read'`, `'update'`, `'delete'`) i zwracać `True` lub `False`.
4. Utwórz **niestandardową klasę uprawnień** (`BasePermission`), która w metodzie `has_object_permission()` korzysta z tego helpera.
5. Podepnij tę klasę do widoku DRF (np. `RetrieveUpdateDestroyAPIView`).
6. Skonfiguruj routing tak, aby móc pobierać, aktualizować i usuwać obiekty.
7. Przetestuj różne scenariusze:
   - Właściciel obiektu wykonuje akcję → dostęp przyznany.
   - Inny zalogowany użytkownik wykonuje akcję → dostęp zabroniony (`403 Forbidden`).
   - Użytkownik niezalogowany próbuje wykonać akcję → `401 Unauthorized`.

---

## Wymagania funkcjonalne

- **Odczyt (`GET`)** – dozwolony tylko dla właściciela (lub zgodnie z Twoją polityką w helperze).
- **Edycja i usuwanie (`PUT`, `PATCH`, `DELETE`)** – tylko właściciel.
- **Tworzenie (`POST`)** – dozwolone dla każdego zalogowanego użytkownika.

---

## Kryteria akceptacji

- [ ] Projekt działa w osobnym katalogu, z pełną konfiguracją JWT.
- [ ] Helper ACL poprawnie decyduje o dostępie na podstawie użytkownika i akcji.
- [ ] Klasa uprawnień DRF korzysta z helpera i blokuje/zezwala na dostęp zgodnie z logiką.
- [ ] Testy potwierdzają, że różni użytkownicy otrzymują różne kody odpowiedzi (`200/403/401`) w zależności od sytuacji.


&nbsp;

> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-{module-name})*

> :arrow_left: [*poprzednie zadanie*](./../03) | [*następne zadanie*](./../05) :arrow_right:
