import asyncio
from datetime import datetime

from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator


async def crawl_sequential(urls: list[str]):
    print("\n=== Sequential Crawling with Session Reuse ===")

    # Generate timestamp-based filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"crawled_docs_{timestamp}.md"

    # Enhanced browser configuration for anti-bot detection
    browser_config = BrowserConfig(
        headless=True,
        user_agent_mode="random",  # Randomize user agent to avoid detection
        viewport_width=1920,  # Realistic viewport size
        viewport_height=1080,
        headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        },
        # For better performance in Docker or low-memory environments + anti-bot detection:
        extra_args=[
            "--disable-gpu",
            "--disable-dev-shm-usage",
            "--no-sandbox",
            "--disable-blink-features=AutomationControlled",  # Hide automation
            "--disable-features=VizDisplayCompositor",
        ],
    )

    # Enhanced crawler configuration for JavaScript-heavy SPAs
    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(),
        # Wait for content to load - flexible condition for different site structures
        wait_for="js:() => (document.querySelector('#app') && document.querySelector('#app').children.length > 0) || document.querySelector('main') || document.querySelector('.content') || document.readyState === 'complete'",
        js_code=[
            "await new Promise(resolve => setTimeout(resolve, 2000));",  # Wait 2 seconds
            "window.scrollTo(0, document.body.scrollHeight);",  # Scroll to trigger loading
            "await new Promise(resolve => setTimeout(resolve, 1000));",  # Wait additional 1 second
        ],
        page_timeout=30000,  # 30 second timeout
        delay_before_return_html=3.0,  # Wait 3 seconds before extracting
    )

    # Create the crawler (opens the browser)
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        session_id = "session1"  # Reuse the same session across all URLs
        crawled_content = []

        for url in urls:
            result = await crawler.arun(url=url, config=crawl_config, session_id=session_id)
            if result.success:
                print(f"Successfully crawled: {url}")
                markdown_content = (
                    result.markdown.raw_markdown
                    if hasattr(result.markdown, "raw_markdown")
                    else result.markdown
                )
                print(f"Markdown length: {len(markdown_content)}")

                # Add URL header and content to the list
                page_content = f"# {url}\n\n{markdown_content}"
                crawled_content.append(page_content)
            else:
                print(f"Failed: {url} - Error: {result.error_message}")

        # Save all content to file with separators
        if crawled_content:
            try:
                with open(output_filename, "w", encoding="utf-8") as file:
                    file.write("\n\n---\n\n".join(crawled_content))
                print(f"\nCrawled content saved to: {output_filename}")
                print(f"Total pages crawled: {len(crawled_content)}")
            except OSError as e:
                print(f"Error saving file: {e}")
        else:
            print("No content was successfully crawled.")

    finally:
        # After all URLs are done, close the crawler (and the browser)
        await crawler.close()


def get_docs_urls():
    urls = []

    try:
        with open("./links.txt") as file:
            for line in file:
                url = line.strip()  # Remove whitespace and newline characters
                if url:  # Only add non-empty lines
                    urls.append(url)
    except FileNotFoundError:
        print("Error: links.txt file not found")
    except OSError:
        print("Error: Could not read the links.txt file")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return urls


async def main():
    urls = get_docs_urls()
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        await crawl_sequential(urls)
    else:
        print("No URLs found to crawl")


if __name__ == "__main__":
    asyncio.run(main())
