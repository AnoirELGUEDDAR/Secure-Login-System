# Description:
This Python project demonstrates a simple yet secure client-server login system. It uses SQLite for user storage, SHA256 hashing for password protection, and a basic TCP socket connection for communication.
# Key Features:
### Password Hashing (SHA-256): 
Passwords are never stored in plain text. Instead, they are hashed using the secure SHA-256 algorithm. This protects user credentials in case of a database breach.
### SQLite Database:
User information (hashed passwords) is stored in a SQLite database, making it persistent across sessions.

![image](https://github.com/user-attachments/assets/6d6e6d37-2ae5-4487-a1f6-90df38efc719)

### Client-Server Model: 
Utilizes a TCP socket connection for client-server communication. The server handles authentication, and the client provides login credentials.
### Multithreading (Server):
The server uses threading to handle multiple client connections concurrently, improving responsiveness.
# How it Works:
## Server:
-Establishes a TCP socket and listens on port 9999. <br>
-When a client connects, a new thread is created to handle the login process.<br>
-The server prompts the client for a username and password.<br>
-The received password is hashed using SHA-256.<br>
-The hashed password is compared to the stored hash in the database.<br>
-The server sends a "Login successful!" or "Login failed!" message back to the client.<br>
## Client:
-Connects to the server on port 9999.<br>
-Receives prompts for username and password from the server.<br>
-Sends the entered credentials to the server.<br>
-Displays the server's response ("Login successful!" or "Login failed!").<br>
## Database Initialization (create_user.py):
-Creates a SQLite database userdata.db.<br>
-Creates a table userdata with columns id, username, and password.<br>
-Inserts sample user data with hashed passwords.<br>
# How to Use:
### Set Up Database:
Run **create_user.py** once to create the database and add sample users.
### Start Server:
Run **server.py.**
### Run Client (Multiple Times):
-Open multiple terminals.<br>
-Run client.py in each terminal.<br>
-Enter credentials for each client.<br>

![image](https://github.com/user-attachments/assets/1e4a4d4a-5482-4e40-b5c6-e074f47c4068)


![image](https://github.com/user-attachments/assets/93acff7b-cfbf-4aeb-ac99-d2947af443ff)















