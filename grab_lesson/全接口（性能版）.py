import requests, time, json
from bs4 import BeautifulSoup
from selenium import webdriver
from threading import Thread


def welcome():
    print(
        '''
    欢迎使用西安交大自助抢选课程序,祝你好运！

    Welcome to the XJTU-Grab-Lessons program, wish you good luck!
    '''
    )
    time.sleep(1)


# 显示功能面板
def show_funtions():
    print('''
    请选择：

    1.查询主修课程

    2.查询选修课程

    3.查询形势与政策/体育课程

    4.查看当前课表

    5.退选课程

    6.退出
    ''')


# 方法选择
def choose_funtion(choice):
    while True:
        if choice == 1:
            key = int(input('''
            1.查询全部课程

            2.查询不冲突课程

            '''))
            if key == 1:
                get_recommendedCourse_list()
            else:
                get_available_recommendedCourse_list()
        elif choice == 2:
            key = int(input('''
            1.查询全部课程

            2.查询不冲突课程

            '''))
            if key == 1:
                get_publicCourse_list()
            else:
                get_available_publicCourse_list()
        elif choice == 3:
            key = int(input('''
            1.查询全部课程

            2.查询不冲突课程

            '''))
            if key == 1:
                get_programCourse_list()
            else:
                get_available_programCourse_list()
        elif choice == 4:
            show_my_courses()
        elif choice == 5:
            my_courses_list = show_my_courses()
            loc = (input('请输入退选课程序号：'))
            delete_course(loc, my_courses_list)
        elif choice == 7:
            my_list = get_recommendedCourse_list()
            course_id = int(input('ID='))
            select_course(course_id, my_list, headers)
        else:
            print('exit')
            break
        print('continue')


# 输入用户信息及选课批次
student_ID = '2186114147'  # input('请输入学号')
Pass_word = 'lchAK47.423'  # input('请输入密码')
electiveBatchCode = "01ffc28d54e1452cbf1e954ccd138ab9"


# 获取登录Cookie
def get_cookie(my_id, my_psw):
    driver = webdriver.Chrome()
    # driver.minimize_window()
    driver.get("http://xkfw.xjtu.edu.cn/")
    # print(driver.current_url)
    # driver.get_screenshot_as_file("111.png")
    # print(driver.page_source)
    user_name = driver.find_element_by_xpath(r'//*[@id="form1"]/input[1]')
    user_name.send_keys(my_id)
    pass_word = driver.find_element_by_xpath(r'//*[@id="form1"]/input[2]')
    pass_word.send_keys(my_psw)
    button_3 = driver.find_element_by_xpath(r'//*[@id="account_login"]')
    button_3.click()
    while driver.current_url != "http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/*default/index.do":
        time.sleep(1)
    cookie = driver.get_cookies()
    driver.close()
    jsonCookies = json.dumps(cookie)
    with open('jwc.json', 'w') as f:
        f.write(jsonCookies)
    with open('jwc.json', 'r', encoding='utf-8') as f:
        listCookies = json.loads(f.read())
    cookie = [item["name"] + "=" + item["value"]
              for item in listCookies]
    cookiestr = '; '.join(item for item in cookie)
    return cookiestr


cookies = get_cookie(student_ID, Pass_word)


# 获取token
def get_token(cookies=cookies):
    url_gettoken = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/student/register.do?number=' + student_ID
    headers_1 = {
        'Cookie': cookies
    }
    res = requests.get(url_gettoken, headers=headers_1).json()
    token = res['data']['token']
    return token


headers = {
    'Cookie': cookies,
    'token': get_token()
}

# 初始界面
welcome()
show_funtions()


# 获取课程信息列表(形策体育)
def get_programCourse_list(headers=headers):
    mode = input('请输入要选择的课程类型(1.形势与政策 2.体育):')
    if mode == '1':
        mode = 'FANKC'
    else:
        mode = 'TYKC'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do'
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"0","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
    except:
        print('该课程为空！')
        return
    course_list = ['']
    count = 1
    for course in courses_list:
        courseName = course['courseName']
        courses = course['tcList']
        for course in courses:
            print(str(count) + '.  ', end='  ')
            count += 1
            course_list.append([course['teachingClassID'], mode])
            print(courseName, end='  ')
            print(course['teacherName'], end='  ')
            print(course['teachingClassID'], end='  ')
            print(course['teachingPlace'])
            conflict = course['conflictDesc']
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量' + course['classCapacity'], end='  ')
            print('已选人数' + course['numberOfSelected'], end='  ')
            print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list


