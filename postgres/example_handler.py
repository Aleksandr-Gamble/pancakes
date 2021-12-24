import json
import psycopg2

conn = psycopg2.connect(
    host="123.456.78.90",
    database="my_database",
    user="postgres",
    password="abc123")

def lambda_handler(event, context):
    cur = conn.cursor()
    cur.execute("SELECT * FROM things")
    things = cur.fetchall()
    return {
        'statusCode': 200,
        'body': json.dumps({'things':things})
    }

