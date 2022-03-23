#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
engine = create_engine("mysql://root:@localhost/test",echo = True)
conn = engine.connect()


# In[3]:


def getimages():
    
    my_cursor=conn.execute("SELECT * FROM  images")
    my_result=my_cursor.fetchall()
    for row  in my_result:
        print(row)
        fob=open(r'C:\Users\Dell\Desktop\Jainam docs\Deteccion de mascara\Database Images/'+ str(row[0])+'.jpeg','wb')
        fob=fob.write(row[1]) 


# In[ ]:




