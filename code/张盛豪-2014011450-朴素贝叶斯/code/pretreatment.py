# coding:utf-8
import config
import numpy

def treat(before_train, after_train, train_per, before_test, after_test, test_per, ignore):
    """
    获取提取后的数据集
    :param before_train: 原始训练集
    :param after_train: 处理后的训练集
    :param train_per: 处理后训练集中原始训练集占的比例
    :param before_test: 原始测试集
    :param after_test: 处理后测试集
    :param test_per: 处理后训练集中测试集的比例
    :param ignore: 忽略掉的特征
    :return:
    """
    # 获取所有的输入数据,测试集和训练集
    lines_train = None
    lines_test = None
    with open(before_train) as in_train:
        lines_train = in_train.readlines()
    with open(before_test) as in_test:
        lines_test = in_test.readlines()

    # 训练集中训练集的数量,测试集中的数量
    len_train = int(train_per * float(len(lines_train)))
    len_test = int(test_per * float(len(lines_test)))

    # 测试集的组成部分
    count_test = 0
    with open(after_test, 'w') as out_test:
        for i in range(0, len(lines_test)):
            line = lines_test[i]
            if '?' in line and config.ignore_miss:
                continue
            # else:
            #    line.replace('?', str(-100))
            line = do_split(line, ignore)
            out_test.writelines(line)
            count_test += 1

    # 训练集的组成部分
    count_train = 0
    # 训练集中原始训练集数目
    train_train = 0
    # 训练集中原始测试集的数目
    train_test = 0
    with open(after_train, 'w') as out_train:
        # 顺序抽取训练集
        train_list = [x for x in range(0, len(lines_train))]
        test_list = [x for x in range(0, len(lines_test))]
        if config.if_random:
            # 随机抽取训练集
            train_list = list(numpy.random.permutation(len(lines_train)))
            test_list = list(numpy.random.permutation(len(lines_test)))

        for i in range(0, len_train):
            line = lines_train[train_list[i]]
            if '?' in line and config.ignore_miss:
                continue
            # else:
            #    line.replace('?', str(-100))
            line = do_split(line, ignore)
            out_train.writelines(line)
            count_train += 1
            train_train += 1

        for i in range(0, len_test):
            line = lines_test[test_list[i]]
            if '?' in line and config.ignore_miss:
                continue
            # else:
            #    line.replace('?', str(-100))
            line = do_split(line, ignore)
            out_train.writelines(line)
            count_train += 1
            train_test += 1
        print '训练比例:', '\t\tadult.train:', train_per, '\t\t\tadult.test:', test_per
        print '训练集:',  '\t\t\tadult.train:', train_train, '\t\t\tadult.test:', train_test, '\t\t\t', count_train, '条数据'
        print '测试集:',  '\t\t\tadult.train:', 0, '\t\t\t\tadult.test:', count_test, '\t\t\t', count_test, '条数据'


def do_split(line, ignore):
    """
    对数据进行处理
    :param line:
    :return:
    """
    # 以空格分割每一行的数据
    line = line.replace("\n", "")
    line = line.replace(".", "")
    line = line.replace("Never-worked", "Without-pay")
    cols = line.split(',')
    # 年龄进行离散
    cols[0] = str(int((int(cols[0])-17)/config.age_step))
    # 工作时间进行离散
    cols[12] = str(int(int(cols[12]) / config.hour_step))
    """
    | **变量名**		| **范围**	| **分割粒度**		|
    | -------------	| ---------	| ---------------	|
    | age			| 17~90		| 5					|
    | capital_gain	| 0 ~ 99999	| 0，0~7298，7298+	|
    | capital_loss	| 0 ~ 4356	| 0，0~1887， 1887+	|
    | hours_per_week| 1~99 		| 5 				|
    """
    cols[10] = int(cols[10])
    cols[11] = int(cols[11])

    if config.capital_if_step:
        # 投资收益与损失等间距离散
        cols[10] = int(cols[10]) / config.capital_step
        cols[11] = int(cols[11]) / config.capital_step
    else:
        # 投资收益与损失按 无,低,高进行离散
        if cols[10] <= 0:
            cols[10] = 0
        if 0 < cols[10] < config.gain_middle:
            # 收益低
            cols[10] = 1
        else:
            if cols[10] >= config.gain_middle:
                cols[10] = 2

        if cols[11] <= 0:
            cols[11] = 0
        if 0 < cols[11] < config.loss_middle:
            # 损耗低
            cols[11] = 1
        else:
            if cols[11] >= config.loss_middle:
                cols[11] = 2

    cols[10] = str(cols[10])
    cols[11] = str(cols[11])
    result = cols[0]
    for i in range(1, 15):
        if i not in ignore:
            result += ',' + cols[i]
    # print cols
    result += "\n"
    # print result
    return result
