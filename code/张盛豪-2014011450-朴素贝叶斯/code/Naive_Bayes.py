# coding:utf-8
import pretreatment
import config
from config import *


class NBC:
    def __init__(self, train_data, cols_names):
        """
        朴素贝叶斯分类器初始化,为了方便,可以指定训练和测试数据集文件
        :param train_data: 训练数据集文件
        :param cols_names: 选取的特征
        """
        # 训练集和测试集总数
        self.train_total = 0
        # 列标签
        self.tags = ['']
        # 先验概率
        self.pre_y = {}
        self.condition = {}

        # 我们使用字典来统计每个类别的次数,从而计算先验概率,扫描结果为:
        """
        # 第一行
        income_dict = {'<=50K.': 0}
        # All
        income_dict = {'<=50K.': x, '>50K.': y}
        """
        income_dict = {}
        # 我们使用嵌套字典统计后验概率
        # 为每个类别分别做统计
        cols_dict = {}

        # 进行统计
        with open(train_data) as train:
            lines = train.readlines()

        for line in lines:
            # 分离每一行的数据
            self.train_total += 1
            line = line.replace('\n', '')
            cols = line.split(',')
            length = len(cols)
            # 该数据的类型
            class_ = cols[length - 1]
            # 去除class, 得到特征值
            cols.pop(length - 1)

            """
            dict.setdefault(key, vlaue) 如果键值key还未出现,则设置为默认值value,
            第一条数据之后为:
            income_dict: {'<=50K': 0}
            cols_dict: {'<=50K': {}}
            cols_dict: {'<=50K': {'age': {'7': 1}}}
            cols_dict: {'<=50K': {'work_class': {'State-gov': 1}, 'age': {'7': 1}}}
            """
            income_dict.setdefault(class_, 0)
            cols_dict.setdefault(class_, {})
            income_dict[class_] += 1
            id = 0
            for value in cols:
                # 统计某个类型下的数据
                cols_dict[class_].setdefault(cols_names[id], {})
                # 设置某一个描述类型的结果统计初始值
                cols_dict[class_][cols_names[id]].setdefault(value, 0)
                cols_dict[class_][cols_names[id]][value] += 1
                id += 1
        self.col = dict(cols_dict)
        self.income = dict(income_dict)

        # 计算先验概率, class_dict中每一个类别出现的概率
        for income in income_dict.keys():
            self.pre_y[income] = float(income_dict[income]) / float(
                self.train_total)

        # 计算条件概率, P(xi | y = c), 当类型为c时,x出现的概率
        for income in income_dict.keys():
            self.condition.setdefault(income, {})
            for cols in cols_dict[income].keys():
                # 统计各个列目录下的概率
                self.condition[income].setdefault(cols, {})
                for value in cols_dict[income][cols].keys():
                    # 拉普拉斯平滑
                    n = float(
                        len(cols_dict[income][cols].keys())) * config.Lambda
                    # 计算收入为income时, cols列的取值为value的概率
                    self.condition[income][cols][value] = (float(
                        cols_dict[income][cols][
                            value]) + 1.0 * config.Lambda) / (float(
                        income_dict[income]) + n)

        # 数据读取完成之后, debug 设置为True可以输出先验概率和条件概率统计结果
        if config.debug:
            print "收入", '\t\t', "数量", '\t\t', '概率'
            for key in income_dict.keys():
                print key, '\t\t', income_dict[key], self.pre_y[key]

            print "\n\n"
            print "收入", '\t\t', '属性', '\t\t', '取值', '\t\t', '数量', '\t\t', '概率'
            for income in cols_dict.keys():
                for cols in cols_dict[income].keys():
                    ans = 0.0
                    for value in cols_dict[income][cols].keys():
                        ans += self.condition[income][cols][value]
                        print income, '\t\t', cols, '\t\t', value, '\t\t', \
                            cols_dict[income][cols][value], '\t\t', \
                            self.condition[income][cols][value]
                    print ans

    def test(self, test_data, cols_names):
        with open(test_data) as test:
            lines = test.readlines()
        accurate = 0
        count = 0
        for line in lines:
            count += 1
            answers = ""
            # total += 1
            incomes = ['<=50K', '>50K']
            ans = [0.0, 0.0]
            for i in range(0, 2):
                # 对于每一种收入,计算其概率值, 避免连乘误差,采用取对数加法
                ans[i] = self.pre_y[incomes[i]]
                line = line.replace('\n', '')
                cols = line.split(',')
                length = len(cols)
                answers = cols[length - 1]
                cols.pop(length - 1)
                id = 0
                for value in cols:
                    if value not in self.condition[incomes[i]][cols_names[id]]:
                        n = float(len(self.col[incomes[i]][
                                          cols_names[id]].keys())) * config.Lambda
                        ans[i] = ans[i] * (1.0 * config.Lambda) / (float(
                            self.income[incomes[i]]) + n)
                    else:
                        ans[i] = ans[i] * \
                                 self.condition[incomes[i]][cols_names[id]][
                                     value]
                    id += 1
            if ans[0] > ans[1]:
                if answers == '<=50K':
                    accurate += 1

            elif ans[0] < ans[1]:
                if answers == '>50K':
                    accurate += 1

        print "准确率:", '\t\t\t', float(accurate) / float(count)


def get_cols_name(ignores):
    names = []
    chi = []
    for i in range(0, len(origin_names)):
        if i not in ignores:
            names.append(origin_names[i])
            chi.append(chinese_names[i])
    return names, chi


def print_cols(names):
    print '特征值\t\t\t',
    for i in range(0, len(names)):
        print names[i],
    print '\n',


def begin(train_per, test_per, ignore):
    print '忽略栏\t\t\t', ignore
    cols_name, chi = get_cols_name(ignore)
    print_cols(chi)
    """
    pretreatment.treat(before_train, after_train, train_per, before_test,
    after_test, test_per, ignore):
    :param before_train: 原始训练集
    :param after_train: 处理后的训练集
    :param train_per: 处理后训练集中原始训练集占的比例
    :param before_test: 原始测试集
    :param after_test: 处理后测试集
    :param test_per: 处理后训练集中测试集的比例
    :param ignore: 忽略掉的特征
    """
    pretreatment.treat(before_train=before_train, after_train=after_train,
                       train_per=train_per, before_test=before_test,
                       after_test=after_test, test_per=test_per, ignore=ignore)
    c = NBC(train_data=after_train, cols_names=cols_name)
    c.test(test_data=after_test, cols_names=cols_name)
    print '\n'


if __name__ == '__main__':
    print "90% 训练集 + 10% 测试集,这里可以验证各个特征对其影响"
    train_per = 0.9
    test_per = 0.1

    ignore = [2, 4]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 3, 7, 8, 9, 10, 11, 12, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 8, 9, 10, 11, 12, 13]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 13, 9, 8, 12]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 13, 9, 8]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4, 7, 13, 9]
    begin(train_per=train_per, test_per=test_per, ignore=ignore)


    print '训练集中加入测试集数据'

    train_per = 1.0
    test_per = 0.05
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    train_per = 1.0
    test_per = 0.5
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    train_per = 1.0
    test_per = 1.0
    begin(train_per=train_per, test_per=test_per, ignore=ignore)

    ignore = [2, 4]
    train_per = 0.5
    test_per = 1.0
    begin(train_per=train_per, test_per=test_per, ignore=ignore)
