'''3、摆放家具
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
'''
#家具类，
#家具面积
class jiaju():
    def __init__(self,name,mj):
        self.name = name
        self.mj = mj
#房子类
#总面积和剩余面积   家具列表
class house():
    def __init__(self,weizhi,mianji):
        self.weizhi = weizhi
        self.mianji = mianji
        self.symj = mianji
        self.list = []
    def __str__(self):
        return f'房子位于{self.weizhi}，面积是{self.mianji},剩余面积是{self.symj},房子有{self.list}'

    def ban(self,jj):
        if self.symj > jj.mj:
            self.list.append(jj.name)
            self.symj -= jj.mj
        else:
            print('空间不够了')
bad = jiaju('床',4)
bad1 = house('四合院',100)
print(bad1)
bad1.ban(bad)
print(bad1)




