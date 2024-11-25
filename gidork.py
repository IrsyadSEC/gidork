from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time

def google_search(query, max_results=20):
    driver = webdriver.Chrome()  
    driver.get("https://www.google.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(2)

    results = driver.find_elements(By.CSS_SELECTOR, ".tF2Cxc a")
    links = [result.get_attribute("href") for result in results[:max_results]]
    driver.quit()  
    return links

def check_redirects_and_content(links, target_domain, keyword):
    redirect_links = []
    keyword_found_links = []

    for link in links:
        try:
            response = requests.get(link, allow_redirects=True, timeout=5)
            final_url = response.url
            status_code = response.status_code  

            if urlparse(final_url).netloc != target_domain:
                redirect_links.append((link, final_url, status_code))

            if target_domain in final_url:
                soup = BeautifulSoup(response.text, 'html.parser')
                if keyword.lower() in soup.get_text().lower():
                    keyword_found_links.append((final_url, status_code))
        except requests.exceptions.RequestException:
            continue
    
    return redirect_links, keyword_found_links

if __name__ == "__main__":
    print("=============================================")
    print("                GIDORK | v1.0                ")
    print("             Author: IRSYADSEC              ")
    print("=============================================")

    target_domain = input("Enter target domain (e.g., domain.ac.id): ").strip()
    keyword = input("Enter the keyword to search for (e.g., slot): ").strip()

    query = f"site:{target_domain} intext:{keyword}"

    print("\nSearching for links on Google...")
    links = google_search(query)
    print(f"Found {len(links)} links.")

    print("\nChecking for redirects and page content...")
    redirect_links, keyword_links = check_redirects_and_content(links, target_domain, keyword)

    print("\nLinks with redirects:")
    if redirect_links:
        for original, redirected, status in redirect_links:
            print(f"Original: {original}\nRedirected: {redirected}\nStatus Code: {status}\n")
    else:
        print("No redirect links detected.")

    print("\nLinks containing the keyword:")
    if keyword_links:
        for link, status in keyword_links:
            print(f"Link: {link}\nStatus Code: {status}\n")
    else:
        print("No links containing the keyword.")
