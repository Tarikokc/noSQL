# NoSQL Database Examples

This repository contains example implementations for MongoDB, Redis, and Neo4j databases created in February 2025.

## 📂 Directory Structure

```
NOSQL/
├── mongoDB/
│   ├── captures/                     # Screenshots  
│   │   ├── conn_mongoDB.png
│   │   └── json_mongoDB.png
│   └── py/                          # Python implementation
│       ├── accounts.json            # Sample data
│       ├── accounts.py              # Account operations
│       └── conn_mongodb.py          # Connection example
├── neo4j/
│   ├── capture/                     # Screenshots
│   └── neo_conn.py                  # Graph operations example
└── Redis/
    ├── data/                        # Data types documentation
    │   ├── Hashes.png
    │   ├── List.png 
    │   ├── Sets.png
    │   └── Sorted_sets.png
    ├── init/                        # Initialization
    └── py/                          # Python implementation
        ├── redis_python_connection.py
        └── redis_python_pool.py
```

## 🚀 Getting Started 

### Prerequisites

- Docker
- Python 3.x
- WSL2 (if using Windows)

### Installation
```bash
# Create Python virtual environment
python3 -m venv python_env
source python_env/bin/activate

# Install required packages
pip install pymongo redis neo4j
```

### Starting Databases with Docker

```bash
# MongoDB
docker run -d -p 27017:27017 mongo

# Redis
docker run -d -p 6379:6379 redis

# Neo4j (password must be at least 8 characters)
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/test12345678 neo4j
```

### WSL Users
Replace `localhost` with your host machine IP in connection strings:
```python
# Find your host IP
cat /etc/resolv.conf | grep nameserver | awk '{print $2}'
```

## 📚 Database Examples

### MongoDB
- Basic CRUD operations
- Account management example
- JSON data handling

### Redis
- Connection examples
- Connection pooling
- Data types:
  - Lists
  - Sets
  - Hashes
  - Sorted Sets

### Neo4j
- Graph database operations
- Movie recommendation system
- Relationship queries

---

