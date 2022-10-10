from GoogleNews import GoogleNews
import pandas as pd

news = GoogleNews(period='1d')
news.search("Nigeria")
result = news.result()

data = pd.DataFrame.from_dict(result)
# data = data.drop(columns=["img"])
data.head()
