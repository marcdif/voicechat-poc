import socket
import pyaudio

def main():
    server_ip = "0.0.0.0"  # Listen on all available interfaces
    server_port = 12345

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

    # Create a socket server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Listening for connections on {server_ip}:{server_port}")

    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connected to {client_address}")

    try:
        while True:
            audio_data = stream.read(1024)  # Capture audio
            client_socket.send(audio_data)  # Send audio to the client
    except KeyboardInterrupt:
        print("Connection closed.")
    finally:
        client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
