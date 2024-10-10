from flask import Flask, jsonify, request
import psycopg2  # pip install psycopg2
import datetime

app = Flask(__name__)


# Database connection parameters
DB_HOST = 'localhost'
DB_NAME = 'news'
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_PORT = '5432'

# Function to connect to PostgreSQL
def connect_to_db():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

@app.route('/articles', methods=['GET'])
def get_articles():
    conn = connect_to_db()
    cur = conn.cursor()

    # Get query parameters
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    category = request.args.get('category')

    # Build the WHERE clause based on query parameters
    where_clause = []
    params = []
    if start_date:
        where_clause.append("articles.publicationdate >= %s")
        start_date_formatted = datetime.datetime.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
        params.append(start_date_formatted)
    if end_date:
        where_clause.append("articles.publicationdate <= %s")
        end_date_formatted = datetime.datetime.strptime(end_date, "%Y-%m-%d").strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
        params.append(end_date_formatted)
    if category:
        where_clause.append("articles.category LIKE %s")
        params.append(f"%{category}%")  # Use wildcard for case-insensitive search

    # Construct the SQL query
    query = "SELECT * FROM articles"
    if where_clause:
        query += " WHERE " + " AND ".join(where_clause)

    # Execute the query with parameters
    cur.execute(query, params)
    rows = cur.fetchall()

    articles = []
    for row in rows:
        article = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "publication_date": row[3].strftime("%Y-%m-%d"),  # Format date as YYYY-MM-DD
            "source": row[4],
            "url": row[5],
            "category": row[6]
        }
        articles.append(article)

    cur.close()
    conn.close()

    if len(articles) == 0:
        return jsonify({'message': 'No articles found matching the search criteria'}), 404  # Return a 404 if no articles found
    return jsonify(articles)

@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM articles WHERE id = %s", (article_id,))  # Use parameterized query for safety
    row = cur.fetchone()

    if row:
        article = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "publication_date": row[3].strftime("%Y-%m-%d"),  # Format date as YYYY-MM-DD
            "source": row[4],
            "url": row[5],
            "category": row[6]
        }
        cur.close()
        conn.close()
        return jsonify(article)
    else:
        cur.close()
        conn.close()
        return jsonify({'message': 'Article not found'}), 404  # Return a 404 status code if article not found


@app.route('/search', methods=['GET'])
def search_articles():
    conn = connect_to_db()
    cur = conn.cursor()

    # Get query parameters
    keywords = request.args.get('keywords')
    # print(keywords)
    # Build the WHERE clause based on query parameters
    where_clause = []
    params=[]
    if keywords:
        # Search for keywords in title, summary, and other relevant fields
        where_clause.append("LOWER(articles.title) LIKE %s OR LOWER(articles.summary) LIKE %s")
        params.extend([f"%{keywords}%".lower(), f"%{keywords}%".lower()])
    # print(params)
    # Construct the SQL query
    query = "SELECT * FROM articles"
    if where_clause:
        query += " WHERE " + where_clause[0]

    # Execute the query with parameters
    cur.execute(query, params)
    rows = cur.fetchall()

    articles = []
    for row in rows:
        article = {
            "id": row[0],
            "title": row[1],
            "summary": row[2],
            "publication_date": row[3].strftime("%Y-%m-%d"),  # Format date as YYYY-MM-DD
            "source": row[4],
            "url": row[5],
            "category": row[6]
        }
        articles.append(article)

    cur.close()
    conn.close()

    if len(articles) == 0:
        return jsonify({'message': 'No articles found matching the search criteria'}), 404  # Return a 404 if no articles found
    return jsonify(articles)


if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print("An exception: ", e)