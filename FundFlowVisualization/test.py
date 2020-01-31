# 尝试了一下从neo4j获取规定格式的数据
from py2neo import Graph
from flask import Flask, jsonify, render_template

graph = Graph('http://localhost:7474', username='neo4j', password='neo4j')

result_Node = graph.run("match(n) return n limit 20")

# ####YEAH
# a = list(result_Node)
# #a[1]['n'] 已经是一个node类了
# node = a[1]['n']
# print(dict(node))
# print(a[1]['n']['AccountName']) # 对公账户2852

result_N_R = list(graph.run('match(n)-[r]->(m) return n,r,m'))  # 怎么调用游标？把他们列表化

print(len(result_N_R))
n = result_N_R[0]['n']
r = result_N_R[0]['r']
m = result_N_R[0]['m']
print(n.labels)
print(r.start_node)  # 关系的起止点在网页可视化时很重要 返回的时一个node类型的数据结构

def bulidNodes(nodeRecord):
    nodes_data = []
    for record in list(nodeRecord):  # 这个便利了不同条记录，每条记录中都包含n r m
        node = record['n']
        node_data = {
            "AccountName": node['AccountName'],
            "AccountId": node["AccountId"],
            'label': "account"
        }
        nodes_data.append({'data': node_data})
    return nodes_data

def bulidEdges(Record):
    relationships_data = []

    for record in list(Record):
        print(record)
        relationship = record['r']
        print(relationship["Amount"])
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
    return relationships_data

def get_graph():
    nodes = bulidNodes(graph.run('match(n)-[r]->(m) return n,r,m'))
    edges = bulidEdges(graph.run('match(n)-[r]->(m) return n,r,m'))
    return jsonify(elements={"nodes": nodes, "edges": edges})


def buildAll(Record):  # 统一一下输出格式 都小写加驼峰
    nodes_data = []
    # print(list(Record))
    for record in list(Record):

        node_n = record['n']

        print(node_n)

        node_n_data = {
            "accountName": node_n['AccountName'],
            "accountId": node_n["AccountId"],
            'label': 'account'
        }
        nodes_data.append({"data": node_n_data})

        node_m = record['m']
        node_m_data = {
            "accountName": node_m['AccountName'],
            "accountId": node_m["AccountId"],
            'label': 'account'
        }
        nodes_data.append({"data": node_m_data})

    relationships_data = []
    for record in list(Record):
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

print(buildAll(graph.run('match(n)-[r]->(m) return n,r,m limit 5')))