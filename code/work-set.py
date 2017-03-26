# coding: utf-8
# ! /usr/bin/env python

# 工作集页面置换算法

# 访存页面链表
work_list = []
# 工作集
work_set = set(work_list)
# 窗口大小
t = 4


def access(page):
    """
    访问页面函数,针对每一个页,进行工作集的更新,访存链表的更新,页面置换
    :param page:
    :return:
    """
    global work_set
    global work_list
    # 是否出现页缺失
    miss = False
    if page in work_set:
        # 当前页面在工作集中,表示命中
        print "命中页面"
    else:
        miss = True
        print "页缺失"
    work_list.append(page)
    # 删除第一个页面
    first = work_list[0]
    if len(work_list) > t:
        # 已经超出工作集,去除列表首页
        del work_list[0]
    work_set = set(work_list)
    if first not in work_set:
        print 'page %s 换出' % first
    if miss:
        print "page %s 换入" % page
    print "当前访存链表:", work_list
    print "当前工作集:", work_set


def access_pages(pages, input_work_list):
    global work_set
    global work_list
    work_list = input_work_list
    work_set = set(input_work_list)
    print "页面访问顺序为:", pages
    print "初始工作集:", work_set
    print "初始访问列表:", work_list
    pages = pages.split(',')
    count = 0
    for i in pages:
        count += 1
        print 'Page ', count, i,
        access(i)
        print ''
    # 访问完成之后清空
    work_list = []
    work_set = set(work_list)

if __name__ == '__main__':
    print "这是一个工作集置换算法的简单实现"

    log = '''
    t = 4
    test_pages = "c,c,d,b,c,e,c,e,a,d"
    test_work_str = "e,d,a"
    '''

    print "课件中测试集:", log
    t = input("窗口大小t=")
    assert (int(t) > 0)
    # 访问页面顺序
    test_pages = raw_input('测试页面顺序(以,隔开,如e,d,a,c,c) test_pages=')
    test_work_str = raw_input('此前访问的t个页面顺序为(如e,d,a)test_work_str=')
    test_work_list = test_work_str.split(',')
    print test_work_list
    assert (len(test_work_list) <= t)
    # test_pages = "e,d,a,c,c,d,b,c,e,c,e,a,d"
    access_pages(test_pages, test_work_list)

