import sqlite3
import hashlib
import socket
import threading


def handle_connection(c):
    try:
        c.send("Username: ".encode())
        username = c.recv(1024).decode().strip()
        c.send("Password: ".encode())
        password = c.recv(1024).strip()
        password = hashlib.sha256(password).hexdigest()

        conn = sqlite3.connect("userdata.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM userdata WHERE username=? AND password=?", (username, password))
        if cur.fetchone():
            c.send("Login successful!".encode())
        else:
            c.send("Login failed!".encode())
        conn.close()
    except Exception as e:
        print(f"Error handling connection: {e}")
    finally:
        c.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen()

print("Server is listening on port 9999...")

while True:
    client, addr = server.accept()
    print(f"Connection from {addr} has been established.")
    threading.Thread(target=handle_connection, args=(client,)).start()
