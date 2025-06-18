import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig

async def main():
    # Enhanced browser configuration for anti-bot detection
    browser_config = BrowserConfig(
        headless=True,
        user_agent_mode="random",  # Randomize user agent to avoid detection
        viewport_width=1920,       # Realistic viewport size
        viewport_height=1080,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        extra_args=[
            "--disable-gpu", 
            "--disable-dev-shm-usage", 
            "--no-sandbox",
            "--disable-blink-features=AutomationControlled",  # Hide automation
            "--disable-features=VizDisplayCompositor",
        ]
    )
    
    # Enhanced crawler configuration for JavaScript-heavy SPAs
    crawler_config = CrawlerRunConfig(
        # Wait for content to load - flexible condition for different site structures
        wait_for="js:() => (document.querySelector('#app') && document.querySelector('#app').children.length > 0) || document.querySelector('main') || document.querySelector('.content') || document.readyState === 'complete'",
        js_code=[
            "await new Promise(resolve => setTimeout(resolve, 2000));",  # Wait 2 seconds
            "window.scrollTo(0, document.body.scrollHeight);",          # Scroll to trigger loading
            "await new Promise(resolve => setTimeout(resolve, 1000));",  # Wait additional 1 second
        ],
        page_timeout=30000,  # 30 second timeout
        delay_before_return_html=3.0,  # Wait 3 seconds before extracting
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url="https://docs.hyperwallet.com/content/drop-in-uis/v2_4/overview",
            # url="https://docs.crawl4ai.com/",  # Alternative URL for testing
            config=crawler_config,
        )
        print(f"Success: {result.success}")
        print(f"Status: {result.status_code}")
        print(f"Content length: {len(result.markdown) if result.markdown else 0}")
        print("First 500 characters of extracted text:")
        print(result.markdown[:500] if result.markdown else "No content extracted")

if __name__ == "__main__":
    asyncio.run(main())
