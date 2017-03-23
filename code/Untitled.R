# 读取测试集，已清除？
test = read.csv("adult.test", 
                  sep=",", header=F, col.names=c("age", "work_class", "fnlwgt", "education", "education_num", 
                                                  "marital-status", "occupation", "relationship", "race", "sex",
                                                  "capital_gain", "capital_loss", "hourr_per_week","native-country", "income"),
                  fill = FALSE, strip.white = T)

# 读取训练集，已清除？
train = read.csv("adult.train", 
                  sep=",", header=F, col.names=c("age", "work_class", "fnlwgt", "education", "education_num", 
                                                 "marital-status", "occupation", "relationship", "race", "sex",
                                                 "capital_gain", "capital_loss", "hourr_per_week","native-country", "income"),
                  fill = FALSE, strip.white = T)

# 读取测试集，已清除？
test = read.csv("after.test", 
                sep=",", header=F, col.names=c("age", "work_class", "education",
                                               "marital-status", "occupation", "relationship", "race", "sex",
                                               "capital_gain", "capital_loss", "hourr_per_week","native-country", "income"),
                fill = FALSE, strip.white = T)

# 读取训练集，已清除？
train = read.csv("after.train", 
                 sep=",", header=F, col.names=c("age", "work_class", "education", 
                                                "marital-status", "occupation", "relationship", "race", "sex",
                                                "capital_gain", "capital_loss", "hourr_per_week","native-country", "income"),
                 fill = FALSE, strip.white = T)

# 工作类型
table(train$work_class)
table(test$work_class)

# 年龄
table(train$age)
table(test$age)

# 资本收益
table(train$capital_gain)
table(test$capital_gain)



# 资本损失
table(train$capital_loss)
table(test$capital_loss)


table(train$capital_gain)
table(train$capital_gain[train$capital_gain!=0])
# 资本收益平均值
mean(train$capital_gain[train$capital_gain!=0])
# 资本收益中位数
median(train$capital_gain[train$capital_gain!=0])
# 资本收益方差
sd(train$capital_gain[train$capital_gain!=0])


table(train$capital_loss)
table(train$capital_loss[train$capital_loss!=0])
# 资本损失平均值
mean(train$capital_loss[train$capital_loss!=0])
# 资本损失中位数
median(train$capital_loss[train$capital_loss!=0])
# 资本损失收益方差
sd(train$capital_loss[train$capital_loss!=0])


# 对于测试集
table(test$capital_gain)
table(test$capital_gain[test$capital_gain!=0])
# 资本收益平均值
mean(test$capital_gain[test$capital_gain!=0])
# 资本收益中位数
median(test$capital_gain[test$capital_gain!=0])
# 资本收益方差
sd(test$capital_gain[test$capital_gain!=0])


table(test$capital_loss)
table(test$capital_loss[test$capital_loss!=0])
# 资本损失平均值
mean(test$capital_loss[test$capital_loss!=0])
# 资本损失中位数
median(test$capital_loss[test$capital_loss!=0])
# 资本损失收益方差
sd(test$capital_loss[test$capital_loss!=0])

# 每周工作时间
table(train$hourr_per_week)
table(test$hourr_per_week)

# 教育
table(train$education)
table(test$education)

# 婚姻状况
table(train$marital.status)
table(test$marital.status)

