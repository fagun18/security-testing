import requests
import json

def test_sql_injection(url):
    # Test for SQL injection vulnerability
    payload = {"username": "' OR '1'='1", "password": "password"}
    response = requests.post(url, data=payload)

    if "error" in response.text:
        print("SQL injection vulnerability found.")
    else:
        print("No SQL injection vulnerability found.")

def test_xss(url):
    # Test for cross-site scripting (XSS) vulnerability
    payload = {"comment": "<script>alert('XSS')</script>"}
    response = requests.post(url, data=payload)

    if "<script>" in response.text:
        print("XSS vulnerability found.")
    else:
        print("No XSS vulnerability found.")

def test_csrf(url):
    # Test for cross-site request forgery (CSRF) vulnerability
    cookies = {"session_id": "12345"}
    headers = {"Referer": "http://attacker.com"}
    payload = {"username": "new_username"}
    response = requests.post(url, cookies=cookies, headers=headers, data=payload)

    if "username changed" in response.text:
        print("CSRF vulnerability found.")
    else:
        print("No CSRF vulnerability found.")

def test_ssl_validation(url):
    # Test for SSL certificate validation
    try:
        requests.get(url, verify=True)
        print("SSL certificate is valid.")
    except requests.exceptions.SSLError:
        print("SSL certificate validation failed.")

if __name__ == '__main__':
    url = "https://example.com"
    test_sql_injection(url)
    test_xss(url)
    test_csrf(url)
    test_ssl_validation(url)
