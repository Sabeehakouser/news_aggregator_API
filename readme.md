PersonalizedNewsAggregator
#
<p>End Goal: To develop a news aggregator that scrapes articles from multiple sources, categorizes them, and provides access via a REST API and a simple front-end interface.
</p>
<p>
Part 1: News Scraper
Objective:
To scrape news articles from multiple sources (any 2 news sources e.g., BBC, CNN, Timesofindia
etc) and collect the following data:<br>
● Title: The article's headline.<br>
● Summary: A brief overview or the first few sentences.<br>
● Publication Date: The date the article was published.<br>
● Source: The news outlet's name.<br>
● URL: Link to the article.<br>
and category for training<br>
Output:
Store data in news_articles.csv.
</p>
<p>
Part 2: Content Categorization
Objective:
Use NLP(Used random forest for training custom model i.e., random_forest_model.pkl) to categorize articles into topics (e.g., politics, technology, sports).
<br>
Output:
Update news_articles_with_predictions.csv with a new "PCategory" column.
</p>
<p>
Part 3: REST API Development
Objective:
Create a REST API to serve the news articles.<br>
Endpoints:<br>
● GET /articles: Retrieve all articles, with filtering options like by a date range, of a
specific category.<br>
● GET /articles/{id}: Retrieve a specific article.<br>
● GET /search: Search articles by keywords.<br>
->Used Flask, PostgreSQL<br>
Output:
Serve data in JSON format.
</p>
<b>Postman Collections Link</b>: <a href="https://www.postman.com/mission-geoscientist-3256618/newsaggregrator/collection/2vej9dm/deepklarity?action=share&creator=36276051">Click here!</a>

![Screenshot 2024-10-10 201053](https://github.com/user-attachments/assets/e9bb26ba-27fe-4542-9284-d91e680a7683)
![Screenshot 2024-10-10 201338](https://github.com/user-attachments/assets/492c68bd-c553-49d2-873e-336b6f49b132)
![Screenshot 2024-10-10 201133](https://github.com/user-attachments/assets/35dfbf15-508a-47dd-9345-5f9ac3ec63d7)
![Screenshot 2024-10-14 172325](https://github.com/user-attachments/assets/9476ef3b-334d-4956-a351-262d152717b3)
