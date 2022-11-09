input.onButtonPressed(Button.A, function () {
    cabeza_dino.change(LedSpriteProperty.Y, -1)
    foot_dino.change(LedSpriteProperty.Y, -1)
    basic.pause(1000)
    cabeza_dino.change(LedSpriteProperty.Y, 1)
    foot_dino.change(LedSpriteProperty.Y, 1)
})
function piedra () {
    pierda = game.createSprite(4, 4)
    for (let index = 0; index < 4; index++) {
        basic.pause(1000)
        pierda.change(LedSpriteProperty.X, -1)
        if (pierda.isTouching(foot_dino)) {
            basic.showIcon(IconNames.Sad)
            music.playMelody("C5 E A B F - - - ", 183)
            piedra()
        }
    }
}
let pierda: game.LedSprite = null
let cabeza_dino: game.LedSprite = null
let foot_dino: game.LedSprite = null
foot_dino = game.createSprite(0, 4)
cabeza_dino = game.createSprite(0, 3)
piedra()
basic.forever(function () {
    if (pierda.isTouchingEdge()) {
        basic.pause(500)
        pierda.delete()
        piedra()
    }
})
