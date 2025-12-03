#!/usr/bin/env python3
# iptrack.py - Simple Termux-friendly IP tracker using only ip-api.com
# Auto-installs minimal dependencies if missing.
# Developer: ARIYAN MIRZA

import os
import sys
import subprocess
import time

# --- ensure required packages are installed ---
REQUIRED = ("requests", "rich", "pyfiglet")

def ensure_packages(pkgs):
    missing = []
    for p in pkgs:
        try:
            __import__(p)
        except Exception:
            missing.append(p)
    if not missing:
        return
    print("Installing missing packages:", ", ".join(missing))
    try:
        # Use the current Python executable to run pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
    except Exception as e:
        print("Could not auto-install packages. Install manually and re-run.")
        print("Error:", e)
        sys.exit(1)

ensure_packages(REQUIRED)

# --- now safe to import ---
import requests
import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

console = Console()

# --- ASCII banner you provided ---
BANNER = r"""
╔══╗───╔════╗──────╔╗
╚╣╠╝───║╔╗╔╗║──────║║
─║║╔══╗╚╝║║╠╩╦══╦══╣║╔╦══╦═╗
─║║║╔╗║──║║║╔╣╔╗║╔═╣╚╝╣║═╣╔╝
╔╣╠╣╚╝║──║║║║║╔╗║╚═╣╔╗╣║═╣║
╚══╣╔═╝──╚╝╚╝╚╝╚╩══╩╝╚╩══╩╝
───║║
───╚╝
"""

def clear():
    try:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    except Exception:
        pass

def show_welcome():
    clear()
    # print simple title bar
    title_bar = Panel(Text(" CODING BY - ARIYAN MIRZA ", justify="center", style="bold white on black"),
                      border_style="green")
    console.print(title_bar)
    # big ascii banner (your banner)
    console.print(f"[bold green]{BANNER}[/bold green]")
    # info block like termux screenshot (developer + tool label)
    info = Table.grid(padding=(0,1))
    info.add_column(justify="right", style="bold yellow")
    info.add_column(justify="left", style="bold cyan")
    info.add_row("DEVELOPER", "> ARIYAN MIRZA")
    info.add_row("TOOL NAME", "> IP TRACKER")
    info.add_row("API", "> Contact Me (single-source)")
    console.print(Panel(info, border_style="magenta"))
    # the small WELCOME box you marked
    console.print(Align.center(Panel(Text("WELCOME", justify="center", style="bold white"),
                                     border_style="green", width=20)))
    console.print()

def show_table_ip(data):
    table = Table(title="🌍 IP Location", border_style="magenta")
    table.add_column("Info", style="bold yellow", justify="right")
    table.add_column("Details", style="bold cyan")
    table.add_row("IP Address", str(data.get("query", "N/A")))
    table.add_row("Country", str(data.get("country", "N/A")))
    table.add_row("Region", str(data.get("regionName", "N/A")))
    table.add_row("City", str(data.get("city", "N/A")))
    table.add_row("ISP", str(data.get("isp", "N/A")))
    table.add_row("Timezone", str(data.get("timezone", "N/A")))
    table.add_row("Latitude", str(data.get("lat", "N/A")))
    table.add_row("Longitude", str(data.get("lon", "N/A")))
    console.print(table)

def fetch_ip_api(ip=""):
    # ip_api only; if ip is empty ip-api will return caller's IP info
    url = f"http://ip-api.com/json/{ip}" if ip else "http://ip-api.com/json/"
    try:
        r = requests.get(url, timeout=6)
        data = r.json()
    except Exception as e:
        console.print(Panel(f"[red]Network error: {e}[/red]", border_style="red"))
        return None
    if data.get("status") == "success":
        return data
    else:
        # show message returned by api if any
        message = data.get("message", "Unknown error")
        console.print(Panel(f"[red]API error: {message}[/red]", border_style="red"))
        return None

def main():
    show_welcome()
    # prompt for ip
    ip = console.input("[bold green]Enter target IP (leave blank for your IP): [/bold green]").strip()
    if ip == "":
        console.print("[cyan]Looking up your IP via ip-api.com...[/cyan]")
    else:
        console.print(f"[cyan]Looking up {ip}  [/cyan]")
    data = fetch_ip_api(ip)
    if data:
        show_table_ip(data)
    else:
        console.print("[red]Failed to get data from ip-api.com[/red]")

if __name__ == "__main__":
    main()
