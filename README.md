**
In windows operating system, passwords saved in chrome browser are in a local database called sqlite and are encrypted using the windows API function CryptProtectData. The script client-sqlite.py will do these 4 steps:

  1- It kills all processes with the name "chrome.exe" to unlock the database.
  2- It opens the local database and pulls all the data from it.
  3- It uses CryptUnprotectData function to return the passwords in plaintext.
  4- It sends the data to the server through sockets.

The server is running on a linux machine and waiting for the data from the windows machine to be displayed once received.

**
