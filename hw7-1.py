# _*_coding=utf8_*_
import operator


def find_word_after_keyword(lines_list, keyword):
    count_dic = {}
    for i in lines_list:
        g = -1
        while True:
            position = i.find(keyword, g + 1)
            if position == -1:
                break
            if position+len(keyword)+1 > len(i):
                break
            else:
                word = i[position + len(keyword)]  # 找尋關鍵字後一個字
            if word not in count_dic:
                count_dic[word] = 1
            else:
                count_dic[word] += 1
            g = position
    count_list = sorted(count_dic.items(),  # 將關鍵字dic由大到小排序 再用中文內碼排序
                        key=operator.itemgetter(1, 0), reverse=True)
    # print(count_list)
    return count_list


def find_word_before_keyword(lines_list, keyword):
    count_dic = {}
    for i in lines_list:
        g = 0
        while True:
            position = i.find(keyword, g + 1)
            if position == -1:
                break
            else:
                word = i[position-1]  # 找尋關鍵字的前一個字
            if word not in count_dic:
                count_dic[word] = 1
            else:
                count_dic[word] += 1
            g = position
    count_list = sorted(count_dic.items(),  # 將關鍵字dic由大到小排序 再用中文內碼排序
                        key=operator.itemgetter(1, 0), reverse=True)
    # print(count_list)
    return count_list


file_path = input()
keyword = input()
# 讀檔將檔案處理成應該要的樣子 然後append到list裡
with open(file=file_path, mode="r", encoding="utf-8") as f:
    new_lines_list = []
    lines_list = f.readlines()
    for i in lines_list:
        line = i.strip()
        line = line.replace("\n", "")  # 將換行字元除掉
        for g in line.split("\t"):  # 以\t為界線 分別問句答句
            new_lines_list.append(g.strip())

word1_list = find_word_before_keyword(lines_list=new_lines_list,
                                      keyword=keyword)
word2_list = find_word_after_keyword(lines_list=new_lines_list,
                                     keyword=keyword)

# 若長度不足十 則以當前數字計算
if len(word1_list) < 10:
    z = len(word1_list)
else:
    z = 10
if len(word2_list) < 10:
    x = len(word2_list)
else:
    x = 10

# 加上無關鍵字情況 仍要印出"熱門前一個字:" "熱門下一個字:"
if z == 0:
    print("熱門前一個字:")
else:
    for i in range(z):
        if i == 0:
            print("熱門前一個字:\n%s---%s" % (word1_list[i][0], keyword))
        else:
            prints = "%s---%s" % (word1_list[i][0], keyword)
            print(prints)

if x == 0:
    print("熱門下一個字:")
else:
    for i in range(x):
        if i == 0:
            print("熱門下一個字:\n%s---%s" % (keyword, word2_list[i][0]))
        else:
            prints = "%s---%s" % (keyword, word2_list[i][0])
            print(prints)

'''
/Users/davidding/Downloads/Gossiping-QA-Dataset.txt
今天
'''