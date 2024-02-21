# Monitor Pamięci RAM w Pythonie

## Opis
Projekt "Monitor Pamięci RAM" jest niewielkim narzędziem napisanym w języku Python, które pozwala monitorować zużycie pamięci RAM na Twoim systemie w czasie rzeczywistym.

## Funkcje
- Wyświetlanie bieżącego zużycia pamięci RAM w formie procentowej.
- Możliwość ustawienia progu zużycia pamięci, po przekroczeniu którego użytkownik zostanie powiadomiony.

## Wymagania
- Python 3.x
- Biblioteka psutil (do instalacji za pomocą pip: `pip install psutil`)

## Uruchamianie
1. Upewnij się, że masz zainstalowanego Pythona w wersji 3.x na swoim systemie.
2. Zainstaluj bibliotekę psutil, jeśli nie jest jeszcze zainstalowana: `pip install psutil`.
3. Uruchom skrypt `monitor_ram.py` za pomocą Pythona: `monitorpamieciram.py`.

## Użycie
1. Uruchom skrypt `monitor_ram.py`.
2. Na ekranie zostanie wyświetlone bieżące zużycie pamięci RAM.
3. Jeśli chcesz dostosować próg zużycia pamięci, edytuj zmienną `MEMORY_THRESHOLD` w pliku `monitorpamieciram.py`.

## Autor
Ten projekt został stworzony przez @Kamilq99