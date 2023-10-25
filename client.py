import socket
import pyaudio

def main():
    server_ip = "192.168.10.42"  # Server's IP
    server_port = 12345

    # Initialize PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

    # Create a socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    try:
        while True:
            audio_data = client_socket.recv(1024)  # Receive audio
            stream.write(audio_data)  # Play audio
    except KeyboardInterrupt:
        print("Connection closed.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
