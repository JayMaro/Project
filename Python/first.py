import requests
from bs4 import BeautifulSoup as bs

#url1
url= "http://ncov.mohw.go.kr/en/"
response = requests.get(url)
res = bs( response.content, 'html.parser' )

#url2
url2 = 'http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=161&dataGubun=&ncvContSeq=&contSeq=&board_id='
response2 = requests.get(url2)
res2 = bs( response2.content, 'html.parser' )

#url3
url3 = 'http://ncov.mohw.go.kr/en/bdBoardList.do?brdId=16&brdGubun=163&dataGubun=&ncvContSeq=&contSeq=&board_id=&gubun='
response3 = requests.get(url3)
res3 = bs( response3.content, 'html.parser' )



def p1():
    print('P1.')
    #
    # Your Code
    #
    print('Student ID : 2014310703\nStudent Name : Kim Jin Kyu')
    print()

def p2():
    print('P2.')
    #
    # Your Code
    #
    daily = res.find('div', {'class': 'mpsl_b'})
    daily_ch = daily.find('em')
    daily_num = daily.find('span')
    print(daily_ch.get_text(),':' ,daily_num.get_text())
    print()
    
def p3():
    print('P3.')
    #
    # Your Code
    #
    CC = res.find('div', {'class': 'mpsl_c'})
    CC_num = CC.find('span')
    print('Confirmed Cases (accumulation) :',CC_num.get_text())
    print()
   
def p4(): 
    print('P4.')
    #
    # Your Code
    #
    ICC = res2.find_all('table', {'class': 'num'})
    ICC_tr = ICC[1].find_all('tr')
    ICC_China = ICC_tr[2].find('td')
    ICC_AsiaoutsideChina = ICC_tr[3].find('td')
    ICC_Europe = ICC_tr[4].find('td')
    ICC_America = ICC_tr[5].find('td')
    ICC_Africa = ICC_tr[6].find('td')
    ICC_Oceania = ICC_tr[7].find('td')
    print('China Daily Change :', ICC_China.get_text())
    print('AsiaoutsideChina Daily Change :', ICC_AsiaoutsideChina.get_text())
    print('Europe Daily Change :', ICC_Europe.get_text())
    print('America Daily Change :', ICC_America.get_text())
    print('Africa Daily Change :', ICC_Africa.get_text())
    print('Oceania Daily Change :', ICC_Oceania.get_text())

    print()


def p5():
    print('P5.')
    #
    # Your Code
    #
    Region = []
    GS = res3.find('table', {'class': 'num'}).find('tbody')
    GS_th = GS.find_all('th', {'scope': 'row'})
    for region in GS_th[:-1]:
        Region.append(region.get_text())

    Country = {}
    Asia = {}
    Middle_East = {}
    America = {}
    Europe = {}
    Oceania = {}
    Africa = {}
    Others = {}

    GS_tr = GS.find_all('tr')

    def con(num1, num2, Count):
        for country in GS_tr[num1:num2]:
            GS_td = country.find_all('td')
            td1 = GS_td[1].get_text().replace('\r', '')
            td1 = td1.replace('\t', '')
            td1 = td1.replace('\n', '')
            td1 = td1.replace(',', '')
            Con = td1.split('(')
            if len(Con) == 2:
                Con[1] = Con[1].replace(')', '')
                Con[1] = Con[1].replace('Deceased ', '')
            num = list(map(int, Con))
            Count[GS_td[0].get_text()] = num

    def Mortality(num1, num2, Count):
        for country in GS_tr[num1:num2]:
            GS_td = country.find_all('td')
            td1 = GS_td[1].get_text().replace('\r', '')
            td1 = td1.replace('\t', '')
            td1 = td1.replace('\n', '')
            td1 = td1.replace(',', '')
            Con = td1.split('(')
            if len(Con) == 2:
                Con[1] = Con[1].replace(')', '')
                Con[1] = Con[1].replace('Deceased ', '')
            num = list(map(int, Con))
            if len(num) == 2:
                Count[GS_td[0].get_text()] = (round((num[1] / num[0]), 3) * 100)
            else:
                Count[GS_td[0].get_text()] = 0

    con(0, 30, Asia)
    con(30, 48, Middle_East)
    con(48, 83, America)
    con(83, 131, Europe)
    con(131, 135, Oceania)
    con(135, 184, Africa)
    con(184, 185, Others)
    Mortality(0, 185, Country)

    def reg(name):
        if name == 'Asia':
            return Asia

        if name == 'Middle East':
            return Middle_East

        if name == 'America':
            return America

        if name == 'Europe':
            return Europe

        if name == 'Oceania':
            return Oceania

        if name == 'Africa':
            return Africa

        if name == 'Others':
            return Others

    def regis(name):
        regname = reg(name)
        print('There are {0} countries.'.format(len(regname)))
        sum = 0
        for x, y in regname.items():
            sum += y[0]
        print('Sum of Confirmed Cases : {0}'.format(sum))
        ky = max(regname.keys(), key=(lambda k: regname[k]))

        print('Highest Confirmed Case Country : {} {}'.format(ky, regname[ky][0]))
        print()

    def Input_R():
        try:
            R_name = input('Enter a Region Name (Asia, Middle East, America, Europe, Oceania, Africa, Others) : ')
            regis(R_name)
            return R_name
        except:
            print('There is no Region "{}" try again'.format(R_name))
            return Input_R()

    flag = 1
    while 1:
        if flag == 0:
            break

        R_name = Input_R()

        while 1:
            C_name = input('Enter a Country Name in {} : '.format(R_name))
            if C_name == 'back':
                break
            if C_name == 'stop':
                flag = 0
                break

            case = 0

            for name in reg(R_name).keys():
                if C_name == name:
                    case = 1
                    if len(reg(R_name)[C_name]) == 2:
                        print(C_name, ':', reg(R_name)[C_name][0], '(Deceased {})'.format(reg(R_name)[C_name][1]))
                    else:
                        print(C_name, ':', reg(R_name)[C_name][0])
            if case == 0:
                print('There is no Country "{}" try agian'.format(C_name))
            print()
    print()
    mortality = sorted(Country.items(), key=lambda x: x[1], reverse=True)
    for x, y in mortality:
        if round(y, 1) > 5:
            print("{} : {}".format(x, round(y, 1)))


    print()

def p6():
    print('P6.')
    #
    # Your Code
    #
    def search(keyword):
        url4 = 'http://ncov.mohw.go.kr/en/tcmBoardList.do?pageIndex=&brdId=12&brdGubun=125&board_id=&search_item=1&search_content={}'.format(
            keyword)
        response4 = requests.get(url4)
        res4 = bs(response4.content, 'html.parser')
        return res4

    res4 = search('')
    count = res4.find('p',{'class':'bt_count'})
    strong = count.find('strong')
    print('There are {} articles.'.format(strong.get_text()))
    print()

    def Article(keyword):
        res4 = search(keyword)
        count = res4.find('p',{'class':'bt_count'})
        strong = count.find('strong')
        articles.append(int(strong.get_text()))
    
    while 1:
        keyword = input('Enter a keyword : ')
        if keyword == 'ilovepython':
            print('exit')
            break
        cap = keyword.capitalize()
        Upper = keyword.upper()
        Lower = keyword.lower()
        LC = Lower.capitalize()
        articles = []
        Article(keyword)
        Article(cap)
        Article(Upper)
        Article(Lower)
        Article(LC)
        print('There are {} articles.'.format(max(articles)))
        print()
        
        
    print()


#
# Your Code
#


# Call Only the Functions YOU SOLVED
#p1()
#p2()
#p3()
#p4()
#p5()
#p6()

