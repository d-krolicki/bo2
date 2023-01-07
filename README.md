# Badania operacyjne 2
## Hurtownia
## Dokumentacja
https://docs.google.com/document/d/1nTYyFvVB-BnhqwKx-9pCZMtF9Uv5BPESLCRWCIge8cI/edit

### TO-DO:
1. Crossover
2. Rozbudować funkcję celu o sprawdzanie pokrycia zapotrzebowania przy zamawianiu
3. Algorytm
4. Warunki stopu algorytmu:
    - ilość iteracji,
    - ocena jakości najlepszego osobnika np. poprzez prównanie do średniej populacji(?).
5. GUI:
    - dodawanie plików .txt: hurtownie, samochody, produkty,
    - wykres funkcji celu (wartość w każdej iteracji),
    - ustawianie paramterów:
         - prawdopodobieństwo mutacji/krzyżówki,
         - liczebność populacji,
         - ilość iteracji (warunek stopu),
         - ocena jakości najlepszego osobnika (warunek stopu)(?).


### Macierz dystansów między sklepem oraz hurtowniami
s - sklep

wn - hurtownia n

         w1 w2 w3 s
    w1 [ 0  x  x  x]
    w2 [ x  0  x  x]
    w3 [ x  x  0  x]

