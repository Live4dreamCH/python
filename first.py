import json
if __name__ == '__main__':
    student_ID = '2186114147'
    electiveBatchCode = "01ffc28d54e1452cbf1e954ccd138ab9"
    mode = '10'
    page = 10
    data1 = {
        'querySetting': '\
        {\
            "data":\
            {\
                "studentCode":' + student_ID + ',\
                "campus":"1",\
                "electiveBatchCode":"' + electiveBatchCode + '",\
                "isMajor":"1",\
                "teachingClassType":"' + mode + '",\
                "checkConflict":"2",\
                "checkCapacity":"2",\
                "queryContent":""\
            },\
            "pageSize":"10",\
            "pageNumber":"' + str(page) + '",\
            "order":""\
        }'
    }
    data = {
        'querySetting': '{"data":{"studentCode":' + student_ID + ',"campus":"1","electiveBatchCode":"' + electiveBatchCode + '","isMajor":"1","teachingClassType":"' + mode + '","checkConflict":"2","checkCapacity":"2","queryContent":""},"pageSize":"10","pageNumber":"' + str(
            page) + '","order":""}'
    }
    data.json()
    print(data == data1)
    print(data, '\n')
    print(data1)
