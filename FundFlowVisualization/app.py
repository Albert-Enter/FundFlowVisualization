from flask import Flask, jsonify, render_template
from py2neo import Graph

graph = Graph('http://localhost:7474', username='neo4j', password='neo4j')

app = Flask(__name__)



def buildAll(Record):  # 统一一下输出格式 都小写加驼峰

    nodes_data = []
    relationships_data = []
    # print(list(Record))
    for record in list(Record):
# 取 n
        if "n" in record.keys():
            node_n = record['n']
            node_n_data = {
                "accountName": node_n['AccountName'],
                "id": node_n["AccountId"],
                'label': 'account'
            }
            nodes_data.append({"data": node_n_data})

        if "m" in record.keys():
            node_m = record['m']
            node_m_data = {
                "accountName": node_m['AccountName'],
                "id": node_m["AccountId"],  # 一定要改成id!!!
                'label': 'account'
            }
            nodes_data.append({"data": node_m_data})

        if "r" in record.keys():
            relationship = record['r']
            relationship_data = {
                'source': relationship.start_node['AccountId'],
                'target': relationship.end_node['AccountId'],
                "type": relationship['Type'],
                "balance": relationship["balance"],
                'amount': relationship["Amount"],
                "index": relationship["index"],
                "time": relationship["time"]
            }
            relationships_data.append({"data": relationship_data})

    return {"nodes": nodes_data, "edges": relationships_data}

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/graph")
def get_graph():
    graph_data = buildAll(graph.run("match(n)-[r]->(m) return n,r,m limit 100"))
    return jsonify(elements=graph_data)


if __name__ == '__main__':
    app.run(debug=True)


# def bulidNodes(Record): # 统一一下输出格式 都小写加驼峰
#     nodes_data = []
#     for record in list(Record):
#         node = record['n']
#         node_data = {
#             "accountName": node['AccountName'],
#             "accountId": node["AccountId"],
#             'label': 'account'
#         }
#         nodes_data.append({"data":node_data})
#     return nodes_data
#
# def bulidEdges(Record):
#     relationships_data = []
#     for record in list(Record):
#         relationship = record['r']
#         relationship_data = {
#             'source': relationship.start_node['AccountId'],
#             'target': relationship.end_node['AccountId'],
#             "type": relationship['Type'],
#             "balance": relationship["balance"],
#             'amount': relationship["Amount"],
#             "index": relationship["index"],
#             "time": relationship["time"]
#         }
#         relationships_data.append({"data": relationship_data})
#     return relationships_data