# 获取不冲突课程信息列表(形策体育)
def get_available_programCourse_list(headers=headers):
    mode = input('请输入要选择的课程类型(1.形势与政策 2.体育):')
    if mode == '1':
        mode = 'FANKC'
    else:
        mode = 'TYKC'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do'
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"0","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
    except:
        print('该课程为空！')
        return
    course_list = ['']
    count = 1
    for course in courses_list:
        courseName = course['courseName']
        courses = course['tcList']
        for course in courses:
            conflict = course['conflictDesc']
            if conflict:
                continue
            else:
                pass
            print(str(count) + '.  ', end='  ')
            count += 1
            course_list.append([course['teachingClassID'], mode])
            print(courseName, end='  ')
            print(course['teacherName'], end='  ')
            print(course['teachingClassID'], end='  ')
            print(course['teachingPlace'])
            conflict = course['conflictDesc']
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量' + course['classCapacity'], end='  ')
            print('已选人数' + course['numberOfSelected'], end='  ')
            print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list


# 获取课程信息列表(选修)
def get_publicCourse_list(headers=headers):
    mode = 'XGXK'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/publicCourse.do'
    page = 0
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
            page) + '","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        total = int(res['totalCount'])
        pages = int(total / 10) + 1
    except:
        print('该课程为空！')
        return
    count = 1
    for page in range(pages):
        data = {
            'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
                page) + '","order":""}'
        }
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        course_list = ['']
        for course in courses_list:
            print(str(count) + '.  ', end='  ')
            count += 1
            course_list.append([course['teachingClassID'], mode])
            print(course['courseName'], end='  ')
            print(course['teacherName'], end='  ')
            print(course['teachingClassID'], end='  ')
            print(course['teachingPlace'])
            conflict = course['conflictDesc']
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量' + course['classCapacity'], end='  ')
            print('已选人数' + course['numberOfSelected'], end='  ')
            print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list


# 获取不冲突课程信息列表(选修)
def get_available_publicCourse_list(headers=headers):
    mode = 'XGXK'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/publicCourse.do'
    page = 0
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
            page) + '","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        total = int(res['totalCount'])
        pages = int(total / 10) + 1
    except:
        print('该课程为空！')
        return
    count = 1
    for page in range(pages):
        data = {
            'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
                page) + '","order":""}'
        }
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        course_list = ['']
        for course in courses_list:
            conflict = course['conflictDesc']
            if conflict:
                continue
            else:
                pass
            print(str(count) + '.  ', end='  ')
            count += 1
            course_list.append([course['teachingClassID'], mode])
            print(course['courseName'], end='  ')
            print(course['teacherName'], end='  ')
            print(course['teachingClassID'], end='  ')
            print(course['teachingPlace'])
            conflict = course['conflictDesc']
            if conflict:
                print(course['conflictDesc'])
            else:
                print('不冲突')
            print('课程容量' + course['classCapacity'], end='  ')
            print('已选人数' + course['numberOfSelected'], end='  ')
            print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
            print('-------------------------------------')
    return course_list


# 获取课程信息列表(主修)
def get_recommendedCourse_list(headers=headers):
    mode = 'TJKC'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/recommendedCourse.do'
    page = 0
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
            page) + '","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        total = int(res['totalCount'])
        pages = int(total / 10) + 1
    except:
        print('该课程为空！')
        return
    count = 1
    for page in range(pages):
        data = {
            'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
                page) + '","order":""}'
        }
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        course_list = ['']
        for course1 in courses_list:
            courseName = course1['courseName']
            courses = course1['tcList']
            for course in courses:
                print(str(count) + '.  ', end='  ')
                count += 1
                course_list.append([course['teachingClassID'], mode])
                print(courseName, end='  ')
                print(course['teacherName'], end='  ')
                print(course['teachingClassID'], end='  ')
                print(course['teachingPlace'])
                conflict = course['conflictDesc']
                if conflict:
                    print(course['conflictDesc'])
                else:
                    print('不冲突')
                print('课程容量' + course['classCapacity'], end='  ')
                print('已选人数' + course['numberOfSelected'], end='  ')
                print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
                print('-------------------------------------')
    return course_list


