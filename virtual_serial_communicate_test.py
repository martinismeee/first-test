import serial
import time
import threading

# Serial port configuration
port = 'COM4'
baudrate = 9600
timeout = 1  # Timeout for read operations

# Initialize the serial port
ser = serial.Serial(port, baudrate, timeout=timeout)

def read_from_port(ser):
    while True:
        if ser.in_waiting:
            incoming_data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {incoming_data}")

def write_to_port(ser, message):
    while True:
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")
        time.sleep(1)

if __name__ == '__main__':
    try:
        # Check if the serial port is open
        if ser.isOpen():
            print(f"Port {ser.name} is open.")
        else:
            print("Failed to open the serial port. Exiting.")
            exit()

        # Create a thread for reading from port
        thread_read = threading.Thread(target=read_from_port, args=(ser,))
        thread_read.start()

        # Create a thread for writing to port
        message = "你好，世界"
        thread_write = threading.Thread(target=write_to_port, args=(ser, message))
        thread_write.start()

        # Join threads to the main thread
        thread_read.join()
        thread_write.join()

    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    finally:
        ser.close()  # Close the serial port
