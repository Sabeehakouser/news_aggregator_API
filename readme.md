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
<img width="953" alt="image" src="https://github.com/user-attachments/assets/a65baf8f-b9bc-4b59-9adc-bc359147052f">
<img width="959" alt="image" src="https://github.com/user-attachments/assets/1134bd8d-0fbb-4059-a02d-77cea710d4d1">
<img width="956" alt="image" src="https://github.com/user-attachments/assets/a04a8440-c0a3-47bc-a0fc-1c108e402015">
<img width="958" alt="image" src="https://github.com/user-attachments/assets/9a39185e-1c8a-4b08-b135-7669204650c4">