# 获取不冲突课程信息列表(主修)
def get_available_recommendedCourse_list(headers=headers):
    mode = 'TJKC'
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/recommendedCourse.do'
    page = 0
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
            page) + '","order":""}'
    }
    try:
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        total = int(res['totalCount'])
        pages = int(total / 10) + 1
    except:
        print('该课程为空！')
        return
    count = 1
    for page in range(pages):
        data = {
            'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
                page) + '","order":""}'
        }
        res = requests.post(url, headers=headers, data=data).json()
        courses_list = res['dataList']
        course_list = ['']
        for course in courses_list:
            courseName = course['courseName']
            courses = course['tcList']
            for course in courses:
                conflict = course['conflictDesc']
                if conflict:
                    continue
                else:
                    pass
                print(str(count) + '.  ', end='  ')
                count += 1
                course_list.append([course['teachingClassID'], mode])
                print(courseName, end='  ')
                print(course['teacherName'], end='  ')
                print(course['teachingClassID'], end='  ')
                print(course['teachingPlace'])
                conflict = course['conflictDesc']
                if conflict:
                    print(course['conflictDesc'])
                else:
                    print('不冲突')
                print('课程容量' + course['classCapacity'], end='  ')
                print('已选人数' + course['numberOfSelected'], end='  ')
                print('剩余名额' + str(int(course['classCapacity']) - int(course['numberOfSelected'])))
                print('-------------------------------------')
    return course_list


# 查看课表
def show_my_courses(headers=headers):
    timestamp = str(int(time.time()))
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/courseResult.do?timestamp=' + timestamp + '&studentCode=' + student_ID + '&electiveBatchCode=' + electiveBatchCode
    my_courses = requests.get(url, headers=headers).json()
    my_courses = my_courses['dataList']
    print('课程列表')
    my_courses_list = ['']
    count = 1
    for course in my_courses:
        print(str(count) + '.', end='  ')
        count += 1
        print(course['courseName'], end='  ')
        print(course['teacherName'], end='  ')
        print(course['teachingClassID'])
        my_courses_list.append(course['teachingClassID'])
        print('')
    return my_courses_list


# 退课
def delete_course(ID, my_courses_list, headers=headers):
    teachingClassId = my_courses_list[ID][0]
    mode = my_courses_list[ID][1]
    timestamp = str(int(time.time()))
    param = {
        'deleteParam': '{"data":{"operationType":"2","studentCode":' + student_ID + ',"electiveBatchCode":"' + electiveBatchCode + '","teachingClassId":' + teachingClassId + ',"isMajor":"1","campus":"1","teachingClassType":"' + mode + '"}}',
        'timestamp': timestamp
    }
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/deleteVolunteer.do'
    res = requests.get(url, headers=headers, params=param)
    print('')
    print(res.json()['msg'])
    print('')


def select_course(ID, course_list, headers):
    teachingClassId = course_list[ID]
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do'
    param = {
        'addParam': '{"data":{"operationType":"1","studentCode":"' + student_ID + '",'
                                                                                  '"electiveBatchCode":"' + electiveBatchCode + '","teachingClassId":' + teachingClassId +
                    ',"isMajor":"1","campus":"1","teachingClassType":"TJKC"}} '
    }
    res = requests.post(url, headers=headers, params=param)
    print('')
    print(res.json()['msg'])
    print('')
    if int(res.json()['code']) == 2:
        return 0
    else:
        return 1
    time.sleep(1)


# 抢课
def grab_lessons(ID, course_list, headers=headers):
    print('正在持续查询中：')
    teachingClassId = course_list[ID][0]
    mode = course_list[ID][1]
    url = 'http://xkfw.xjtu.edu.cn/xsxkapp/sys/xsxkapp/elective/programCourse.do'
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"0","order":""}'
    }
    times = 1
    while True:
        try:
            res = requests.post(url, headers=headers, data=data).json()
            avialable_course = res['dataList']
            for course in avialable_course:
                detial = course['tcList']
                for member in detial:
                    target_classID = member['teachingClassID']
                    if teachingClassId == target_classID:
                        total_number = int(member['classCapacity'])
                        selected_number = int(member['numberOfSelected'])
                        available_number = total_number - selected_number
                        if available_number >= 1:
                            outcome = select_course(ID, course_list, headers)
                            if outcome == 0:
                                print('容量剩余，但你无法选择此课程')
                                return 0
                            elif outcome == 1:
                                print('抢课成功，查询结束')
                                return 1
                        elif available_number == 0:
                            print('容量已满，继续查询中，已查询次数：', times)
                            times = times + 1
                            time.sleep(1)
                            continue
        except:
            print('网络异常正在重试。。。')
            pass

if __name__ == '__main__':

    choice = int(input())
    choose_funtion(choice)
