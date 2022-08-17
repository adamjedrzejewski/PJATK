import serial



with serial.Serial('COM5', 9600, timeout=10) as alpha_bot:
    while True:
        alpha_bot.write(bytes("350\n", 'utf-8'))
