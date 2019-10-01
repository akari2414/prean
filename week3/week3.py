import urllib.request, json, sqlite3

data = urllib.request.urlopen('http://api.plos.org/search?q=title:DNA').read()
jsonData = json.loads(data)
docs = jsonData['response']['docs']

con = sqlite3.connect('./week3/hun.sqlite')
cur = con.cursor()

cc = cur.execute('''
drop table if exists docs''')

create = ''

for colum in docs[0].keys() :
    if create == '' :
        create = colum + ' TEXT'
    else :
        create += ', ' + colum + ' TEXT'

cur.execute('''
create table docs (''' + create + ''')''')

for docsData in docs:
    v = ['?'] * len(docsData.keys())
    ide = []

    query = "insert into docs (" + ', '.join(docsData.keys()) + ") values (" + ','.join(v) + ")"
    for ck in docsData.values() :
        if(type(ck) is list):
            ide.append(json.dumps(ck))
        else :
            ide.append(ck)

    cur.execute(query, ide)
    con.commit()

print(len(docs))