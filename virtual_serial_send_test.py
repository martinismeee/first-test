import serial
import time

# Configure the serial connection
ser = serial.Serial(
    port='COM4',     # Your COM port may vary
    baudrate=9600,   # Baud rate (you can change this according to your needs)
    timeout=1        # Timeout for read operations (you can adjust this)
)

# Check if the serial port is open
if ser.isOpen():
    print(f"Port {ser.name} is open. Now sending '你好，世界' every second.")
else:
    print("Failed to open the serial port. Check your port name and make sure it's not in use.")
    ser.close()
    exit()

try:
    while True:
        # Encode the string to bytes and send it to the serial port
        ser.write('你好，世界'.encode('utf-8'))
        print("Sent '你好，世界'")
        time.sleep(1)  # Wait for 1 second before sending the next message
except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    ser.close()  # Close the serial port
