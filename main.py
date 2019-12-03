import serial

ser = serial.Serial('COM5', 115200)

ser.write(bytes('bin\r\n', encoding='ascii'))

while True:
    print(ser.read().hex())