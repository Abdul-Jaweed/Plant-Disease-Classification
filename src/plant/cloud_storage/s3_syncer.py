import os
class S3Sync:
    
    # to send data to s3
    def sync_folder_to_s3(self,folder,aws_buket_url):
        command = f"aws s3 sync {folder} {aws_buket_url} "
        os.system(command)
    
    # to receive data to s3
    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_buket_url} {folder} "
        os.system(command)