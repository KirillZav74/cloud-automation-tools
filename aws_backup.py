# Скрипт для резервного копирования в AWS S3
import boto3
import datetime

def backup_to_s3(local_path, bucket_name):
    s3 = boto3.client('s3')
    date = datetime.datetime.now().strftime("%Y%m%d")
    s3.upload_file(local_path, bucket_name, f"backups/backup_{date}.tar.gz")
    print(f"Backup {local_path} to {bucket_name} completed")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python aws_backup.py [local_file] [s3_bucket]")
        sys.exit(1)
    backup_to_s3(sys.argv[1], sys.argv[2])
