#  김진규 2014310703 과제2

print("Let's go hiking!")

while 1:
    mount_height = int(input("Input height of mountain(m).\n"))  # 높이입력
    if mount_height > 100:
        break
    print("Wrong Input!")

while 1:
    time = int(input("Input what time you start hiking.\n"))  # 출발 시간 입력
    if time > 5 and time < 17:
        break
    print("Wrong Input!")

up_height = 0  # 올라온 높이
up_time = 0  # 올라간 시간

while 1:

    if time == 12:  # 점심시간
        print("Take some delicious lunch, between {} o'clock and {} o'clock. :^)".format(time, time+1))
        time += 1
        continue
    up = int(input("How far you climb between {} o'clock and {} o'clock(m).\n".format(time, time + 1)))  # 올라간 높이
    if not up > 0:
        print("Wrong Input!")
        continue
    if up > (mount_height-up_height):  # 너무 높이 올라갔어
        print("You can't climb the air, left to top: {}".format(mount_height-up_height))
        continue
    up_height += up  # 올라온 높이 계산
    time += 1  # 시간 증가
    up_time += 1  # 올라간 시간 증가
    if mount_height == up_height:  # 정상 도착
        print("Successful hiking today, Ya-ho!")
        break

    if time == 17:  # 도착 실패
        print("Fail to get to the top.")
        print("Do better next time. :^(")
        break

print("Total time you hiking: {} hours".format(up_time))  # 올라간 시간
print("How far you climb: {} meters".format(up_height))  # 올라간 높이
