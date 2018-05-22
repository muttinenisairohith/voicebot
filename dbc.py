import sqlite3

conn = sqlite3.connect('test.db')
print "opened database successfully";

#conn.execute('''create table chat(id int primary key not null,ques char[50] not null,ans char[50] not null);'')
#print "table created successfully"

conn.execute("insert into chat(id,ques,ans) values(3,'hello gud morning','hello gud morning')");
conn.commit()
print "records successfully created"

cursor = conn.execute("SELECT id, ques, ans from chat")
for row in cursor:
   print "id = ", row[0]
   print "ques = ", row[1]
   print "Ans = ", row[2]

print "Operation done successfully";
conn.close()
