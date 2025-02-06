import requests
from bs4 import BeautifulSoup as bs

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

#print(page.text)

soup = bs(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
#print(results.prettify)

job_cards = results.find_all("div", class_="card-content")

for job_card in job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())

# Use a lambda function to return any h2 elements containing the substring of "python"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# debug print to see if you're bringing back python jobs
#print(len(python_jobs))

# step up to the third-level parent div of the element containing "python" to return more job data
python_job_cards = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for card in python_job_cards:
    title_element = job_card.find("h2", class_="title")
    company_element = job_card.find("h3", class_="company")
    location_element = job_card.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())