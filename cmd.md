```bash
# Create virtual environment
python3 -m venv python_env

# Activate environment
source python_env/bin/activate

# Install required packages
pip install pymongo redis neo4j

# Stop all containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -a -q)

# Check running containers
docker ps

# MongoDB
docker run -d -p 27017:27017 mongo

# Redis
docker run -d -p 6379:6379 redis

# Neo4j
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/test12345678 neo4j

# Elasticsearch
docker run -p 9200:9200 -p 9300:9300 -d \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.14.0

# Find Windows host IP
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'

# Launch Elasticsearch Container
docker run -p 9200:9200 -p 9300:9300 -d \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.14.0

curl 0.0.0.0:9200/_cluster/health | jq 
```

