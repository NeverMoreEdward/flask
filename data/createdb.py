import sqlite3
conn = sqlite3.connect('errorlog.db')
cursor = conn.cursor()
cursor.execute('create table errorlog (id int(20) primary key, message varchar(20), timestamp_ varchar(20), pythontime double  ) ')
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(1, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(2, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(3, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(4, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(5, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(6, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(7, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(8, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(9, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(10, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))
cursor.execute('insert into errorlog (id, message, timestamp_, pythontime) values (%i, %a, %a, %a)' %(11, "This is the first message", "2019-01-04T05:44:45.521Z", 1547012345.2921011))





cursor.close()
conn.commit()
conn.close()
