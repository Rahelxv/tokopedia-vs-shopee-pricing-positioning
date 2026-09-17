BOT_NAME = "market_places"

SPIDER_MODULES = ["market_places.spiders"]
NEWSPIDER_MODULE = "market_places.spiders"

DOWNLOAD_HANDLERS = {
"https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
 "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

USER_AGENT="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" 

ROBOTSTXT_OBEY = False

CONCURRENT_REQUESTS = 1
COOKIES_ENABLED = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": False,
}

PLAYWRIGHT_PROCESS_REQUEST_HEADERS = None

PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000
PLAYWRIGHT_MAX_PAGES_PER_CONTEXT = 1  
DOWNLOAD_DELAY = 0


