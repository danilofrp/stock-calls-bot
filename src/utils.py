import json

def read_json(filepath):
    with open(filepath, 'r') as f:
        json_str = f.read()
        data = json.loads(json_str)
    return data


def read_json_from_s3(s3_client, bucket, filepath):
    data = s3_client.Object(bucket, filepath).get()['Body'].read()
    data = json.loads(data)
    return data


def write_json(filepath, data):
    with open(filepath, 'w') as f:
        json_str = json.dumps(data)
        f.write(json_str)
        
        
def write_json_to_s3(s3_client, bucket, filepath, data):
    s3_client.Object(bucket, filepath).put(Body=json.dumps(data))