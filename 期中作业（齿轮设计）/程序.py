import math


#1.计算弯曲许用应力
                        #参数设置

Y_st = 2.0     #应力修正系数（国标）
Y_X = 1     #尺寸系数（若m > 5mm 则查图5-31）                          ##
Y_N = 1     #寿命系数（由N=nat，查表可变）                             ##


S_Flim1 = 2.5     #小齿轮弯曲强度安全系数（一般1.3-1.5；重要1.6-3.0）  ##
xgm_Flim1 = 290    #小齿轮接触疲劳极限（图5-29）                       ##
xgm_FP1 = xgm_Flim1 * Y_st / S_Flim1 * Y_X * Y_N
print('xgm_FP1 = {:.2f}'.format(xgm_FP1))

S_Flim2 = 2.0     #大齿轮弯曲强度安全系数（一般1.3-1.5；重要1.6-3.0）  ##
xgm_Flim2 = 290    #大齿轮接触疲劳极限（图5-29）                       ##
xgm_FP2 = xgm_Flim1 * Y_st / S_Flim2 * Y_X * Y_N
print('xgm_FP2 = {:.2f}'.format(xgm_FP2))

#2.计算接触许用应力
                        #参数设置


Z_W = 1     #硬化系数（均为硬齿面故为1）                               ##
Z_N = 1     #寿命系数（由N=nat，查表可变）                             ##


S_Hlim1 = 1.3     #小齿轮弯曲强度安全系数（一般1.0-1.2；重要1.3-1.6）   ##
xgm_Hlim1 = 700   #小齿轮弯曲疲劳极限（图5-29）                       ##
xgm_HP1 = xgm_Hlim1 / S_Hlim1 * Z_W * Z_N
print('xgm_HP1 = {:.2f}'.format(xgm_HP1))


S_Hlim2 = 1.3     #大齿轮弯曲强度安全系数（一般1.0-1.2；重要1.3-1.6）   ##
xgm_Hlim2 = 700    #大齿轮弯曲疲劳极限（图5-29）                       ##
xgm_HP2 = xgm_Hlim2 / S_Hlim2 * Z_W * Z_N
print('xgm_HP2 = {:.2f}'.format(xgm_HP2))



#3.设置参数
              #基本参数
K = 1.3     #查表（一般取1.3-1.7 PPT第110页）      ##
n = 1500    #电机转速                ##
v = 1.5     #运输带工作速度          ##
F = 3000    #运输带工作压力          ##
P = F * v   #输入功率W
T = 9.550 * P / n    #转矩（Nm）
print('T = {:.2f}'.format(T))


              #齿轮参数

z1 = 29     #小齿轮齿数          ##
z2 = 130    #大齿轮齿数          ##
posai = 0.5    #齿宽系数         ##
beita = 15     #螺旋角           ##
b = math.cos(beita*math.pi/180)   #cos(beita)
u = z2 / z1    #
z_v1 = z1 / b**3    #
z_v2 = z2 / b**3    #
print('z_v1 = {:.2f}'.format(z_v1))
print('z_v2 = {:.2f}'.format(z_v2))

Y_FS1 = float(input('请根据复合齿形系数z_v1在P88图5-26中找出其对应的Y_FS1并输入：'))
Y_FS2 = float(input('请根据复合齿形系数z_v2在P88图5-26中找出其对应的Y_FS2并输入：'))

ypxl = (1.88 - 3.2 * (1 / z_v1 + 1 / z_v2)) * b
print('ypxl = {:.2f}'.format(ypxl))
Y_eb = float(input('请根据重合度ypxl(这个是希腊字母伊普西龙,图5-41横坐标)在P103图5-41中找出对应的螺旋角系数Y_eb并输入：'))

#4.求解模数
m_n = (2000*K*T*b**2/posai/z1**2/xgm_FP1*Y_eb*Y_FS1)

print('模数m_n = {:.3f}'.format(m_n))
m = float(input('请根据m_n在P70表5-1中找出标准模数（选一个比计算模数大一点的就是标准模数）并输入：'))


#5.更改参数
a = m * (z1 + z2) / 2 / b      
print('a = {:.2f}'.format(a))
real_a = float(input('中心距a的取值为：'))
real_beita = math.acos(m*(z1+z2)/2/real_a)/math.pi*180
print('螺旋角beita = {:.3f}'.format(real_beita))
print('螺旋角beita的cos值 = {:.3f}'.format(m*(z1+z2)/2/real_a))
d1 = m * z1 / math.cos(real_beita*math.pi/180)
d2 = m * z2 / math.cos(real_beita*math.pi/180)
print('d1 = {:.3f}'.format(d1))
print('d2 = {:.3f}'.format(d2))
b2 = posai * d1
print('b2 = {:.3f}'.format(b2))
b2 = float(input('取b2 = '))
print('b1的取值范围为{:.3f}-{:.3f}'.format(b2+5,b2+10))
b1 = float(input('取b1 = '))

#6.校核齿面接触强度
Z_ypxl = 0.85    #重合度系数（斜齿轮取0.75-0.88）    ##
Z_E = 189.8     #材料弹性系数（查表5-4）             ##
#Z_beita = math.sqrt(real_beita*math.pi/180)
xgm_H = 109*Z_E*Z_ypxl*(K*T*(u+1)/u/b2/d1**2)**(1/2)
print('xgm_H = {:.3f}'.format(xgm_H))
print('xgm_HP1 = {:.3f}'.format(xgm_HP1))
