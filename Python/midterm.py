#과제 3 2014310703 김진규
num = int(input())
chart = []
VE_chart = []
interval_chart = []
list_in = []
visit_error = []
exit_error = []
#VE_chart를 0으로 초기화
for i in range(24):
    VE_chart.append([0,0])
    
#입력값들을 리스트로 만듦(시간형식도 함께 수정)
def list_set(list):
    list[0] = int(list[0])
    list[2] = list[2].split(':')
    list[2][0] = int(list[2][0])
    list[2][1] = int(list[2][1])
    if len(list)==4:
        if list[3] == "am":
            del list[3]
        elif list[3] == "pm":
            if list[2][0]>=12:
                del list[3]
            else:
                list[2][0] += 12
                del list[3]
    return
def time_set(i):
    if chart[i][2][0]<chart[i-1][2][0]:
        chart[i][2][0]+=12
    return
#function 0,1
#시간별 VE 값들 추가=====================================================
def VE_set(time,VE):
    if VE == 'V':
        VE_chart[time][0] += 1
    elif VE == 'E':
        VE_chart[time][1] += 1

#최대값을 갖는 VE 시간대 찾기
def search_VE():
    V_max=0
    V_index=0
    E_max=0
    E_index=0

    for i in range(24):
        if VE_chart[i][0]>V_max:
            V_max = VE_chart[i][0]
            V_index = i

        if VE_chart[i][1]>E_max:
            E_max = VE_chart[i][1]
            E_index = i
    return V_index,E_index,V_max,E_max
#==========================================================================
#function 2================================================================
#방문한 간격 계산
def set_interval(chart,i):
    if chart[i][1] == 'E':
        return [100,100]
    HH = chart[i][2][0]-chart[i-1][2][0]
    MM = chart[i][2][1]-chart[i-1][2][1]
    if MM<0:
        HH-=1
        MM+=60
    return [HH,MM]
#shortest interval 찾기
def search_Mitv():
    
    itv_min = 1000000
    itv_index = 0

    for i in range(1,num):
        if (interval_chart[i][0] * 60)+interval_chart[i][1]<itv_min:
            itv_min = (interval_chart[i][0] * 60)+interval_chart[i][1]
            itv_index = i
    return itv_index
#===========================================================================
#function 3,4===============================================================
#나가지 않고 재방문한 사람과 방문없이 나간사람  찾기
def VE_id(id,VE):
    if VE == 'V':
        
        if id in list_in:
            if not id in visit_error:
                visit_error.append(id)
        else:
            list_in.append(id)

    if VE == 'E':
        if id in list_in:
            list_in.remove(id)
        else:
            if not id in exit_error:
                exit_error.append(id)

#===========================================================================
#입력한 형태로 출력하는 함수(그냥 보기 편하게 만들어 봤습니다.)
def show_all():
    for i in chart:
        print(i[0],i[1],"{0:02d}:{1:02d}".format(i[2][0],i[2][1]))
    return

#입력값들로 chart를 만듦
for i in range(num):
    list = []
    list = input().split()
    list_set(list)
    chart.append(list)
    time_set(i)
    VE_set(list[2][0],list[1])
    interval_chart.append(set_interval(chart,i))
    VE_id(list[0],list[1])
    

V_index,E_index,V_max,E_max = search_VE()
itv_index = search_Mitv()




print(V_index, V_max)
print(E_index, E_max)
print(chart[itv_index-1][0],chart[itv_index][0],end=' ')
print("{0:02d}:{1:02d}".format(interval_chart[itv_index][0],interval_chart[itv_index][1]))
for i in visit_error:
    print(i,end=' ')
print()
for i in exit_error:
    print(i,end=' ')
print()

