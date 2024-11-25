# GIDORK | v1.0
**Author:** IRSYADSEC  

GIDORK is a powerful tool designed to assist cybersecurity staff in identifying compromised company websites or specific domains. The tool automates Google Dorking, analyzes links for redirects, and scans page content for specific keywords. This tool will be regularly updated to improve functionality and support the evolving needs of the cybersecurity community.


## Features
- **Google Dorking Automation**: Perform automated Google searches based on your input.
- **Redirect Detection**: Identify links that redirect to domains outside the target.
- **Keyword Analysis**: Search for specific keywords within page content.
- **HTTP Status Code Reporting**: Display the status code (e.g., 200, 404) of each checked link.


## Requirements

### **System Requirements**
- **Operating System**: Windows, macOS, or Linux.
- **Python Version**: Python 3.7 or later.
- **Browser**: Google Chrome (latest version).
- **RAM**: Minimum 2GB (to run Chrome and the script efficiently).
- **Internet Connection**: Required for Google searches and fetching web pages.

### **Python Dependencies**
The following Python libraries are required:
- **Selenium**: For browser automation.
- **Requests**: For handling HTTP requests.
- **BeautifulSoup4 (bs4)**: For parsing HTML content.

To install all dependencies, use the following command:
```bash
pip install selenium requests beautifulsoup4
```


## Usage
You can download the latest version of gidork by cloning the GitHub repository.
```bash
git clone https://github.com/IrsyadSEC/gidork.git
```

```bash
python gidork.py
```
