# glassdoor-interview-questions-scraper
This scraper scrapes the interview questions for a company without other information, such as application status. It aims to help intewviewees collect previous interview questions more easily.

## Installation
1. `$ git clone https://github.com/moneybabe/glassdoor-interview-questions-scraper.git`
2. `$ pip install selenium`
3. Download Chromedriver from [here](https://chromedriver.chromium.org/downloads).

## Usage
1. In `scrape.py`, configure `urls_pages`. Say you want to scrape the first 10 pages of Jane Street's interview questions, then you would put `urls_pages = {"https://www.glassdoor.com/Interview/Jane-Street-Interview-Questions-E255549.htm": 10}`
2. Configure `PATH` to be where you downloaded your Chromedriver to. To avoid hassle, you can simply put the Chromedrive in the working directory and set `PATH = "chromedriver"`
3. Run `$ python scrape.py`, and a chrome browser would open up. Then you will need to manually login to your account within 10 seconds window.
4. After logging in, it will start scraping, and after it's done, `interview_questions.txt` would be created in the same directory you are working in.

NOTE: `scrape.ipynb` briefly shows the working principle of everything, and how to work independently with the functions.

#### Have fun and good luck in your interview!
