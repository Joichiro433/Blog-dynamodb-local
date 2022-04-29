"""
Requirements
------------
$ pip install boto3
"""


import boto3


def create_table(dynamodb):
    table = dynamodb.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


def insert_data(table):
    movies = [
            {
                "year": 2013,
                "title": "Rush",
                "info": {"directors": ["Ron Howard"], "release_date": "2013-09-02T00:00:00Z"}
            },
            {
                "year": 2013,
                "title": "Prisoners",
                "info": {"directors": ["Denis Villeneuve"], "release_date": "2013-08-30T00:00:00Z"}
            }
    ]

    with table.batch_writer() as batch:
        for movie in movies:
            batch.put_item(Item=movie)
            print(f'Adding movie: {movie["year"]}, {movie["title"]}')


if __name__ == '__main__':
    dynamodb = boto3.resource(
        service_name='dynamodb', 
        endpoint_url='http://localhost:8000',
        aws_access_key_id='',
        aws_secret_access_key='',
        region_name='')
    movie_table = create_table(dynamodb)
    print(f'Table status: {movie_table.table_status}')
    insert_data(movie_table)