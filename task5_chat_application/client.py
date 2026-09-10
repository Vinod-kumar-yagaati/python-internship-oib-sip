"""
TASK 5 · Chat Application - CLIENT (Beginner Tier)
-----------------------------------------------------
Simple chat client that connects to server.py using sockets + threading.

Checklist covered (client-side portion):
[x] Client script that connects to the server
[x] Real-time, bidirectional message exchange
[x] Messages displayed with a timestamp prefix (handled by server formatting)
[x] Graceful disconnection handling
[x] Runnable on localhost

Run (after starting server.py):
    python3 client.py
Open this in two separate terminals to simulate two users chatting.
"""

import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5050


def listen_for_messages(sock: socket.socket):
    """Background thread: continuously print incoming messages from the server."""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[Disconnected from server]")
                break
            message = data.decode("utf-8")
            # Avoid re-printing the "Enter your name" prompt after initial handshake
            print(f"\r{message}> ", end="")
        except OSError:
            break


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print(f"Could not connect to server at {HOST}:{PORT}. Is server.py running?")
        sys.exit(1)

    # Handshake: server asks for name first
    prompt = sock.recv(1024).decode("utf-8")
    name = input(prompt)
    sock.sendall(name.encode("utf-8"))

    listener = threading.Thread(target=listen_for_messages, args=(sock,), daemon=True)
    listener.start()

    print("Connected! Type your messages below (type 'exit' to quit).\n")

    try:
        while True:
            text = input("> ")
            if text.strip().lower() == "exit":
                break
            sock.sendall(text.encode("utf-8"))
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        sock.close()
        print("Disconnected.")


if __name__ == "__main__":
    main()
