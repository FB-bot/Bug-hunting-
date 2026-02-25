from playwright.async_api import async_playwright

async def take(url):

    async with async_playwright() as p:
        browser=await p.chromium.launch()
        page=await browser.new_page()

        await page.goto(url)

        await page.screenshot(path="reports/screenshot.png")

        await browser.close()
