# crawl4ai-docs-scraper

A Python documentation scraper using crawl4ai with JavaScript SPA support and anti-bot detection bypass.

## 🚀 Features

- **JavaScript SPA Support**: Handles modern single-page applications with dynamic content loading
- **Anti-Bot Detection**: Bypasses common bot detection mechanisms with stealth browsing
- **Session Reuse**: Efficient crawling with persistent browser sessions
- **Flexible Content Detection**: Smart waiting conditions for different site structures
- **Sequential Processing**: Crawl multiple URLs with optimized performance
- **Markdown Output**: Clean, structured markdown extraction
- **Modern Python**: Built with Python 3.10+ and modern async/await patterns

## 📋 Requirements

- Python 3.10+
- crawl4ai
- playwright

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/LeonidShamis/crawl4ai-docs-scraper.git
   cd crawl4ai-docs-scraper
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install playwright browsers** (required for crawl4ai):
   ```bash
   crawl4ai-setup
   ```
   or 

   ```bash
   playwright install
   ```

## 🎯 Usage

### Single URL Crawling

Use `simple_crawl.py` for testing individual URLs or one-off crawling:

```bash
python simple_crawl.py
```

**Features**:
- Quick single-URL testing
- Immediate console output
- Easy URL modification in code
- Perfect for development and debugging

### Batch URL Crawling

Use `crawl_docs_sequential.py` for comprehensive automated scraping of multiple URLs:

```bash
python crawl_docs_sequential.py
```

**Features**:
- Reads URLs from `links.txt`
- Session reuse for efficiency
- Timestamped output files (`crawled_docs_YYYYMMDD_HHMMSS.md`)
- Progress tracking and error handling
- Comprehensive markdown compilation

### Configuration

The project includes a sample `links.txt` with **PayPal Hyperwallet documentation URLs** as a reference use case:

- Drop-in UIs v2.4 overview and authentication
- Transfer method setup and configuration
- Payee verification workflows
- Styling and customization options
- Event handling and webhooks

To use your own URLs, simply edit `links.txt` with one URL per line.

## 🔧 Code Quality

The project includes **Ruff** for comprehensive linting and formatting:

```bash
# Check code for issues
ruff check .

# Auto-fix issues
ruff check . --fix

# Format code
ruff format .

# Complete cleanup
ruff check . --fix && ruff format .
```

## 🏗️ Architecture

### Browser Configuration
- **Stealth Mode**: Random user agents and anti-automation flags
- **Realistic Headers**: Mimics genuine browser requests
- **Optimized Performance**: Docker-compatible flags for various environments

### JavaScript Handling
- **Smart Waiting**: Flexible conditions for different site structures (`#app`, `main`, `.content`)
- **Dynamic Content**: Waits for JavaScript execution and content loading
- **Scroll Triggering**: Simulates user interaction to trigger lazy loading

### Session Management
- **Persistent Sessions**: Reuses browser instances across multiple URLs
- **Error Recovery**: Robust error handling with detailed logging
- **Resource Cleanup**: Proper session cleanup and memory management

## 📁 Project Structure

```
crawl4ai-docs-scraper/
├── simple_crawl.py              # Single URL crawler
├── crawl_docs_sequential.py     # Batch URL crawler
├── links.txt                    # Sample URLs (Hyperwallet docs)
├── requirements.txt             # Python dependencies
├── ruff.toml                    # Linting configuration
├── .gitignore                   # Git exclusions
└── README.md                    # This file
```

## 🎨 Output Format

Crawled content is saved as clean markdown with:
- URL headers for each page
- Properly formatted content structure
- Separator lines between pages
- UTF-8 encoding for international content

Example output structure:
```markdown
# https://docs.example.com/page1

[Page 1 content in markdown]

---

# https://docs.example.com/page2

[Page 2 content in markdown]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run linting: `ruff check . --fix && ruff format .`
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [crawl4ai](https://github.com/unclecode/crawl4ai) - Advanced web crawling framework
- Uses [Playwright](https://playwright.dev/) for browser automation

## ⚠️ Disclaimer

This tool is intended for legitimate documentation crawling and research purposes. Always respect website terms of service and robots.txt files. Use responsibly and in compliance with applicable laws and regulations.