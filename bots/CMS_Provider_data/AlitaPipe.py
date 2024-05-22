import win32pipe
import win32file
import json
import os
import sys

class AlitaPipe():
    def __init__(self, botGuid):
        self.pipe = win32pipe.CreateNamedPipe(
            r'\\.\pipe\\AlitaBot-' + botGuid,
            win32pipe.PIPE_ACCESS_OUTBOUND,
            win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,
            1,
            65536,
            65536,
            0,
            None)
            
    def connect(self):
        win32pipe.ConnectNamedPipe(self.pipe, None)

    def write(self, message):
        if isinstance(message, dict):
            message = json.dumps(message)
        win32file.WriteFile(self.pipe, message.encode() + b'\n')

    def close(self):
        win32file.CloseHandle(self.pipe)

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        json_content = file.read()
        return json.loads(json_content)

def send_message(botGuid, message):
    try:
        pipe = AlitaPipe(botGuid)
        pipe.connect()
        pipe.write(message)
        pipe.write('Closing')
    except Exception as e:
        print(f"Error {e}")
    finally:
        pipe.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python script.py <botGuid> [<message>]")
        sys.exit(1)

    botGuid = sys.argv[1]

    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        directorio_actual = os.getcwd()
        json_file_path = os.path.join(directorio_actual, 'dataset', 'data.json')
        message = read_json_from_file(json_file_path)
        
    send_message(botGuid, message)
    
