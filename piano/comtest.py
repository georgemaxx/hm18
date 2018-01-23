import serial
import serial.tools.list_ports
import time

print ('hello')
ports = list(serial.tools.list_ports.comports())
print (ports)

song1 = ['1','1','5','5','6','6','5','5','4','4','3','3','2','2','1','1']
song2 = ['1','2','3','1','1','2','3','1','3','4','5','3','4','5']
song3 = ['3','6','7','11','7','6','3','6','7','11','12','11','12','13']
#f = open('mysongs.csv', 'r')
#data = f.read()
#rows = data.split('\n')
#print(rows[0:5])
#row=rows[0]
#song1 = row.split(',')

for p in ports:
    print (p[1])
<<<<<<< HEAD
    if "Arduino" in p[1]:

=======
    if "USB-SERIAL CH340 (COM3)" in p[1]:
>>>>>>> c78caaab8e8b17e1446e8151649266ae0c24bf82
	    ser=serial.Serial(port=p[0])
    else :
	    print ("No Arduino Device was found connected to the computer")

#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')

def run():
    action = "empty"
    while action != "q":
        print ("No Arduino Device was found connected to the computer")
        action = input("> ")
        if action =="1":
            for notes in song1:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        elif action == "2":
            for notes in song２:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        elif action == "3":
            for notes in song3:
                ser.write(notes.encode())
                print ("send:"+notes)
                time.sleep(1)
        else :
            return

run()
