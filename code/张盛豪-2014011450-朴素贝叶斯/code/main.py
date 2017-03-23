# coding:utf-8

import random
from Naive_Bayes import begin
import config


def test_size():
    print "测试训练集规模对分类效果的影响"

    # ignore 指忽略掉的特征值编号
    ignore = [2, 4, 7, 13, 9, 8, 12]

    # 5%训练集
    train_per = 0.05
    test_per = 0.0
    # 参数含义详见Naive_Bayes.begin函数
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    # 50% 训练集
    train_per = 0.5
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    # 100% 训练集
    train_per = 1.0
    begin(train_per=train_per, test_per=test_per, ignore=ignore)


def test_random():
    # 重复五次进行随机抽取训练集测试
    config.if_random = True
    ignore = [2, 4, 7, 13, 9, 8, 12]

    test_per = 0.0
    train_per = 0.5
    while True:
        # 训练集百分百随机生成,要求大于0
        train_per = random.random()
        if train_per > 0.0:
            break
    begin(train_per=train_per, test_per=test_per, ignore=ignore)
    config.if_random = False


def test_lambda():
    ignore = [2, 4, 7, 13, 9, 8, 12]
    train_per = 0.5
    test_per = 0.0

    config.Lambda = 0.0
    print 'Lambda: ', config.Lambda
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.Lambda = 1.0
    print 'Lambda: ', config.Lambda
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.Lambda = 2.0
    print 'Lambda: ', config.Lambda
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.Lambda = 1.0


def test_age():
    ignore = [2, 4, 7, 13, 9, 8]
    train_per = 1.0
    test_per = 0.0

    print '年龄不做分割'
    config.age_step = 1
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '年龄分割粒度为3'
    config.age_step = 3
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '年龄分割粒度为5'
    config.age_step = 5
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '年龄分割粒度为10'
    config.age_step = 10
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.age_step = 5


def test_hour():
    ignore = [2, 4, 7, 13, 9, 8]
    train_per = 1.0
    test_per = 0.0

    print '工作时间不做分割'
    config.hour_step = 1
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '工作时间分割粒度为3'
    config.hour_step = 3
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '工作时间分割粒度为5'
    config.hour_step = 5
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '工作时间分割粒度为10'
    config.hour_step = 10
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.hour_step = 5


def test_capital():
    ignore = [2, 4, 7, 13, 9, 8]
    train_per = 1.0
    test_per = 0.0
    print '投资收益损失不做分割'
    config.capital_step = 1
    config.capital_if_step = True
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '投资收益损失以1000等距离散'
    config.capital_step = 1000
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '投资收益损失以 无,低,高分割'
    config.capital_if_step = False
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.capital_step = 1000
    config.capital_if_step = False


def test_miss():
    ignore = [2, 4, 7, 13, 9, 8, 12]
    train_per = 1.0
    test_per = 0.0

    print '忽略掉?'
    config.ignore_miss = True
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '将?视为新类型'
    config.ignore_miss = False
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    config.ignore_miss = True


def test_attrs():
    train_per = 1.0
    test_per = 0.0

    # '不忽略任何特征'
    ignore = []
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    # 忽略fnlwgt, education_num
    ignore = [2, 4]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    # 忽略fnlwgt, education_num, race
    ignore = [2, 4, 8]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 9, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 8, 9, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 8, 9, 12, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 3, 7, 8, 9, 10, 11, 12, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 8, 9, 10, 11, 12, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)


def test_Crossvalidation():
    ignore = [2, 4, 7, 13, 9, 8, 12]
    train_per = 0.5

    print '不加入测试集数据'
    test_per = 0.0
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '5%测试集数据'
    test_per = 0.05
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '50%测试集数据'
    test_per = 0.50
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    print '100%测试集数据'
    test_per = 1.0
    begin(train_per=train_per, test_per=test_per, ignore=ignore)


if __name__ == '__main__':

    # 测试集规模影响
    test_size()

    # 测试随机序列
    print '测试随机选取训练集的训练效果, 重复5次'
    for i in range(0, 5):
        test_random()

    print '拉普拉斯平滑'
    test_lambda()

    print '测试数据的离散化效果'
    print '年龄离散度的影响'
    test_age()
    print '工作时间离散度的影响'
    test_hour()
    print '投资收益损失的影响'
    test_capital()

    print '测试missing attrs'
    test_miss()

    print '测试选取的特征对分类效果的影响'
    test_attrs()

    print '在训练集中加入一定的测试集数据'
    test_Crossvalidation()
