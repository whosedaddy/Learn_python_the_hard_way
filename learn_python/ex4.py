# -*- coding:utf-8 -*- 
#总车辆数
cars=100
#车辆空位数
space_in_a_car=4.0
#运行车辆数
drivers=30
#乘客总数
passengers=90
#变量名出错较多，下次一定要注意
#没开的车=总车辆数-运行车辆数
cars_not_driven=cars-drivers
#同上，标记
#车辆运行数=运行车辆数
cars_driven=drivers
#车辆运送能力=车辆运行数*车辆空位数
carpool_capacity=cars_driven*space_in_a_car
#平均车载乘客数=乘客总数/车辆运行数
average_passengers_per_car=passengers/cars_driven

print "There are",cars,"cars available."
print "There are only",drivers,"drivers available."
#同上，标记
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."
