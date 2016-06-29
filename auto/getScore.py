#author: Chenshufu
#date:2015年12月15日15:32:02
from urllib import request, parse
from http import cookiejar
from bs4 import BeautifulSoup

def getScoreText(x):
    return x.text.strip()

def getScore(htmldoc):
    soup = BeautifulSoup(htmldoc.read().decode('gbk'),'html.parser')
    tmp = soup.find_all('tr',onmouseout="this.className='even';")
    scoreList = []
    for x in tmp:
        scoreList.append(list(map(getScoreText,[x.contents[5],x.contents[11],x.contents[13],x.contents[9]])))
    return scoreList

def showScore(scoreList):
    lis = []
    for ele in scoreList:
        if ele[2] == '':
            ele[2] = "未发布"
        lis.append(ele[0]+'\n'+ele[1]+'\t'+ele[3]+'学分'+'\t'+ele[2])
    return lis

def initLoginData(username,passwd):
    login_data = parse.urlencode([
        ('zjh', username),
        ('mm', passwd),
    ])
    return login_data

#cookie操作 & 报表头
def initOpener():
    cookie = cookiejar.CookieJar()
    opener=request.build_opener(request.HTTPCookieProcessor(cookie))
    opener.addheaders = [
       ('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
    ,('Cache-Control','max-age=0')
    ,('Host','202.115.47.141')
    ,('Connection','keep-alive')
    ,('Origin', 'http://202.115.47.141')
    ,('DNT','1')
    ,('Content-Length','197')
    ,('Upgrade-Insecure-Requests','1')
    ,('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36')]
    return opener

Score_url = 'http://202.115.47.141/bxqcjcxAction.do'
Score_data = parse.urlencode([('totalrows','300'),
    ('pageSize', '300')])
login_url = 'http://202.115.47.141/loginAction.do'

class score():
    def __init__(self,username,pasward):
        self.username = username
        self.passwd = pasward
        self.lis = []

    def run(self):
        try:
            opener = initOpener()
            login_data = initLoginData(self.username,self.passwd)
            ht = opener.open(login_url,login_data.encode('gbk')) #登陆并获取cookie
            #print(ht.read().decode('gbk'))#debug测试
            htmldoc = opener.open(Score_url,Score_data.encode('gbk'))  #获取列表
            #print(htmldoc.read().decode('gbk'))
            self.lis = showScore(getScore(htmldoc))
            #print(tmp)
        except:
            print('失败了 ╮(╯▽╰)╭')
        return self.lis
