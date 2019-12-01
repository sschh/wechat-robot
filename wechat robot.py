
# coding: utf-8

# In[4]:


from wxpy import *
import time


# ## 指定时间给指定人、群发送信息

# In[70]:


#date '11-24 00:00:00'
def minput(name,date,message):
    flag=0
    found=[]
    try:
        found=bot.friends().search(name)
        if not found:
            print('未找到好友') 
            bot.file_helper.send('未找到好友')
        else:
             #判断搜索和查找结果是否完全匹配
            for i in range(len(found)):
                if found[i].name==name:
                    name=found[i]
                    break
            if type(name)==str:
                print('未找到好友') 
                bot.file_helper.send('未找到好友') 
            else:
                print('好友已找到') 
                bot.file_helper.send('好友已找到')
                flag=1
    except ResponseError as e:
        print(e.err_code, e.err_msg) # 查看错误号和错误消息
        print('好友查找出错') 
        bot.file_helper.send('好友查找出错')
    if flag==0:
        try:
            found=bot.groups().search(name)
            if not found:
                print('未找到微信群') 
                bot.file_helper.send('未找到微信群')
            else:
                 #判断搜索和查找结果是否完全匹配
                for i in range(len(found)):
                    if found[i].name==name:
                        name=found[i]
                        break
                if type(name)==str:
                    print('未找到微信群') 
                    bot.file_helper.send('未找到微信群') 
                else:
                    print('微信群已找到') 
                    bot.file_helper.send('微信群已找到')
                    flag=2
        except ResponseError as e:
            print(e.err_code, e.err_msg) # 查看错误号和错误消息
            print('群查找出错') 
            bot.file_helper.send('群查找出错')
    if flag==0:return 0
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
def msend():
    name=input('请输入名字：')
    date=input('请输入日期（MM-DD hh:mm:ss）：')
    message=input('请输入发送信息：')
    minput(name,date,message)


# ### 查找群成员

# In[71]:


#name 部分关键字   group指定群
def gsearch(name,group):
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
        #判断搜索和查找结果是否完全匹配
        for i in range(len(found)):
            if found[i].name==group:
                group=found[i]
                break
        if type(group)==str:
            return '没有该群'
    for member in group:
        if name in member.name:
            result.append(member.name)
    return result

# ###查找聊天记录（登录后的）

# In[72]:


#记录消息类型、内容、发送人、接收时间
def search(message):
    bot.messages.max_history = 1000
    meslist=[]
    mesid=[]
    m=bot.messages.search(message)
    for mes in m:
        #查找消息ID，若已加入，则不管（不循环运行没必要判断）
        if med.id not in mesid:
            mesid.append(mes.id)
            meslist.append([mes.type,mes.text,mes.sender,mes.member,mes.receive_time.strftime("%Y-%m-%d %H:%M:%S")])
    print(meslist)
def recordsearch():
    message=input('请输入查找信息：')
    search(message)


bot=Bot(cache_path=True)#console_qr=1
#msend()#指定时间给指定好友、群发消息
#gsearch(name,group)#查找群成员
#recordsearch()#查找聊天记录(登录以后的)

