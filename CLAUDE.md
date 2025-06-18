# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Environment Setup
```bash
# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install playwright browsers (required for crawl4ai)
playwright install
```

### Running the Project
```bash
# Run the main crawling script
python crawl_docs_sequential.py
```

### Project Overview
This is a Python-based web scraping project designed to crawl and extract documentation from Hyperwallet's documentation website. The codebase uses the `crawl4ai` library to perform sequential web crawling of documentation pages, converting the content to markdown format for further processing or analysis.

## Project Structure

### Root Directory: `/mnt/ssd/ai/web-scraping/for-ai/`

```
/mnt/ssd/ai/web-scraping/for-ai/
├── crawl_docs_sequential.py    # Main crawling script
├── links.txt                   # List of URLs to crawl
├── requirements.txt            # Python dependencies
├── venv/                      # Python virtual environment
└── .claude/                   # Claude-specific directory
```

## Key Directories and Their Purposes

### `/venv/` - Virtual Environment
- **Purpose**: Contains the isolated Python environment for this project
- **Python Version**: 3.10.12
- **Structure**: Standard Python virtual environment with `bin/`, `lib/`, `include/` directories
- **Configuration**: Located in `venv/pyvenv.cfg`

### `/.claude/` - Claude Configuration
- **Purpose**: Directory for Claude-specific configurations and files
- **Contents**: Currently empty but reserved for Claude Code usage

## Main Programming Languages and Frameworks

### Python 3.10.12
- **Primary Language**: Python
- **Runtime**: Python 3.10.12

### Key Dependencies (from requirements.txt)
1. **crawl4ai** - Main web crawling framework
   - Provides `AsyncWebCrawler` for asynchronous web crawling
   - Includes `BrowserConfig` for browser configuration
   - Uses `DefaultMarkdownGenerator` for content conversion
   
2. **playwright** - Browser automation library
   - Used by crawl4ai for browser control
   - Handles headless browser operations

### Additional Libraries Used
- **asyncio** - For asynchronous programming
- **requests** - HTTP library (imported but not actively used in current code)
- **xml.etree.ElementTree** - XML parsing (imported but not actively used)

## Configuration Files

### `requirements.txt`
- **Purpose**: Python package dependencies
- **Build System**: Standard pip requirements file
- **Dependencies**: crawl4ai, playwright

### `venv/pyvenv.cfg`
- **Purpose**: Virtual environment configuration
- **Python Version**: 3.10.12
- **System Packages**: Excluded (`include-system-site-packages = false`)

## Data Files

### `links.txt`
- **Purpose**: Contains list of Hyperwallet documentation URLs to crawl
- **Format**: One URL per line
- **Target**: Hyperwallet Drop-in UI v2.4 documentation
- **Content**: 18 URLs covering:
  - Overview and authentication
  - Transfer methods
  - Payee verification
  - Configuration and styling options

## Architecture

### Main Script: `crawl_docs_sequential.py`
- **Entry Point**: `main()` function loads URLs from `links.txt` and initiates crawling
- **Sequential Processing**: Uses session reuse for efficient crawling across multiple URLs
- **Browser Configuration**: Optimized for headless operation with Docker-compatible flags
- **Error Handling**: Robust error handling for file I/O and crawling operations
- **Output**: Markdown conversion using `DefaultMarkdownGenerator`

### Key Components
- `crawl_sequential()`: Main crawling logic with session management
- `get_docs_urls()`: File-based URL loading with error handling
- `AsyncWebCrawler`: crawl4ai's main crawling engine
- `BrowserConfig`: Browser settings optimized for performance

## Usage Context
This project appears to be designed for documentation extraction and analysis, likely for:
- Creating local copies of documentation
- Content analysis and processing
- Documentation migration or backup
- Integration with AI/ML workflows (given the "for-ai" directory name)

## Development Environment
- **Platform**: Linux (specifically Ubuntu/Debian based on kernel version)
- **Package Manager**: pip (standard Python package manager)
- **Environment Isolation**: Python virtual environment
- **Browser Engine**: Playwright (Chromium-based)