# https://github.com/coleam00/ottomator-agents/blob/main/crawl4AI-agent/crawl4AI-examples/2-crawl_docs_sequential.py

import asyncio
from typing import List
from datetime import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
import requests
from xml.etree import ElementTree

async def crawl_sequential(urls: List[str]):
    print("\n=== Sequential Crawling with Session Reuse ===")

    # Generate timestamp-based filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"crawled_docs_{timestamp}.md"
    
    browser_config = BrowserConfig(
        headless=True,
        # For better performance in Docker or low-memory environments:
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )

    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator()
    )

    # Create the crawler (opens the browser)
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        session_id = "session1"  # Reuse the same session across all URLs
        crawled_content = []
        
        for url in urls:
            result = await crawler.arun(
                url=url,
                config=crawl_config,
                session_id=session_id
            )
            if result.success:
                print(f"Successfully crawled: {url}")
                print(f"Markdown length: {len(result.markdown.raw_markdown)}")
                
                # Add URL header and content to the list
                page_content = f"# {url}\n\n{result.markdown.raw_markdown}"
                crawled_content.append(page_content)
            else:
                print(f"Failed: {url} - Error: {result.error_message}")
        
        # Save all content to file with separators
        if crawled_content:
            try:
                with open(output_filename, 'w', encoding='utf-8') as file:
                    file.write("\n\n---\n\n".join(crawled_content))
                print(f"\nCrawled content saved to: {output_filename}")
                print(f"Total pages crawled: {len(crawled_content)}")
            except IOError as e:
                print(f"Error saving file: {e}")
        else:
            print("No content was successfully crawled.")
            
    finally:
        # After all URLs are done, close the crawler (and the browser)
        await crawler.close()

def get_docs_urls():
    urls = []
    
    try:
        with open("./links.txt", "r") as file:
            for line in file:
                url = line.strip()  # Remove whitespace and newline characters
                if url:  # Only add non-empty lines
                    urls.append(url)
    except FileNotFoundError:
        print("Error: links.txt file not found")
    except IOError:
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