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
radio.on()
radio.config(channel=7)

# glowna petla programu
while True:
    # wyczysc wyswietlacz
    display.clear()
    # licznik petli
    counter = counter + 1

    ### obsluga radia i pilki ###

    # jesli pilka jest na drugim microbicie
    if not ball_present:
        data = radio.receive()
        if data:
            ball_x = int(data)
            if ball_x == 99:
                display.show(Image.HAPPY)
                break
            else:
                ball_y = 0
                ball_up = False
                ball_present = True

    # jesli pilka jest na naszym microbicie
    if ball_present:
        # pilka porusza sie raz na 5 wykonan tej petli
        if counter%5 == 0:
            if ball_y >= 0 and ball_y < 4:
                # ruch pilki w gore
                if ball_up:
                    ball_y = ball_y - 1
                # ruch pilki w dol
                else:
                    ball_y = ball_y + 1
            # resetujemy licznik petli
            counter = 0
        # wyswietlenie pilki
        if ball_y >= 0:
            display.set_pixel(ball_x, ball_y, 9)
        else:
            radio.send(str(ball_x))
            ball_present = False

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
            radio.send("99")
            break

    # usypiamy petle na 50ms
    sleep(50)
