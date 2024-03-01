import serial # импрорт библиотеки pyserial
import time # импрорт библиотеки time
import serial.tools.list_ports # импрорт модуля list_ports библиотеки pyserial

speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200'] # создание списка скоростей в бодах
ports = [p.device for p in serial.tools.list_ports.comports()] # создание списка используемых последовательных портов
port_name = ports[0] # инициализациия переменной с первым элементом в списке ports
port_speed = int(speeds[-1]) # инициализация переменной с последним элементом в списке port_speed
port_timeout = 10 # инициализация переменной со значением 10

ard = serial.Serial(port_name, port_speed, timeout = port_timeout) # создание объекта ard класса Serial c параметрами port_*
# параметр port_name передает название последовательного порта
# параметр port_speed передает скорость передачи в бодах
# параметр port_timeout устанавливает тайм-аут, по истичению которого будут возвращены все байты полученные до этого момента
time.sleep(1) # устанавлиет задержку выполнения кода на x секунд
ard.flushInput() # очищает входной буфер, удалив все его содержимое

try: # начало блока обработчика исключения
	msg_bin = ard.read(ard.inWaiting()) # cчитывает байты размера из последовательного порта
	msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
	msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
	msg_bin += ard.read(ard.inWaiting()) # добавляет cчитываемые байты размера из последовательного порта
	msg_str_ = msg_bin.decode() # возвращает байты, декодированные в строку
	print(len(msg_bin)) # вывод в консоль длины строки
except Exception as e: # при возникновении ошибки выполнится данный блок
	print('Error!') # вывод в консоль "Error!"

ard.close() # немедленно закрывает порт
time.sleep(1) # устанавливает задержку выполнения кода на x секунд
print(msg_str_) # вывод значения переменной msg_str_
