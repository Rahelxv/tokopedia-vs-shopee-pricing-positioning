import asyncio
import scrapy
from scrapy_playwright.page import PageMethod


class MarketplacesSpider(scrapy.Spider):
    name = "marketplaces"
    allowed_domains = ["tokopedia.com"]

    async def start(self):
        url = "https://www.tokopedia.com/p/elektronik"

        yield scrapy.Request(
            url,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", "body"),
                    PageMethod(
                        "evaluate",
                        """async () => {
                            await new Promise((resolve) => {
                                let totalHeight = 0;
                                const distance = 300;
                                const timer = setInterval(() => {
                                    const scrollHeight = document.body.scrollHeight;
                                    window.scrollBy(0, distance);
                                    totalHeight += distance;

                                    if (totalHeight >= scrollHeight || totalHeight > 5000) {
                                        clearInterval(timer);
                                        resolve();
                                    }
                                }, 200);
                            });
                        }""",
                    ),
                    PageMethod("wait_for_timeout", 4000),
                ],
            },
            callback=self.parse,
        )

    def parse(self, response):
        self.logger.info(
            f"[ SUCCESS ] Ukuran Response HTML: {len(response.body)} bytes"
        )

        cards = response.xpath(
            '//div[contains(@class, "gG1uA844gIiB2+C3QWiaKA==")]'
        )

        for card in cards:

            judul = card.xpath(
                './/div[contains(@class, "y-oybT3IAd310DVdH3OwVg==")]//span/text()'
            ).get()

            harga = card.xpath('.//span[contains(text(), "Rp")]/text()').get()
            if not harga:
                harga = card.xpath(
                    './/div[contains(text(), "Rp")]/text()'
                ).get()

            rating = card.xpath(
                './/div[contains(@class, "c7W9YYbRQuC29+GfsfRTEA==")]//span[contains(@class, "_2NfJxPu4JC")]/text()'
            ).get()

            terjual = card.xpath(
                './/span[contains(text(), "terjual") or contains(text(), "Terjual")]/text()'
            ).get()

            judul_clean = judul.strip() if judul else None
            harga_clean = harga.strip() if harga else None
            rating_clean = rating.strip() if rating else None
            terjual_clean = terjual.strip() if terjual else None

            if judul_clean:
                yield {
                    "judul": judul_clean,
                    "harga": harga_clean,
                    "rating": rating_clean,
                    "terjual": terjual_clean,
                }