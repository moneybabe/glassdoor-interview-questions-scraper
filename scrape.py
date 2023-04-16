from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


urls_pages = {"https://www.glassdoor.com/Interview/Amazon-Interview-Questions-E6036_P4.htm": 4}
PATH = "/path/to/chromedriver"

class Scrape:
    
    # urls_pages is a dictionary of urls as keys and number of pages you want to scrape for corresponding url as values
    def __init__(self, urls_pages):
        self.urls_pages = urls_pages
        self.questions = set()

    def scrape(self):
        # initialize driver
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"
        driver = webdriver.Chrome(PATH, desired_capabilities=caps)

        # login, need to manually type in email and password within 10 seconds window
        driver.get("http://www.glassdoor.com/profile/login_input.htm")
        time.sleep(10)

        for url in self.urls_pages:

            # iterate through all the pages
            for i in range(1, self.urls_pages[url]+1):
                current_url = url[:-4] + "_IP" + str(i) + ".htm"
                driver.get(current_url)
                time.sleep(0.2)
                question_nodes = driver.find_elements_by_xpath("//*[@class='d-inline-block mb-sm']")
                for question_node in question_nodes:
                    question = {question_node.text}
                    self.questions = self.questions.union(question)

        driver.quit()
        
        return self.questions

    def export_to_txt(self):
        questions = list(self.questions)
        with open("interview_questions.txt", "w") as data:
            for i in range(len(questions)):
                data.write(str(i) + ") \n" + questions[i] + "\n\n")

if __name__ == "__main__":
    scraper = Scrape(urls_pages)
    scraper.scrape()
    scraper.export_to_txt()