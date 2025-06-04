import json
import boto3
import botocore.config
from datetime import datetime

###AWS BEDROCK CALL

def content_generation(blogtopic:str)->str:
    prompt = f"""Write a 200 words blog post on {blogtopic}"""
    
    body = {
        "prompt":prompt,
        "max_gen_len":512,
        "temperature":0.5,
        "top_p" : 0.9,
    }
    
    try:
        