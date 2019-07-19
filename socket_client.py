import telnetlib

tn = telnetlib.Telnet('127.0.0.1', 9004, 15)
tn.write('teste'.encode('utf-8'))
