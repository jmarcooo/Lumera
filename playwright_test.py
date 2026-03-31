import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto('file:///app/index.html')
        await page.wait_for_timeout(2000)
        await page.screenshot(path='index_categories_sections.png', full_page=True)
        await browser.close()

asyncio.run(run())
