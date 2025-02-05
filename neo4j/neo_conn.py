from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
password = "test12345678"

driver = GraphDatabase.driver(uri, auth=(user, password))

def run_query(query):
   with driver.session() as session:
       result = session.run(query)
       return list(result)  

# Creating persons
person1 = "CREATE (p:Person {name: 'Alice', age: 30})"
person2 = "CREATE (p:Person {name: 'Bob', age: 25})"
person3 = "CREATE (p:Person {name: 'Charlie', age: 35})"

run_query(person1)
run_query(person2)
run_query(person3)

# Creating relationships
relationship1 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'}) CREATE (a)-[:FRIEND]->(b)"
relationship2 = "MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"
relationship3 = "MATCH (a:Person {name: 'Bob'}), (b:Person {name: 'Charlie'}) CREATE (a)-[:FRIEND]->(b)"

run_query(relationship1)
run_query(relationship2)
run_query(relationship3)

# Retrieving persons
query_all_persons = "MATCH (p:Person) RETURN p.name, p.age"
results = run_query(query_all_persons)

for record in results:
   print(f"Name: {record['p.name']}, Age: {record['p.age']}")
   
# Finding friends of a person
def get_friends(name):
   query = f"MATCH (p:Person {{name: '{name}'}})-[:FRIEND]->(friend) RETURN friend.name, friend.age"
   results = run_query(query)
   return results

name = "Alice"
friends = get_friends(name)

print(f"Friends of {name}:")
for record in friends:
   print(f"Name: {record['friend.name']}, Age: {record['friend.age']}")

# Example with movies
actors = [
   "CREATE (a:Actor {name: 'Tom Hanks'})",
   "CREATE (a:Actor {name: 'Meryl Streep'})",
   "CREATE (a:Actor {name: 'Tom Cruise'})",
   "CREATE (a:Actor {name: 'Julia Roberts'})",
]

movies = [
   "CREATE (m:Movie {title: 'Forrest Gump', year: 1994})",
   "CREATE (m:Movie {title: 'The Post', year: 2017})",
   "CREATE (m:Movie {title: 'Top Gun', year: 1986})",
   "CREATE (m:Movie {title: 'Pretty Woman', year: 1990})",
]

for actor in actors:
   run_query(actor)

for movie in movies:
   run_query(movie)

relationships = [
   "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'Forrest Gump'}) CREATE (a)-[:ACTED_IN]->(m)",
   "MATCH (a:Actor {name: 'Tom Hanks'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
   "MATCH (a:Actor {name: 'Meryl Streep'}), (m:Movie {title: 'The Post'}) CREATE (a)-[:ACTED_IN]->(m)",
   "MATCH (a:Actor {name: 'Tom Cruise'}), (m:Movie {title: 'Top Gun'}) CREATE (a)-[:ACTED_IN]->(m)",
   "MATCH (a:Actor {name: 'Julia Roberts'}), (m:Movie {title: 'Pretty Woman'}) CREATE (a)-[:ACTED_IN]->(m)",
]

for relationship in relationships:
   run_query(relationship)
