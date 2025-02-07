# ELK Stack Integration

This section describes the Elasticsearch, Logstash, and Kibana (ELK) stack implementation in our NoSQL project.

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
```
Elasticsearch/
├── Logstach/                      # Logstash configurations
│   ├── logs/                      # Log files directory
│   │   └── python_logs.log        # Python application logs
│   ├── data/                      # Data files
│   │   ├── apache_logs.txt        # Apache server logs
│   │   ├── data-json.csv         
│   │   ├── data-json.log
│   │   ├── data.csv
│   │   └── data1.csv
│   └── logstash.conf             # Main Logstash configuration
├── filebeat/                      # Filebeat configuration
│   └── filebeat.yml              # Filebeat settings
└── web_server_logs/              # Web server specific configs
    └── logstash-apache.conf      # Apache logs configuration
```

## 🚀 Getting Started

### Prerequisites
* Docker and Docker Compose
* ELK Stack 7.11.x

### Installation

1. Start the ELK stack using Docker Compose:
```bash
docker-compose up -d
```

2. Verify services are running:
```bash
docker-compose ps
```

### Service Ports
* Elasticsearch: 9200, 9300
* Logstash: 5044, 5045, 9600
* Kibana: 5601

## 🔧 Configuration Files

### Logstash Configuration
```ruby
input {
  beats {
    port => 5044
    type => "python"
  }
  file {
    path => "/data/apache_logs.txt"
    start_position => "beginning"
    sincedb_path => "/dev/null"
    type => "apache"
  }
}

filter {
  if [type] == "python" {
    json {
      source => "message"
      target => "log"
    }
  } else if [type] == "apache" {
    grok {
      match => { "message" => "%{COMBINEDAPACHELOG}" }
    }
    date {
      match => [ "timestamp", "dd/MMM/yyyy:HH:mm:ss Z" ]
      target => "@timestamp"
      remove_field => "timestamp"
    }
    geoip {
      source => "clientip"
    }
  }
}

output {
  if [type] == "python" {
    elasticsearch {
      hosts => ["elasticsearch:9200"]
      index => "python-logs"
    }
    stdout {
      codec => rubydebug
    }
  } else if [type] == "apache" {
    elasticsearch {
      hosts => ["elasticsearch:9200"]
      index => "web_server_logs"
    }
  }
}
```

### Filebeat Configuration
```yaml
filebeat.inputs:
- type: log
  enabled: true
  paths:
    - /logs/*.log
  json.keys_under_root: true
  json.add_error_key: true
  fields:
    type: python

output.logstash:
  hosts: ["logstash:5044"]
```

## 📊 Data Types and Use Cases

### Log Types
1. Python Application Logs
   * Format: JSON
   * Index: python-logs
   * Use cases: Application monitoring, debugging

2. Apache Web Server Logs
   * Format: Combined Apache Log
   * Index: web_server_logs
   * Use cases: Web traffic analysis, security monitoring

## 🔍 Kibana Access

1. Access Kibana dashboard:
   * URL: http://localhost:5601
   * Default credentials: 
     * Username: elastic
     * Password: password

2. Create index patterns:
   * `python-logs` for Python application logs
   * `web_server_logs` for Apache server logs

## 🛠 Maintenance

### Log Rotation
Logs are automatically rotated based on:
* Size: 1GB per file
* Time: Daily rotation

### Backup
Elasticsearch data is persisted using Docker volumes.

## 🔒 Security Notes
* Basic authentication is enabled
* SSL/TLS is disabled (development setup)
* X-Pack security features are disabled

## 📝 Tips for Development
1. Monitor Logstash processing:
```bash
docker-compose logs -f logstash
```

2. Check Elasticsearch indices:
```bash
curl -X GET "localhost:9200/_cat/indices?v"
```

3. Restart individual services:
```bash
docker-compose restart [service_name]
```