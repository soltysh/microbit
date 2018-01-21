from microbit import *
from random import randint

# startowe polozenie pilki
ball_x, ball_y = 4, 4
# polozenie platformy
platform_x, platform_y = 0, 4
# pomocnicza wartosc, aby pilka spadala wolniej
counter = 0

# glowna petla programu
while True:
    # wyczysc wyswietlacz
    display.clear()

    ### obsluga pilki ###

    # pilka spada raz na 5 wykonan tej petli
    if counter%5 == 0:
        if ball_y == 4:
            # losujemy nowe polozenie pilki, kiedy pilka jest juz na dole,
            # innymi slowy y == 4
            ball_y = 0
            ball_x = randint(0, 4)
        else:
            # w przeciwnym wypadku zwiekszamy y o 1, x pozostaje bez zmian
            ball_y = ball_y + 1
        # wyswietlenie pilki
        counter = 0
    # wyswietlenie pilki za kazdym razem
    display.set_pixel(ball_x, ball_y, 9)

    # licznik petli
    counter = counter + 1

    ### obsluga platformy ###

    if button_a.was_pressed() and platform_x > 0:
        # ruch platformy w lewo przyciskiem A
        platform_x = platform_x - 1
    elif button_b.was_pressed() and platform_x < 3:
        # ruch platformy w prawo przyciskiem B
        platform_x = platform_x + 1

    # wyswietlenie platformy
    display.set_pixel(platform_x, platform_y, 9)
    display.set_pixel(platform_x+1, platform_y, 9)

    ### logika gry ###

    # kiedy pilka spadnie na dol i nie zostanie zlapana przez platforme
    # konczymy gre wyswietlajac smutna buzie
    if ball_y == 4 and platform_x != ball_x and platform_x+1 != ball_x:
        display.show(Image.SAD)
        break

    # usypiamy petle na 50ms
    sleep(50)
