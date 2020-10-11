import boto3

ACCESS_KEY = None
SECRET_KEY = None
AWS_FILE = "img/example_file.jpg"
s3 = boto3.client("s3", aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
s3.upload_file("check.jpg", "s3_name", AWS_FILE, ExtraArgs={"ACL": "public-read"})
