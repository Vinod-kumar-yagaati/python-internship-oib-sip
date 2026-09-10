"""
TASK 5 · Chat Application - SERVER (Beginner Tier)
-----------------------------------------------------
Simple two-user chat server using sockets + threading.

Checklist covered (server-side portion):
[x] Server script that listens for incoming client connections
[x] Real-time, bidirectional message exchange between two connected clients
[x] Messages displayed with a timestamp prefix
[x] Graceful disconnection handling: notify the other client when one disconnects
[x] Runnable on localhost

Run: python3 server.py
Then run client.py in two separate terminals.
"""

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5050
MAX_CLIENTS = 2

clients = []          # list of (conn, addr, name)
clients_lock = threading.Lock()


def timestamp() -> str:
    return datetime.now().strftime("%H:%M")


def broadcast(message: str, sender_conn=None):
    """Send a message to every connected client except (optionally) the sender."""
    with clients_lock:
        for conn, addr, name in clients:
            if conn is sender_conn:
                continue
            try:
                conn.sendall(message.encode("utf-8"))
            except OSError:
                pass


def remove_client(conn):
    with clients_lock:
        for entry in clients:
            if entry[0] is conn:
                clients.remove(entry)
                return entry[2]
    return None


def handle_client(conn: socket.socket, addr):
    name = None
    try:
        conn.sendall(b"Enter your name: ")
        name = conn.recv(1024).decode("utf-8").strip() or f"User-{addr[1]}"

        with clients_lock:
            clients.append((conn, addr, name))

        join_msg = f"[{timestamp()}] *** {name} has joined the chat ***\n"
        print(join_msg.strip())
        broadcast(join_msg, sender_conn=conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break

            text = data.decode("utf-8").strip()
            if not text:
                continue

            formatted = f"[{timestamp()}] {name}: {text}\n"
            print(formatted.strip())
            broadcast(formatted, sender_conn=conn)

    except (ConnectionResetError, ConnectionAbortedError):
        pass
    finally:
        removed_name = remove_client(conn)
        display_name = removed_name or name or "A user"
        leave_msg = f"[{timestamp()}] *** {display_name} has disconnected ***\n"
        print(leave_msg.strip())
        broadcast(leave_msg)
        conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(MAX_CLIENTS)

    print("=" * 45)
    print("           PYTHON CHAT SERVER")
    print("=" * 45)
    print(f"Listening on {HOST}:{PORT} ... (Ctrl+C to stop)")

    try:
        while True:
            conn, addr = server.accept()
            print(f"[{timestamp()}] New connection from {addr}")
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server.close()


if __name__ == "__main__":
    main()
