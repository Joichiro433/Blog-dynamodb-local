#/bin/bash

# 以前作成したレコードを消去
docker-compose down
rm -rf dynamodb_data

# dynamoDBを構築
docker-compose up -d

# サンプル用のテーブルを作成
python create_table.py