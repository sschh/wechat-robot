
# coding: utf-8

# In[12]:


from wxpy import *
import time


# ### 查找好友、群

# In[13]:


def fg_search(name):
    found=[]
    try:
        found=bot.friends().search(name)
        if not found:
            print('未找到好友') 
            bot.file_helper.send('未找到好友')
        else:
             #判断搜索和查找结果是否完全匹配
            print(found)
            for i in range(len(found)):
                if found[i].name==name:
                    print('好友已精确找到') 
                    bot.file_helper.send('好友已精确找到') 
                    return found[i]
            print('未精确找到好友') 
            bot.file_helper.send('未精确找到好友')
            flag=1
    except ResponseError as e:
        print(e.err_code, e.err_msg) # 查看错误号和错误消息
        print('好友查找出错') 
        bot.file_helper.send('好友查找出错')
    try:
        found=bot.groups().search(name)
        if not found:
            print('未精确找到微信群') 
            bot.file_helper.send('未精确找到微信群')
        else:
            print(found)
             #判断搜索和查找结果是否完全匹配
            for i in range(len(found)):
                if found[i].name==name:
                    print('微信群已精确找到') 
                    bot.file_helper.send('微信群已精确找到')
                    return found[i]
            print('未找到微信群') 
            bot.file_helper.send('未找到微信群') 
    except ResponseError as e:
        print(e.err_code, e.err_msg) # 查看错误号和错误消息
        print('群查找出错') 
        bot.file_helper.send('群查找出错')
    return []


# ### 指定时间给指定人、群发送信息

# In[14]:


#date '11-24 00:00:00'
def message_input(name,date,message):
    day=date[3:5]
    hour=date[6:8]
    minute=date[-5:-3]
    sec=date[-2:]
    rorw=input(str(day)+'日 '+str(hour)+':'+str(minute)+':'+str(sec)+'\n请确认日期(y/n):')
    if rorw.lower=='n' or rorw.lower=='no' :
        print('已退出')
        return 0
    while 1:
        if time.localtime().tm_mday==int(day) and time.localtime().tm_hour==int(hour) and         time.localtime().tm_min>=int(minute) and time.localtime().tm_sec>=int(sec):
            name.send(message)
            break
    print('信息已发送') 
    bot.file_helper.send('信息已发送')
def message_send():
    name=input('请输入名字：')
    inputname=fg_search(name)
    if not inputname:return 0
    date=input('请输入日期（MM-DD hh:mm:ss）：')
    message=input('请输入发送信息：')
    message_input(inputname,date,message)


# ### 给多好友发消息

# In[15]:


def send_message(namelist,message):
    found_friend=[]
    for friend in namelist:
        found_friend+=bot.friends().search(friend)
    print(found_friend)
    sure=input('请确认好友(y/n):')
    if sure.lower()!='y':
        print('退出')
        return 0
    for name in found_friend:
        name.send(message)
    print('已发送')


# ### 查找群成员

# In[16]:


#name 查找名字列表（部分关键字）   group指定群
def member_search(namelist,group):
    try:
        found=bot.groups().search(group)
    except ResponseError as e:
        print(e.err_code, e.err_msg) # 查看错误号和错误消息
        bot.file_helper.send('群查找出错')
        return 0 
    result=[]
    if not found:
        return '没有该群'
    else:
        #判断群搜索和查找结果是否完全匹配
        for i in range(len(found)):
            if found[i].name==group:
                group=found[i]
                break
        if type(group)==str:
            return '没有该群'
    #查找群成员
    i=0
    while i<len(namelist): 
        for member in group:
            if name[i] in member.name:
                result.append(member.name)
        i+=1
    return result


# ### 查找聊天记录（登录后的）

# In[17]:


#记录消息类型、内容、发送人、接收时间
def news_search(message):
    bot.messages.max_history = 1000
    #消息信息列表
    meslist=[]
    #消息ID列表
    mesid=[]
    #查找
    m=bot.messages.search(message)
    for mes in m:
        #查找消息ID，若已加入，则不管（不循环运行没必要判断）
        if med.id not in mesid:
            mesid.append(mes.id)
            meslist.append([mes.type,mes.text,mes.sender,mes.member,mes.receive_time.strftime("%Y-%m-%d %H:%M:%S")])
    print(meslist)
    bot.file_helper.send(meslist)
def record_search():
    message=input('请输入查找信息：')
    news_search(message)


# In[19]:


bot=Bot(cache_path=True)#console_qr=1
#fg_search(name)#查找好友、群
#message_send()#指定时间给指定好友、群发消息
#send_message(namelist,message)#给多好友发消息
#member_search(namelist,group)#查找群成员
#record_search()#查找聊天记录(登录以后的)

