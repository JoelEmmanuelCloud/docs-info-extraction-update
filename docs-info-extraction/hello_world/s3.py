import boto3

class S3ClientHandler:
    def __init__(self, s3_client=None):
        self.s3_client = s3_client or boto3.client('s3')
        self.bucket_name = "dev-poc-gustavo"

    def get_object(self, object_key: str) -> bytes:
        try:
            response = self.s3_client.get_object(
                Bucket = self.bucket_name,
                Key = object_key
            )
            object_bytes = response['Body'].read()

            return object_bytes

        except Exception as e:
            print(f"Failed to get object {object_key} from bucket {self.bucket_name}")
            print(f"Error: {e}")

    def put_object(self, object_key:str, file: bytes):
        try: 
            self.s3_client.put_object(
                Body = file,
                Bucket = self.bucket_name,
                Key = object_key
            )
        except Exception as e:
            print(f"Failed to put object {object_key} to bucket {self.bucket_name}")
            print(f"Error: {e}")