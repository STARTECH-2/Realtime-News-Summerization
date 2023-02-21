import gtts
from newsapi import NewsApiClient
import pycountry
from newsfetch.news import newspaper
import os
from summarizer import Summarizer
from playsound import playsound
newsapi = NewsApiClient(api_key='0c5239181cb5425782763385b08f7f09')
input_country = "India"
input_countries = [f'{input_country.strip()}']
countries = {}
for country in pycountry.countries:
    countries[
        country.name] = country.alpha_2  # Storing the unique code of each country in the dictionary along with its name

# Checking if the given country name is valid or not
codes = [countries.get(country.title(), 'Unknown code') for country in input_countries]

option = input(
    "Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology"
    "\n\nEnter here: ")

top_headlines = newsapi.get_top_headlines(

    # getting top headlines from all the news channels
    category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

# fetch the top news under that category
Headlines = top_headlines['articles']
# print(Headlines)
lst_articles = []
i = 0
# now we will display the that news with a good readability for user
if Headlines:
    for articles in Headlines:
        i += 1
        s = ""
        b = articles['title'][::-1].index("-")
        if "news" in (articles['title'][-b + 1:]).lower():
            s += f"{articles['url']}."
            lst_articles.append(articles['url'])
            print(str(i) + ".",
                  f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
        else:
            s += f"{articles['url']}."
            lst_articles.append(articles['url'])
            print(str(i) + ".",
                  f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
else:
    print(f"Sorry no articles found for {input_country}, Something is Wrong!!!")
print('\n')
# print(lst_articles)
choice = int(input('Select the article you want to know about : '))
if choice <= len(lst_articles):
    news = newspaper(lst_articles[choice - 1])
    try:
        os.remove("news_article.txt")
        file = open("news_article.txt", "x")
        file.close()
        file = open("news_article.txt", "a")
        file.write(news.article)
        file.close()
    except:
        file = open("news_article.txt", "x")
        file.close()
        file = open("news_article.txt", "a")
        file.write(news.article)
        file.close()
    f = open("news_article.txt","r")
    bert_model = Summarizer()
    bert_summary = ''.join(bert_model(f.read(), min_length=60))
    print(bert_summary)
    tts = gtts.gTTS(bert_summary, lang="en")
    tts.save("G:/Projects/Text-Summerization/my-news.mp3")
    playsound("G:/Projects/Text-Summerization/my-news.mp3")
    os.remove("G:/Projects/Text-Summerization/my-news.mp3")
else:
    print('The article number You have selected is not available. Please try again later!!')
