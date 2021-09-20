from selenium import webdriver

browser = webdriver.Safari()
browser.get('http://localhost:8000')

assert 'work' in browser.title
