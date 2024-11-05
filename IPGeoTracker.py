import tkinter as tk
import requests
import folium
import webbrowser
import datetime
import os

def fetch_ip_info():
    ip_address = ip_entry.get().strip()
    
    if not ip_address:
        result_label.config(text="Please enter a valid IP address.")
        return
    
    result_label.config(text="")
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    
    if response.status_code == 200:
        data = response.json()
        
        location = f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}"
        isp = f"ISP: {data.get('org')}"
        coordinates = data.get('loc')
        
        result_label.config(text=f"{location}\n{isp}\nCoordinates: {coordinates}")
        
        with open("ip_lookup_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - IP: {ip_address}, {location}, {isp}, Coordinates: {coordinates}\n")
        
        if coordinates:
            lat, lon = map(float, coordinates.split(","))
            map_ = folium.Map(location=[lat, lon], zoom_start=10)
            folium.Marker([lat, lon], popup=f"{location}\n{isp}").add_to(map_)
            # Inside fetch_ip_info(), replace this part:
            map_file = "ip_location_map.html"
            map_.save(map_file)

            # Convert the map file to an absolute path and open it in the browser
            map_path = os.path.abspath(map_file)
            webbrowser.open("file://" + map_path)
    else:
        result_label.config(text="Error: Could not retrieve data.")

root = tk.Tk()
root.title("IP Address Tracker")
root.geometry("300x250")
root.minsize(300, 250)
root.configure(bg="#f0f0f0")

# Header Label
header_label = tk.Label(root, text="IP Address Tracker", font=("Helvetica", 16, "bold"), bg="#f0f0f0", fg="#333")
header_label.pack(pady=(10, 5))

# Frame with padding to create rounded effect
entry_frame = tk.Frame(root, bg="#cccccc", padx=5, pady=5)
entry_frame.pack(pady=(10, 5))

# Entry Field for IP Address inside the frame
ip_entry = tk.Entry(entry_frame, width=28, font=("Helvetica", 10), relief="flat")
ip_entry.pack()

# Track IP Button with bold font
track_button = tk.Button(root, text="Track IP", command=fetch_ip_info, font=("Helvetica", 10, "bold"))
track_button.pack(pady=(5, 10))

# Result Display Label
result_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f0f0", fg="#555", justify="left")
result_label.pack(pady=(10, 10))



root.mainloop()
