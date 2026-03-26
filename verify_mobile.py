import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch()

        # Define a mobile viewport (e.g., iPhone 13 Pro)
        context = await browser.new_context(
            viewport={'width': 390, 'height': 844},
            user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
        )

        page = await context.new_page()

        # Navigate to the local file
        # Using an absolute path or file:// protocol
        import os
        filepath = f"file://{os.path.abspath('index.html')}"
        await page.goto(filepath)

        # Take a screenshot
        await page.screenshot(path='mobile.png', full_page=True)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(run())
