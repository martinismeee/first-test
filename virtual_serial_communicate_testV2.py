import serial
import time
import threading

# Shared variable to control the thread's loop
running = True

# Serial port configuration
port = 'COM4'
baudrate = 9600
timeout = 1

# Initialize the serial port
ser = serial.Serial(port, baudrate, timeout=timeout)

def read_from_port(ser):
    global running
    while running:
        if ser.in_waiting:
            incoming_data = ser.readline().decode('utf-8').rstrip()
            print(f"Received: {incoming_data}")

def write_to_port(ser, message):
    global running
    while running:
        ser.write(message.encode('utf-8'))
        print(f"Sent: {message}")
        time.sleep(1)

if __name__ == '__main__':
    try:
        if ser.isOpen():
            print(f"Port {ser.name} is open.")
        else:
            print("Failed to open the serial port. Exiting.")
            exit()

        thread_read = threading.Thread(target=read_from_port, args=(ser,))
        thread_read.daemon = True  # Set thread as daemon
        thread_read.start()

        message = "你好，世界"
        thread_write = threading.Thread(target=write_to_port, args=(ser, message))
        thread_write.daemon = True  # Set thread as daemon
        thread_write.start()

        while True:  # Keep the main program running
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        running = False  # Signal threads to stop
        thread_read.join()  # Wait for threads to finish
        thread_write.join()
        ser.close()
