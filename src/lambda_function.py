import json
import os
import boto3
import logging

s3 = boto3.client("s3")


def lambda_handler(event, context):
    s3_bucket = os.environ.get("S3_BUCKET")
    msg_in = event["message"]

    print(f'Evento recibido: {msg_in}')

    print(f"Variable de entorno bucket S3: {s3_bucket}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda2')
    }
