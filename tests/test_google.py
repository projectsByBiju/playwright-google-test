# tests/test_google.py
import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless = works in CI
        page = browser.new_page()
        page.goto("https://www.google.com")
        assert "Google" in page.title()
        print("Google title test passed!")
        browser.close()