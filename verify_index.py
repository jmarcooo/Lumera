from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto(f"file://{os.path.abspath('index.html')}")
    page.wait_for_timeout(1000)
    page.screenshot(path="verification.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
