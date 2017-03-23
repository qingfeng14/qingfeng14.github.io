# coding=utf-8

# 特征值名称
origin_names = ["age", "work_class", "fnlwgt", "education", "education_num",
                "marital-status", "occupation", "relationship", "race", "sex",
                "capital_gain", "capital_loss", "hours_per_week",
                "native-country", "income"]

chinese_names = ["年龄", "工作类别", '重量', '学历等级', '教育年限', '婚姻状况',
                 '职业', '家庭关系', '人种', '性别', '投资利得', '投资损失',
                 '每周工作时间', '出生国', '收入']

# 测试集及训练集数据来源
before_train = 'adult.train'
before_test = 'adult.test'
after_train = 'after.train'
after_test = 'after.test'

# 是否开启debug模式
debug = False

# 训练集是否随机抓取
if_random = False

# 拉普拉斯平滑
Lambda = 1.0

# 年龄的离散颗粒度
age_step = 5
# 工作时间的离散颗粒度
hour_step = 5

# 投资收益分割
capital_if_step = False
capital_step = 10000
# 投资收益中位数
gain_middle = 7298
# 损失中位数
loss_middle = 1887

# 是否忽略?
ignore_miss = True
