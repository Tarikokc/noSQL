from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

test_text = {
    "analyzer": "french_heavy",
    "text": "Je dois bosser pour mon QCM sinon je vais avoir une sale note :( ..."
}

result = es.indices.analyze(index="french", body=test_text)
print(result)