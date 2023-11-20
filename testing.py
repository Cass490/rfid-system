import serial

# Replace 'COMX' with the actual serial port name (e.g., COM3, /dev/ttyUSB0)
serial_port = serial.Serial('COM5', 9600, timeout=1)

try:
    while True:
        # Read data from the serial port
        data = serial_port.readline().decode().strip()

        # Process the RFID data
        if data:
            print(f"RFID Tag ID: {data}")

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    serial_port.close()
