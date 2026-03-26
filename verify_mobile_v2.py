import os
from playwright.sync_api import sync_playwright, expect

def main():
    os.makedirs("/home/jules/verification/video", exist_ok=True)
    with sync_playwright() as p:
        # Mobile viewport dimensions
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/video",
            viewport={"width": 390, "height": 844},
            device_scale_factor=2,
            is_mobile=True,
            has_touch=True
        )
        page = context.new_page()

        abs_path = os.path.abspath("index.html")
        page.goto(f"file://{abs_path}")

        page.wait_for_timeout(1000)

        # Scroll down slightly to demonstrate layout
        page.evaluate("window.scrollBy(0, 300)")
        page.wait_for_timeout(500)

        page.evaluate("window.scrollBy(0, -300)")
        page.wait_for_timeout(500)

        page.screenshot(path="/home/jules/verification/verification.png", full_page=False)
        page.wait_for_timeout(1000)

        context.close()
        browser.close()

if __name__ == "__main__":
    main()
