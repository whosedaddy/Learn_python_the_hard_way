# -*- coding:utf-8 -*-
#有十种人
x="There are %d types of people."%10
#二进制
binary="binary"
#不
do_not="don't"
#分为知道二进制的和不知道的
y="Those who know %s and those who %s."%(binary, do_not)

#输出x
print x
#输出y
print y

#我说：共有十种人
print "I said:%r."%x
#我也说：分为知道二进制的和不知道的
print "I also said:'%s'."%y

#滑稽的=错误
hilarious=False
#这个好笑吗？
joke_evaluation="Isn't that joke so funny?!%r"

#输出“joke_evaluation
print joke_evaluation%hilarious

#这是左边
w="This is the left side of..."
#这字符串的右边
e="a string with a right side."

#输出w+e
print w+e