# 导入数据
from py2neo import Graph, Node, Relationship

graph = Graph('http://localhost:7474', username='neo4j', password='neo4j')

import pandas as pd
import os

print (os.getcwd())
dirs = os.listdir('data')

for index in range(len(dirs)):  # 对每一个文件操作

    data = pd.read_csv('data/' + dirs[index])
    account = dirs[index][0:18]
    AccountName = dirs[index][20: -4]

    # cypher1 = "merge ({}:Account {{account:{},name:{}}})".format(AccountName, account, "'AccountName'")
    # print(cypher1)
    # graph.run(cypher1)

    #创造根节点
    root = Node("Account", AccountId=account)
    root['AccountName'] = AccountName
    graph.merge(root, 'Account', 'AccountName')

    print(index)

    for i in range(data.shape[0]):# 对每一条数据操作
        index = data.loc[i][0]
        amount = data.loc[i][1]
        balance = data.loc[i][2]
        OppositeAccount = data.loc[i][3]
        OppositeAccountName = data.loc[i][4]
        time = data.loc[i][5]
        TransactionType = data.loc[i][6]

        # 创造关系

        opaccount = Node('Account', AccountId=int(OppositeAccount))
        opaccount['AccountName'] = OppositeAccountName
        graph.merge(opaccount, 'Account', "AccountName")

        if amount > 0:  # 一定要注意数据格式，padas的格式还要int一下

            r = Relationship(root, "转到", opaccount)
            r['time'] = time
            r['balance'] = int(balance)
            r['index'] = int(index)
            r['Type'] = TransactionType
            r['Amount'] = int(amount)
            graph.merge(r, '转到')

        if amount < 0:

            r = Relationship(opaccount, "转到", root)
            r['time'] = time
            r['balance'] = int(balance)
            r['index'] = int(index)
            r['Type'] = TransactionType
            r['Amount'] = int(-amount)
            graph.merge(r, "转到")




