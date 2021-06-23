# Use this code snippet in your app.
# If you need more information about configurations or implementing the sample code, visit the AWS docs:   
# https://aws.amazon.com/developers/getting-started/python/

import boto3
import base64
from botocore.exceptions import ClientError
import pymysql
import json
import sys


def get_secret():

    secret_name = "fox1"
    region_name = "ca-central-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    # In this sample we only handle the specific exceptions for the 'GetSecretValue' API.
    # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
    # We rethrow the exception by default.

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        #return get_secret_value_response

    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            
    # Your code goes here.
    return secret



secret_result = get_secret()
y = json.loads(secret_result)
#print("-------")
#print(secret_result)
#print(y["username"])
#print(y["password"])
#print(y["host"])
#print("-------")

proxy_host = "proxy1.proxy-c3dgprehb0sn.ca-central-1.rds.amazonaws.com"
#proxy_host = "xxxxxxx-2-cluster.cluster-c3dgprehb0sn.ca-central-1.rds.amazonaws.com"
REGION = "ca-central-1"

session = boto3.Session()
client = session.client('rds')
token = client.generate_db_auth_token(DBHostname=proxy_host, Port=y["port"], DBUsername=y["username"], Region=REGION)

#print(token)

#mysql -h proxy1.proxy-c3dgprehb0sn.ca-central-1.rds.amazonaws.com -u xxxxxxx -p

#conn = pymysql.connect(host="database-2-cluster.cluster-c3dgprehb0sn.ca-central-1.rds.amazonaws.com", user="xxxxxxx", password='xxxxxxx', db="accounts")
conn = pymysql.connect(host=proxy_host, user=y["username"], password=y["password"], database="accounts")
#https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.Connecting.Python.html
#https://aws.amazon.com/ko/getting-started/hands-on/set-up-shared-database-connection-amazon-rds-proxy/

try:
    curs = conn.cursor()
    sql = "select * from users order by userid Desc limit 3"
    curs.execute(sql)
    rows = curs.fetchall()
    
    for row in rows:
        print(row)
        
finally:
    conn.close()
