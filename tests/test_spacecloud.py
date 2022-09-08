import time
import unittest
from unittest.case import skip

import pytest
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class TestNaverCrackerClass(unittest.TestCase):
    """Test case docstring."""

    def setUp(self):
        self.ua = UserAgent()
        self.userAgent = self.ua.random
        self.options = Options()

        self.options.add_argument(f"user-agent={self.userAgent}")
        # self.options.add_argument('headless')
        # self.options.add_argument("window-size=1920x1080")
        # self.options.add_argument("disable-gpu")
        # self.driver = webdriver.Chrome(chrome_options=self.options)
        # self.driver = webdriver.Chrome()
        self.target_1 = "https://www.spacecloud.kr/space/23824"

    def tearDown(self):
        pass
        # self.driver.quit()

    def test_smoke_test(self):
        assert True

    def test_request_and_bs4(self):
        res = requests.get(url=self.target_1)
        html = res.text
        soup = bs(html, "html.parser")
        host_space_title = soup.select_one(
            "#content_wraper > div > div > div.detail_forms > div.photo_box_wrap.type9 > div.detail_box.map_box > div.host_profile > div > div.sp_location > p.sp_name"
        )

        host_website = soup.select_one(
            "#content_wraper > div > div > div.detail_forms > div.photo_box_wrap.type9 > div.detail_box.map_box > div.host_profile > div > div.sp_location > p.sp_homepage > a"
        )

        host_address = soup.select_one(
            "#content_wraper > div > div > div.detail_forms > div.photo_box_wrap.type9 > div.detail_box.map_box > div.host_profile > div > div.sp_location > p.sp_address"
        )
        print("\n")
        print(host_space_title.get_text())
        print(host_website.get_text())
        print(host_address.get_text())
        print("\n")
