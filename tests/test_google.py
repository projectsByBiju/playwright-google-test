# tests/test_google.py
import pytest
import os
from playwright.sync_api import sync_playwright
headless = not os.getenv("SHOW_BROWSER")

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless) 
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        print("Google title test passed!")
        browser.close()