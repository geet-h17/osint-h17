
import tkinter as tk
import tkinter.ttk as ttk
import requests
import socket
import ssl
from bs4 import BeautifulSoup

def collect_osint():
    # Clear the previous results
    for widget in results_frame.winfo_children():
        widget.destroy()

    url = url_entry.get()

    # Collect data from various OSINT sources
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("title").text
    headers = response.headers
    ip = socket.gethostbyname(url.split("//")[-1].split("/")[0])
    ssl_cert = ssl.get_server_certificate((url.split("//")[-1].split("/")[0], 443))

    # Update the GUI with the collected data
    ttk.Label(results_frame, text=f"Title: {title}").grid(row=0, column=0, sticky="W")
    ttk.Label(results_frame, text=f"IP: {ip}").grid(row=1, column=0, sticky="W")
    ttk.Label(results_frame, text=f"Server: {headers.get('Server', 'N/A')}").grid(row=2, column=0, sticky="W")
    ttk.Label(results_frame, text=f"Content Type: {headers.get('Content-Type', 'N/A')}").grid(row=3, column=0, sticky="W")
    ttk.Label(results_frame, text=f"SSL Certificate: {ssl_cert}", wraplength=500).grid(row=4, column=0, sticky="W")

root = tk.Tk()
root.title("OSINT Tool")

url_frame = ttk.Frame(root)
url_frame.pack(pady=10)

url_label = ttk.Label(url_frame, text="URL:")
url_label.pack(side="left", padx=5)

url_entry = ttk.Entry(url_frame, width=50)
url_entry.pack(side="left")

collect_button = ttk.Button(url_frame, text="Collect OSINT", command=collect_osint)
collect_button.pack(side="left", padx=5)

results_frame = ttk.Frame(root)
results_frame.pack()

root.mainloop()
