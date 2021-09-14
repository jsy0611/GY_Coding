let 온도 = 0
basic.forever(function () {
    온도 = input.temperature()
    led.plotBarGraph(
    온도,
    100
    )
})
