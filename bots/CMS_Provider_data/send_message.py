from AlitaPipe import AlitaPipe
import sys

def send_message(botGuid, message):
    try:
        pipe = AlitaPipe(botGuid)
        pipe.connect()
        pipe.write(message)
        pipe.write('Closing')
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")
    finally:
        pipe.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <botGuid> <message>")
        sys.exit(1)

    botGuid = sys.argv[1]
    message = sys.argv[2]

    send_message(botGuid, message)
