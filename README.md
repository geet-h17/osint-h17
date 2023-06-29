
# OSINT h17

The OSINT h17 is a Python application that collects open-source intelligence (OSINT) information about a given URL. It retrieves data from various sources, such as the website's title, server details, IP address, and SSL certificate, and displays the results in a graphical user interface (GUI).




## Features

- Retrieves the website's title using BeautifulSoup for HTML parsing.
- Sends an HTTP request to the URL and collects the server's details and IP address.
- Retrieves the SSL certificate of the server.
- Displays the collected data in the GUI.
## Prerequisites

- Python 3.x
- Required Python packages: `tkinter`, `requests`, `beautifulsoup4`
## Installation

Clone the repository to your local machine:

```shell
git clone https://github.com/your-username/osint-h17.git
```
Navigate to the project directory:
```shell
cd osint-tool
```
Install the required Python packages using pip:
```shell
pip install -r requirements.txt
```
## Usage

Run the script:

```shell
python osint.py
```
The OSINT Tool GUI window will appear.

Enter the URL you want to collect OSINT information about in the provided input field.

Click the "Collect OSINT" button.

The tool will retrieve information from the specified URL and display the results in the GUI.
## Acknowledgements
The OSINT Tool uses the following libraries:

Tkinter - Python's de-facto standard GUI package.

Requests - HTTP library for sending requests.

BeautifulSoup - Library for parsing HTML and XML documents.


## Authors

- [@geet-h17](https://www.github.com/geet-h17)

