from microbit import *
import radio

# startowe polozenie pilki
ball_x, ball_y = 2, 0
# informacja czy pilka porusza sie w dol czy w gore
ball_up = False
ball_present = True
# polozenie platformy
platform_x, platform_y = 1, 4
# pomocnicza wartosc, aby pilka spadala wolniej
counter = 0
# wlacz i skonfiguruj radio
# ???

# glowna petla programu
while True:
    # wyczysc wyswietlacz
    display.clear()
    # licznik petli
    counter = counter + 1

    ### obsluga radia i pilki ###

    # ???

    ### obsluga platformy ###

    if button_a.was_pressed() and platform_x >= 0:
        # ruch platformy w lewo przyciskiem A
        platform_x = platform_x - 1
    elif button_b.was_pressed() and platform_x < 3:
        # ruch platformy w prawo przyciskiem B
        platform_x = platform_x + 1

    # wyswietlenie platformy
    if platform_x >= 0:
        display.set_pixel(platform_x, platform_y, 9)
    display.set_pixel(platform_x+1, platform_y, 9)
    if platform_x < 3:
        display.set_pixel(platform_x+2, platform_y, 9)

    ### logika gry ###

    if ball_y == 4:
        # kiedy pilka spadnie na dol na platforme musi zostac odbita
        if ball_x >= platform_x and ball_x <= platform_x+2:
            ball_up = True
            ball_y = ball_y - 1
        # w przeciwnym razie konczymy gre
        else:
            display.show(Image.SAD)
            break

    # usypiamy petle na 50ms
    sleep(50)
