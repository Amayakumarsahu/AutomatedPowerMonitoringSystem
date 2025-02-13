import os
import sys
import time

def find_com_port():
    if sys.platform.startswith('win'):
        for i in range(1, 256):
            port_name = f"COM{i}"
            try:
                with open(f"\\\\.\\{port_name}", "r+b") as port:
                    return port_name
            except OSError:
                pass  # Port not found or in use
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            try:
                with open(port_name, "r+b") as port:
                    return port_name
            except FileNotFoundError:
                pass
    else:
        print("Unsupported operating system.")
        return None

    return None


if __name__ == "__main__":
    com_port = find_com_port()

    if com_port:
        print(f"Found COM port: {com_port}")
        try:
            if sys.platform.startswith('win'):
                port = open(f"\\\\.\\{com_port}", "r+b")
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                port = open(com_port, "r+b")
            else:
                print("Unsupported OS")
                exit()

            port.close() # Close the port
        except OSError as e:
            print(f"Error opening port {com_port}: {e}")
    else:
        print("No COM port found.")