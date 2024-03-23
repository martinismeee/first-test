import serial
import time

# 串口配置
ser = serial.Serial(
    port='COM4',      # 串口号
    baudrate=9600,    # 波特率
    parity=serial.PARITY_NONE, # 校验位
    stopbits=serial.STOPBITS_ONE, # 停止位
    bytesize=serial.EIGHTBITS, # 数据位
    timeout=1         # 读取超时设置
)

# 检查串口是否打开
if ser.isOpen():
    print(f"串口{ser.name}已打开，准备接收数据...")
else:
    print("串口打开失败，请检查串口号及其他配置！")
    exit()

try:
    while True:
        if ser.inWaiting() > 0: # 如果串口有接收到数据
            data = ser.readline() # 读取一行数据
            print('接收到的数据:', data.decode('utf-8')) # 打印数据
        time.sleep(0.1) # 稍作延迟，减少CPU占用
except KeyboardInterrupt:
    ser.close()    # 关闭串口
    print("程序手动中断，串口已关闭。")
