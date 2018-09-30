import boto3


def get_all_object_keys(bucket, start_after='', keys=[], prefix=''):
    """
    Fetch object keys from s3 bucket with given prefix value
    Parameters
    ----------
    bucket: str
        s3 bucket name
    start_after: str
        keyname to start after
    keys: str
        list of keys
    prefix: str
        prefix of files in s3 bucket
    Returns
    -------
    Return keys of objects inside s3 bucket.
    """

    client = boto3.client('s3')
    response = client.list_objects_v2(
        Bucket=bucket, StartAfter=start_after, Prefix=prefix)

    if 'Contents' not in response:
        return keys

    key_list = [item['Key'] for item in response.get('Contents', [])]
    # key_list = response['Contents']
    last_key = key_list[-1]

    keys.extend(key_list)

    return get_all_object_keys(bucket, last_key, keys, prefix)


if __name__ == '__main__':
    input_bucket = ''
    prefix_files = ''
    object_keys = get_all_object_keys(input_bucket, keys=[], prefix=prefix_files)
    file_keys = filter(lambda x: x if not x.endswith('/') else None,
                   object_keys)
    no_of_objects = len(file_keys)
    print no_of_objects
    print file_keys
    