    from google.cloud import storage


    storage_client = storage.Client()

    # List all accounts for a project
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    bucket = storage_client.get_bucket(bucket_name)
    for account in bucket.acl:
        print(account)  
