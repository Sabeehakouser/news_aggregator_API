import psycopg2   # pip install psycopg2
import csv

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

# Main function to ingest data
def ingest_data():
    # Connect to PostgreSQL
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("Delete from articles")
    # Open the CSV file
    with open('news_articles_with_predictions.csv', 'r',encoding='utf-8') as file:
        data_reader = csv.reader(file)
        # next(data_reader)  # Skip the header row
        
        # Insert each row into the table
        for row in data_reader:
            print(row)
            cur.execute("INSERT INTO articles (Title, Summary, PublicationDate, Source, URL, Category) VALUES (%s, %s, %s, %s, %s, %s)", row)

    # Commit and close the connection
    conn.commit()
    cur.close()
    conn.close()
    print("Data ingested successfully")

if __name__ == "__main__":
    ingest_data()