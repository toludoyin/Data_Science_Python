from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.futurefit.co.uk/blog/jobs-without-a-degree/').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find('div', class_ = 'row row-3735-1 row-standard-content first-row before-form before-bg-ff-coral')
for job in jobs:
    job_type = job.find('h3', class_ = 'jobhead').text[2:].strip()
    # avg_amount = job.find('strong')
    print(jobs)