# IP Geo Tracker

The IP Geo Tracker is a Python-based application that allows users to track the geographic location, ISP, and coordinates of any public IP address. The program provides an interactive GUI to enter an IP address and displays the result in the app. Additionally, it opens a map visualization in the browser using Folium, showing the location on an interactive map. Each lookup is logged with a timestamp for reference.

## Features

- Retrieve location information (city, region, country) and ISP for any public IP address.
- Display location coordinates (latitude and longitude).
- Visualize the location on an interactive map in the browser.
- Log each lookup to a text file with timestamp and details.
- Error handling for empty inputs and failed lookups.

## Requirements

- Python 3.x
- Required libraries:
  - `tkinter` (standard with Python)
  - `requests`: To install, run `pip install requests`
  - `folium`: To install, run `pip install folium`

## Setup and Installation

1. Clone the repository or download the script file.
2. Ensure Python 3.x is installed on your machine.
3. Install the required libraries by running:
   ```bash
   pip install requests folium
   ```

## Usage

1. Run the program:
   ```bash
   python ip_address_tracker.py
   ```
2. In the application window:
   - Enter the IP address you want to look up in the text field.
   - Click the "Track IP" button.
   - The application will display location information in the window.

3. The program will:
   - Log the lookup details (IP address, location, ISP, coordinates) to `ip_lookup_log.txt`.
   - Open a map in the default web browser showing the location with a marker.

## Example Output

### Application Window

- **Displayed Information**:
  ```
  Location: Mountain View, California, US
  ISP: Google LLC
  Coordinates: 37.3860,-122.0838
  ```

### Log File (ip_lookup_log.txt)

Each lookup is recorded in the log file with a timestamp:
```
2024-11-04 15:35:20 - IP: 8.8.8.8, Location: Mountain View, California, US, ISP: Google LLC, Coordinates: 37.3860,-122.0838
```

### Map Visualization

- An interactive map opens in the browser with a marker at the specified location.

## Error Handling

- If the IP address field is left empty, the program will display a prompt to enter a valid IP address.
- If the IP address is invalid or the lookup fails, an error message will appear in the application.

## License

This project is open-source and free to use under the MIT License.

## Acknowledgements

- IP data provided by [ipinfo.io](https://ipinfo.io/)
- Mapping functionality provided by [Folium](https://python-visualization.github.io/folium/)
