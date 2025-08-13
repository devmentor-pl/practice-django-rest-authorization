> :white_check_mark: *Jeśli będziesz mieć problem z rozwiązaniem tego zadania, poproś o pomoc na odpowiednim kanale na Slacku, tj. `s9e04-django-rest-authorization` (dotyczy [mentee](https://devmentor.pl/mentoring-javascript/)) lub na ogólnodostępnej i bezpłatnej [społeczności na Discordzie](https://devmentor.pl/discord). Pamiętaj, aby treść Twojego wpisu spełniała [odpowiednie kryteria](https://devmentor.pl/jak-prosic-o-pomoc/).*

&nbsp;
 

# `#02` JWT: Wylogowanie z blacklistą refresh tokenów (zadanie „z dokumentacją”)

**Cel:** samodzielnie, na podstawie dokumentacji **Simple JWT**, dodać mechanizm wylogowania, który **unieważnia refresh token** (blacklista), aby nie mógł posłużyć do odświeżenia access tokenu.

> To zadanie **ma sprawdzić Twoją pracę z dokumentacją** i umiejętność **zastosowania świeżo zdobytej wiedzy w praktyce**. Poniżej dostajesz jedynie **skrawki kodu** i wskazówki – kompletna implementacja jest po Twojej stronie.

---

## Wymagania wstępne

* Działające DRF + Simple JWT z endpointami:

  * `POST /api/token/` (login),
  * `POST /api/token/refresh/` (odświeżanie).
* Istnieje testowy zasób chroniony `IsAuthenticated` (np. `GET /api/secure/`).

---

## Zakres zadania

1. **Włącz blacklistę** w projekcie (moduł `token_blacklist`) i wykonaj odpowiednie **migracje**.
2. **Zaimplementuj wylogowanie**:

   * endpoint `POST /api/logout/`,
   * pobiera `refresh` z ciała żądania,
   * unieważnia go (dodaje do blacklisty),
   * zwraca odpowiedni **kod statusu** (np. `205 Reset Content` albo `200 OK` – uzasadnij wybór).
3. **Przetestuj**:

   * po wylogowaniu ten sam `refresh` nie pozwala uzyskać nowego `access` na `/api/token/refresh/` (spodziewany błąd).
   * istniejący, niewygasły `access` nadal działa do końca swojego TTL (to zachowanie standardowe).


---

## Wskazówki (co sprawdzić w dokumentacji)

* **Nazwa aplikacji** do blacklisty i gdzie ją dodać (`INSTALLED_APPS`).
* **Klasa tokenu** i metoda, która faktycznie **dodaje token do blacklisty**.
* Jakie **modele/tabele** tworzy moduł blacklisty i kiedy – czy wymagane są **migracje**?
* Jaki **kod statusu** HTTP zwrócić po udanym wylogowaniu (i **dlaczego** taki)?
* Jak **obsłużyć błędy**: brak pola `refresh`, niepoprawny/już zblacklistowany token.

> Podczas implementacji **uzasadniaj swoje decyzje** (np. wybór kodów statusu, zabezpieczeń `permission_classes`). To element sprawdzający dojrzałość pracy z dokumentacją.

---

## Kryteria akceptacji

* [ ] `POST /api/logout/` przyjmuje `{"refresh": "<token>"}` i **unieważnia** go (blacklista).
* [ ] Ponowny `POST /api/token/refresh/` z tym samym `refresh` zwraca błąd (token na czarnej liście).
* [ ] Endpoint zwraca **spójne kody statusu** (`205`/`200` dla sukcesu, `400` dla błędów wejścia).
* [ ] (Opcjonalnie) Endpoint wymaga autoryzacji (`IsAuthenticated`) – potrafisz uzasadnić wybór.

---

## Testowanie (propozycja scenariuszy)

1. **Happy path**

   * `POST /api/token/` → odbierz `access`, `refresh`.
   * `POST /api/logout/` z `refresh`.
   * `POST /api/token/refresh/` z tym samym `refresh` → błąd (blacklisted).

2. **Błędne dane**

   * `POST /api/logout/` bez pola `refresh` → `400`.
   * `POST /api/logout/` z losowym stringiem → `400`.

3. **Zastanów się nad bezpieczeństwem**

   * Czy endpoint powinien wymagać **`IsAuthenticated`**?
   * Co w logach chcesz zapisać (bezpieczeństwo vs. PII)?

---

## Materiały 

* **Simple JWT – Blacklist App** (oficjalna dokumentacja)
  [https://django-rest-framework-simplejwt.readthedocs.io/en/latest/blacklist\_app.html](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/blacklist_app.html)


&nbsp;
> :no_entry: *Jeśli nie posiadasz materiałów do tego zadania tj. **PDF, projekt + Code Review**, znajdziesz je na stronie [devmentor.pl](https://devmentor.pl/workshop-django-rest-authorization)*

> :arrow_left: [*poprzednie zadanie*](./../01) | [*następne zadanie*](./../03) :arrow_right:
