import sys
import boto3
import os
import mysql.connector

ENDPOINT="ngoproject-mysql.ch8w6akksq5j.us-west-2.rds.amazonaws.com"
PORT="3306"
USR="ngoproject"
REGION="us-west-2"
DBNAME="ngoproject-mysql"
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'

#gets the credentials from .aws/credentials
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)                    

try:
    conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=token, port=PORT, database=DBNAME, ssl_ca='[full path]rds-combined-ca-bundle.pem')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))
