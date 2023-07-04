from dotenv import load_dotenv
from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
  storage_client = storage.Client()
  breakpoint()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  blob.upload_from_filename(source_file_name)

  print(
    "File {} uploaded to {}.".format(
      source_file_name, destination_blob_name
    )
  )

load_dotenv()
print("Uploading Lenna")
upload_blob('5eozfehvmiegthq94b34', 'test_files\lenna.png', 'lenna')