# TODO: Pull up a list of image URLS with alt_text for the blue/orange/orange and blue offering form Sling landing page.

def test_challenge3slingImage(self):
        self.driver.get("https://sling.com")
        channelList = self.driver.find_elements(By.XPATH, '//*[@id="channelList"]//img')

        print(channelList[i].get_attribute("") + " - " channelList[i].get_attribute("alt"))
