
# Python

## Zmienne

W Pythonie podobnie jak w matematyce możemy przypisać pewne wartości zmiennym.
Jedyną istotną różnicą jest możliwość przypisania zarówno wartości liczbowej:

```python
a = 1
b = 2.5
```

jak i ciągu znaków, które w żargonie programistycznym nazywają się stringami:

```python
text = "ala ma kota"
long_text = """tekst
wielolinijkowy"""
```

Ostanim typem. będą zmienne logiczne, tzn. takie którę przyjmują wartość prawda,
z angielskiego `True` oraz fałsz, z angielskiego `False`. Zwróć uwagę, że obie
wartości pisane są z wielkiej litery.

```python
b = True
```

## Działania matematyczne

Na wcześniej zdefiniowanych zmiennych (i nie tylko) można wykonać podstawowe
działania matematyczne:

```python
a = a + 1   # 2
b = b * 2   # 5
c = b - a   # 3
d = c / a   # 1.5
e = a % 5   # 1 - reszta z dzielenia
```

Tekst za znakiem `#` oznacza komentarz, tzn. fragment kodu, który jest ignorowany
przez Pythona. Wykorzystuje się go po to aby opatrzyć fragment kodu słownym
opisem szczegółowo objaśniającym jego działanie.

Niektóre z powyższych działań można także wykonać ze zmiennymi tekstowymi, tzn.
dodawnie oraz mnożenie:

```python
text = text + " oraz psa"   # ala ma kota oraz psa
text = text * 2             # ala ma kotaala ma kota
```

Zwróćcie uwagę, że w drugim przypadku nie ma znaku przerwy pomiędzy kota a ala.

## Liczby losowe

Moduł w Pythonie to fragment kodu, który został napisany przez inną osobę, a następnie
nam udostępniony. Python posiada szeroki wachlarz wbudowanych modułów, nazywa się je
biblioteką standardową. Na potrzeby dzisiejszego zadania wykorzystamy moduł `random`,
który pozwala na generowanie losowej liczby.

```python
from random import *
...
randint(a, b)
```

Funkcja `randint` zwraca losową liczbę z zakresu [a, b], włączając w to a i b.

## Kierowanie wykonaniem programu

Sterowanie programem odbywa się z użyciem dwóch podstawowych instrukcji.

### Instrukcje warunkowe `if`, `elif` i `else`

Instrukcja warunkowa wygląda następująco:

```python
if <warunek 1>:
    <ciało if>
elif <warunek 2>:
    <ciało elif>
else:
    <ciało else>
```

Zawartość instrukcji `if` (`ciało if`) wykonuje się jeśli `warunek 1` zwróci wartość
`True`. Zwróć uwagę na znak `:` za warunkiem, oraz na wymagane wcięcie `ciała if`.

```python
if a == 1:
    print("A jest jeden")
elif a == 2:
    print("A jest dwa")
else:
    print("A ma inną wartość")
```

Powyższy przykład wypisze nam tekst `A jest jeden`, tylko i wyłącznie wtedy gdy `a`
będzie miało wartość 1, `A jest dwa`, tylko i wyłącznie wtedy gdy `a` będzie miało
wartość 2, oraz `A ma inną wartość` w każdym innym przypadku, tzn. gdy `a` nie będzie
ani 1, ani 2. Podobnie można porównać ciągi znaków:

```python
if text = "ala ma kota":
    print("tekst jest zgodny")
else:
    print("nieznany tekst")
```

### Pętle `for`, `while`

Pętla `while` jest podobna do instrukcji warunkowej, ponieważ wykonuje jej `ciało`,
tak długo jak jej `warunek` zwaraca `True`:

```python
while <warunek>:
    <ciało>
```

Na przykład:

```python
while a == 1:
    print("A jest jeden")
```

Będzie wypisywało na ekranie tekst `A jest jeden` tak długo jak a będzie miało
wartość 1. W przeciwnym razie tekst nie zostanie wypisany.

Instrukcja `for` służy do "odwiedzenia" każdego elementu zbioru:

```python
for x in <zbiór>:
    <ciało>
```

Najlepiej zilustruje to przykład:

```python
for x in [1, 2, 3, 4, 5]:
    print(x)
```

Wypisze na ekranie kolejne liczby z podanego zbioru. Podobnie można "odwiedzić"
elementy ciągu znaków:

```python
for x in "tekst":
    print(x)
```

Wypisze na ekranie kolejne litery słowa `tekst`.

# Microbit

![microbit](img/microbit.gif)

## Wyświetlacz

Microbit posiada wyświetlacz 5x5 pikseli. Do obsługi wyświetlacza korzystamy ze zmiennej
`display` a do dyspozycji mamy kilka metod:

* `show(tekst|obraz)` - wyświetli tekst, bądź obrazek
* `set_pixel(x, y, jasnosc)` - zapali piksel o współrzędnych (x, y) do podanej jasności (0-9).
* `clear()` - wyczyści wyświetlacz

Poniższy kod pokazuje jak wyświetlić tekst, gotowy obrazek, lub stworzyć własny i go wyświetlić.
W tym ostatnim wypadku tworzymy pięć wierszy po pięć cyfr, gdzie każda cyfra oznacza jsność zapalenia
diody (0 - wyłączona, 9 - maksymalna jasność). Istotne są dwukropki (`:`) na końcu każdego wiersza,
gdyż one informują microbita o końcu wiersza.

```python
display.show("Hej Nikodem!")
display.show(Image.COW)
x = Image(
"90009:"
"09090:"
"00900:"
"09090:"
"90009"
)
display.show(x)
```

## Przyciski

Microbit posiada także dwa wbudowane przyciski oznaczone literami **A** i **B**. Każdy z nich posiada
swoją zmienną, która umożliwia odczytanie stanu przycisku. I tak `button_a` odpowiada przyciskowi A,
`button_b` - przyciskowi B. Do odczytania czy przycisk został naciśnięty wykorzystujemy metodę
`was_pressed`:

```python
a = button_a.was_pressed()
b = button_b.was_pressed()
```

## Akcelerometr

Kolejna funkcja Microbita pozwala na odczytanie położenia urządzenia. Do tego celu wykorzystamy zmienną
`accelerometer` w połączeniu z metodą `current_gesture`, która zwróci jedną z następujących wartości:

* `up` - urządzenie jest skierowane do góry
* `down` - urządzenie jest skierowane w dół
* `left` - urządzenie jest skierowane w lewo
* `right` - urządzenie jest skierowane w prawo
* `face up` - urządzenie jest skierowane 'twarzą' do góry
* `face down` - urządzenie jest skierowane `twarzą` w dół
* `shake` - urządzenie zostało potrząśnięte

Przykładowe wykorzystanie:

```python
accelerometer.current_gesture()
```

## Radio

Microbit pozwala na komunikację z innymi urządzeniami Microbit za pomocą wbudowanego modułu radia.
Podstawowe operacje to wysłanie i odbiór wiadomości:

```python
import radio
radio.on()              # włącza moduł radia
radio.config(channel=7) # ustawia nr kanału
radio.send("text")      # wysyła napis 'text'
text = radio.receive()  # odbiera dane
```

# Materiały zewnętrzne

Polska dokumentacja do micro:bit-a znajduje się pod adresem http://microbit-micropython.readthedocs.io/pl/latest/,
z kolei wersja angielska - https://microbit-micropython.readthedocs.io/en/latest/
