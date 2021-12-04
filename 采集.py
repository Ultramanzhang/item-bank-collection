import requests
import jsonpath
import json
import random
import time
import xlwt

# 创建两个空的链表，其中question用来存放所有的题目，answer用来存放所有的答案
question = []
answer = []
intervalMin = 0
intervalMax = 1.0
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Referer': 'http://gjaqjs.haedu.cn/',
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}


def main():
    danxuan(headers)
    duoxuan(headers)
    panduan(headers)
    save()


def danxuan(headers):
    for i in range(16):
        url = 'http://gjaqjs.haedu.cn/data/gjaqzsjsxxzl_danxuan/gjaqzsjsxxzl_danxuan_{}.json'.format(i + 1)
        r = requests.get(url=url, headers=headers)
        # 将获取到的代码进行解码操作
        html_str = r.content.decode("utf-8")
        # 解码json对象
        json1 = json.loads(html_str)
        # 在json文件中找出对应值，question 和 answer
        ti = jsonpath.jsonpath(json1, '$..question')
        # 将题目添加到question链表中
        for temp in ti:
            question.append(temp)
        ti1 = jsonpath.jsonpath(json1, '$..answer')
        # 将题目添加到answer链表中
        for temp in ti1:
            answer.append(temp)
        # 为避免请求过快导致封禁，所以使用随机睡眠
        time.sleep(random.uniform(intervalMin, intervalMax))


def duoxuan(headers):
    for i in range(9):
        url = 'http://gjaqjs.haedu.cn/data/gjaqzsjsxxzl_duoxuan/gjaqzsjsxxzl_duoxuan_{}.json'.format(i + 1)
        r = requests.get(url=url, headers=headers)
        # 将获取到的代码进行解码操作
        html_str = r.content.decode("utf-8")
        # 解码json对象
        json1 = json.loads(html_str)
        # 在json文件中找出对应值，question 和 answer
        ti = jsonpath.jsonpath(json1, '$..question')
        # 将题目添加到question链表中
        for temp in ti:
            question.append(temp)
        ti1 = jsonpath.jsonpath(json1, '$..answer')
        # 将题目添加到answer链表中
        for temp in ti1:
            answer.append(temp)
        # 为避免请求过快导致封禁，所以使用随机睡眠
        time.sleep(random.uniform(intervalMin, intervalMax))


def panduan(headers):
    for i in range(11):
        url = 'http://gjaqjs.haedu.cn/data/gjaqzsjsxxzl_panduan/gjaqzsjsxxzl_panduan_{}.json'.format(i + 1)
        r = requests.get(url=url, headers=headers)
        # 将获取到的代码进行解码操作
        html_str = r.content.decode("utf-8")
        # 解码json对象
        json1 = json.loads(html_str)
        # 在json文件中找出对应值，question 和 answer
        ti = jsonpath.jsonpath(json1, '$..question')
        # 将题目添加到question链表中
        for temp in ti:
            question.append(temp)
        ti1 = jsonpath.jsonpath(json1, '$..answer')
        # 将题目添加到answer链表中
        for temp in ti1:
            answer.append(temp)
        # 为避免请求过快导致封禁，所以使用随机睡眠
        time.sleep(random.uniform(intervalMin, intervalMax))


def save():
    f = xlwt.Workbook(encoding='utf-8')
    sheet = f.add_sheet("sheet1", cell_overwrite_ok=True)
    # 写入数据
    sheet.write(0,0,"问题")
    sheet.write(0,1,"正确答案")
    i = 1
    for temp in question:
        sheet.write(i, 0, temp)
        i = i + 1
    i = 1
    for temp in answer:
        sheet.write(i, 1, temp)
        i = i + 1
    f.save("题库1.xls")


# 实现自适应列宽，暂时未完成
def get_max_col(max_list):
    line_list = []
    # 表示行，j表示列
    for j in range(len(max_list[0])):
        line_num = []
        for i in range(len(max_list)):
            line_num.append(max_list[i][j])  # 将每列的宽度存入line_num
        line_list.append(max(line_num))  # 将每列最大宽度存入line_list
        return line_list


if __name__ == "__main__":
    main()
