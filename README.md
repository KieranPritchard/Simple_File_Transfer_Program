# Simple File Transfer Program

<div align="center">

<img alt="GitHub Created At" src="https://img.shields.io/github/created-at/KieranPritchard/Simple_File_Transfer_Program">

<img alt="GitHub License" src="https://img.shields.io/github/license/KieranPritchard/Simple_File_Transfer_Program">

<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/KieranPritchard/Simple_File_Transfer_Program">

<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/KieranPritchard/Simple_File_Transfer_Program">

<img alt="GitHub language count" src="https://img.shields.io/github/languages/count/KieranPritchard/Simple_File_Transfer_Program">

<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/KieranPritchard/Simple_File_Transfer_Program">

</div>

## Project Description

### Objective

To build a simple file transfer system using Python’s **socket** library — allowing a client to send files directly to a server. This project aims to improve understanding of network programming, data streaming, and basic file handling.

### Features

* Consists of both **client** and **server** applications.
* Allows clients to select and send any local file to a server over TCP.
* The server receives and saves the file to a chosen destination folder.
* Built with simplicity and reusability in mind.

### Technologies and Tools Used

* **Language:** Python
* **Frameworks/Libraries:** socket, os, sys
* **Tools:** Git, GitHub, VS Code

### Challenges Faced

Extracting the filename to be sent over the connection as well as the data. This lead me to finding about the basename function in the os module to extract the filename which i then build into the program by making it send the file name first to the server program and then sending out the rest of the file. Another challenge for me was understanding the sockets module better as i took some time away due to college commitments 

### Outcome

Successfully created a functioning file transfer system that demonstrates the fundamentals of Python’s networking module. Built confidence in working with sockets and handling binary data streams.

### Next Steps

Expand the project to:

* Handle multiple clients concurrently using threading.
* Add a progress bar for file upload/download visualization.
* Implement secure transfer using SSL/TLS.

## How to Use the Project

### 1. **Setup**

Ensure both `server.py` and `client.py` are in the same directory.

### 2. **Run the Server**

* Open a terminal and navigate to the project directory.
* Run:

  ```bash
  python server.py
  ```
* You’ll be prompted to enter the destination folder where received files should be saved.
* The server will then start listening for incoming connections.

### 3. **Run the Client**

* Open another terminal window in the same directory.
* Run:

  ```bash
  python client.py
  ```
* You’ll be prompted to input a **file path** for the file you wish to send.
* The client connects to the server, transfers the file name first, waits for acknowledgment, and then streams the file data.

### 4. **Transfer Process**

* The server receives the filename, acknowledges it, and starts saving the incoming data.
* Once the file transfer completes, the server confirms successful reception.
* The client prints a message confirming that the file was sent successfully.

### 5. **Closing the Programs**

* To stop the **client**, simply close the terminal after the confirmation message.
* To stop the **server**, press `Ctrl + C` in the terminal.

## Example

**Client Output**

```
Please input a file path: example.txt
File sent successfully.
```

**Server Output**

```
Server is listening on 127.0.0.1:12345
Connection established with ('127.0.0.1', 57344)
Input folder path where data is to go: C:\Downloads
Receiving file: example.txt
File successfully received and saved to C:\Downloads\example.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
