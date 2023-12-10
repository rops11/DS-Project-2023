import requests
from bs4 import BeautifulSoup

def dataFromMetacritic(gameName):
    gameNameFormatted = gameName.lower().replace(".", "").replace(":", "").replace(" ", "-")
    URL = f"https://www.metacritic.com/game/{gameNameFormatted}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    #deveoper, rating(E, M etc)
    criticScore = soup.find_all("div", class_="c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green g-color-gray90 c-siteReviewScore_medium")[0].find_all("span")[0].text
    criticCount = soup.find_all("span", class_="c-productScoreInfo_reviewsTotal u-block")[0].find_all("span")[0].text.split()[2].replace(",", "")
    userScore = soup.find_all("div", class_="c-siteReviewScore u-flexbox-column u-flexbox-alignCenter u-flexbox-justifyCenter g-text-bold c-siteReviewScore_green c-siteReviewScore_user g-color-gray90 c-siteReviewScore_medium")[0].find_all("span")[0].text
    userCount = soup.find_all("span", class_="c-productScoreInfo_reviewsTotal u-block")[1].find_all("span")[0].text.split()[2].replace(",", "")
    rating = soup.find_all("div", class_="c-productionDetailsGame_esrb_title u-inline-block g-outer-spacing-left-medium-fluid")[0].find_all("span")[0].text.split()[1]
    developer = soup.find_all("div", class_="c-gameDetails_sectionContainer u-flexbox u-flexbox-column")[1].find_all("li", class_="c-gameDetails_listItem g-color-gray70 u-inline-block")[0].text.strip()
    return {'Critic_Score': criticScore, 'Critic_Count': criticCount, "User_Score": userScore, "User_Count": userCount, "Developer": developer, "Rating": rating}

data = dataFromMetacritic("New Super Mario Bros. Wii")
print(data)