import sys
import re
import time
import telnetlib

def main():
        print ("Conecting with OLT....")

        'foo'.encode('utf-8') # using UTF-8; replace w/ the encoding expected by the remote device
        b'foo'

        user = "user"
        passwd = "password"

        tn = telnetlib.Telnet("192.168.1.11", "23")
        tn.read_until(b"Username: ")
        tn.write(b"user\r\n")
        tn.read_until(b"Password: ")
        tn.write(b"password\r\n")
        tn.read_until(b"OLT8E> ")
        print ("OLT Connected.")
        tn.write(b"enable\r\n")
        tn.read_until(b"OLT8E# ")
        tn.write(b"config term\r\n")
        tn.read_until(b"OLT8E(config)# ")
        #nos conectamos al PON1
        tn.write(b"interface gpon-olt 1/1\r\n")
        tn.read_until(b"OLT8E(config-gpon-olt1/1)# ")
        #Se procede a borrar las ONUs
        print ("Deletings ONUs....")
        for i in range (1, 128):
                str_command = "no onu " + str (i)
                tn.write(str.encode(str_command) + b"\r\n")     #str.encode(str_command) --> covierte un type 'str' a 'bytes'. Por otra parte la cadena 'b"\r\n"' debe enviarse con la opcion 'b'
                time.sleep(2)                                   #hay que darle dos segundos entre comando y comando
        #nos salimos de gpon1/1
        time.sleep(2)
        tn.write(b"exit\r\n")
        #nos conectamos al PON2
        tn.read_until(b"OLT8E(config)# ")
        tn.write(b"interface gpon-olt 1/2\r\n")
        tn.read_until(b"OLT8E(config-gpon-olt1/2)# ")
        #Se procede a borrar las ONUs
        print ("Deletings ONUs....")
        for i in range (1, 128):
                str_command = "no onu " + str (i)
                tn.write(str.encode(str_command) + b"\r\n")     #str.encode(str_command) --> covierte un type 'str' a 'bytes'. Por otra parte la cadena 'b"\r\n"' debe enviarse con la opcion 'b'
                time.sleep(2)                                   #hay que darle dos segundos entre comando y comando
        #nos salimos de gpon1/2
        time.sleep(2)
        tn.write(b"exit\r\n")
        #Cerramos sesion Telnet
        time.sleep(1)
        print ("ONUs deleted.")
        tn.close()
        print ("Connection with OLT closed.")



if __name__ == '__main__':
        main()
