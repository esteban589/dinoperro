def on_button_pressed_a():
    cabeza_dino.change(LedSpriteProperty.Y, -1)
    foot_dino.change(LedSpriteProperty.Y, -1)
    basic.pause(1000)
    cabeza_dino.change(LedSpriteProperty.Y, 1)
    foot_dino.change(LedSpriteProperty.Y, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def piedra():
    global pierda
    pierda = game.create_sprite(4, 4)
    for index in range(4):
        basic.pause(1000)
        pierda.change(LedSpriteProperty.X, -1)
        if pierda.is_touching(foot_dino):
            basic.show_icon(IconNames.SAD)
            music.play_melody("C5 E A B F - - - ", 183)
            piedra()
pierda: game.LedSprite = None
cabeza_dino: game.LedSprite = None
foot_dino: game.LedSprite = None
foot_dino = game.create_sprite(0, 4)
cabeza_dino = game.create_sprite(0, 3)
piedra()

def on_forever():
    if pierda.is_touching_edge():
        basic.pause(1000)
        pierda.delete()
        piedra()
basic.forever(on_forever)
