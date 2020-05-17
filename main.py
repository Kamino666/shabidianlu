from math import sqrt
def 并联(*args):
    分母 = 0
    for i in range(len(args)):
        分母 += 1 / args[i]
    return 1 / 分母


def 计算rbe(rbb, beta, Ic):
    return rbb + beta*(0.0258/Ic)


def 单管共发射极():
    i_data = input("请输入Rb Rc Ube β Ucc rbb(空格分隔，k用e3代替)").split(' ')
    Rb, Rc, Ube, beta, Ucc, rbb = i_data
    # 静态
    Ib = eval('(' + Ucc + '-' + Ube + ')' + '/' + Rb)
    Ic = eval(beta) * Ib
    Uce = eval(Ucc) - Ic*eval(Rc)
    print("Ib = {}; Uce = {}".format(Ib, Uce))
    print("Ie = {}; Ic = {}".format(Ib*(1+eval(beta)),Ib*(eval(beta))))
    # 动态
    rbe = 计算rbe(eval(rbb), eval(beta), Ic)
    Au = -eval(beta) * eval(Rc) / rbe
    ri = 并联(eval(Rb), eval(rbe))
    ro = eval(Rc)
    print("Au = {}".format(Au))
    print("ri = {}; ro = {}".format(ri, ro))


def 静态工作点稳定电路():
    i_data = input("请输入Rb1 Rb2 Rc Re Ube β Ucc rbb Rl(空格分隔，k用e3代替)").split(' ')
    Rb1, Rb2, Rc, Re, Ube, beta, Ucc, rbb, Rl = i_data
    # 静态
    Rb = 1 / ( 1/(eval(Rb1)) + 1/(eval(Rb2)))
    Ubb = eval(Rb2)/(eval(Rb1)+eval(Rb2)) * eval(Ucc)
    Ib = (Ubb - eval(Ube))/((1+eval(beta))*eval(Re)+Rb)
    Uce = eval(Ucc) - eval(beta) * Ib * eval(Rc) - (1+eval(beta))*Ib*eval(Re)
    Ie = Ib*(1+eval(beta))
    Ic = Ib*(eval(beta))
    print("Ib = {}; Uce = {}".format(Ib, Uce))
    print("Ie = {}; Ic = {}".format(Ie, Ic))
    # 动态
    rbe = 计算rbe(eval(rbb), eval(beta), Ic)
    Au1 = -eval(beta) * 并联(eval(Rc), eval(Rl)) / rbe
    Au2 = -eval(beta) * 并联(eval(Rc), eval(Rl)) / (rbe + (1+eval(beta)*eval(Re)) )
    ri1 = 并联(eval(Rb1), eval(Rb2), rbe)
    ri2 = 并联(eval(Rb1), eval(Rb2), (1+eval(beta)*eval(Re)))
    ro = eval(Rc)
    print("带旁路电容Au = {}; 不带旁路电容Au = {}".format(Au1, Au2))
    print("带旁路电容ri = {}; 不带旁路电容ri = {}".format(ri1, ri2))
    print("ro = {}".format(ro))
    print("rbe = {}".format(rbe))


def 射极输出电路():
    i_data = input("请输入Rb Re Ube β Ucc rbb Rl Rs(空格分隔，k用e3代替)").split(' ')
    Rb, Re, Ube, beta, Ucc, rbb, Rl, Rs = i_data
    # 静态
    Ib = (eval(Ucc) - eval(Ube))/(eval(Rb) + eval(beta) * eval(Re))
    Ie = Ib * (1 + eval(beta))
    Ic = Ib * (eval(beta))
    Uce = eval(Ucc) - Ie * eval(Re)
    print("Ib = {}; Uce = {}".format(Ib, Uce))
    print("Ie = {}; Ic = {}".format(Ie, Ic))
    # 动态
    rbe = 计算rbe(eval(rbb), eval(beta), Ic)
    分子 = ( (1+eval(beta)) * 并联(eval(Re), eval(Rl)) )
    Au = 分子/(rbe + 分子)
    ri = 并联(eval(Rb), (rbe + 分子))
    ro = 并联(eval(Re), ( 并联(eval(Rs),eval(Rb)) + rbe )/(1+eval(beta)) )
    print("Au = {}".format(Au))
    print("ri = {}; ro = {}".format(ri, ro))
    print("rbe = {}".format(rbe))


def 并联工具():
    data = input("输入要并联的电阻(空格分隔，k用e3代替)").split(' ')
    data_tuple = tuple([eval(i) for i in data])
    print(data_tuple)
    print("并联结果为: {}".format(并联(*data_tuple)))


def 场效应管分压式共源级放大电路():
    i_data = input("请输入Rg1 Rg2 Rg Rd Udd Rs Ido Ugs(th) Rl(空格分隔，k用e3代替)").split(' ')
    Rg1, Rg2, Rg, Rd, Udd, Rs, Ido, Ugs_th, Rl = i_data
    # 静态
    a = (eval(Rs)*eval(Ido)) / eval(Ugs_th)**2
    b = 1 - (2*eval(Rs)*eval(Ido))/(eval(Ugs_th))
    c = eval(Ido)*eval(Rs) - eval(Udd) * (eval(Rg2))/(eval(Rg1)+eval(Rg2))
    print("a{} b{} c{}".format(a,b,c))
    delta = sqrt(b**2-4*a*c)
    print("delta{}".format(delta))
    Ugs1 = (-b + delta) / (2 * a)
    Id1 = eval(Ido) * (Ugs1 / eval(Ugs_th) - 1) ** 2
    Ugs2 = (-b - delta) / (2 * a)
    Id2 = eval(Ido) * (Ugs2 / eval(Ugs_th) - 1) ** 2
    if Ugs1 > eval(Ugs_th):
        print("选择解1")
        Ugs = Ugs1
        Id = Id1
    else:
        print("选择解2")
        Ugs = Ugs2
        Id = Id2
    Uds = eval(Udd) - Id*eval(Rd) - Id*eval(Rs)
    print("Ugs = {}; Id = {}".format(Ugs, Id))
    print("Uds = {}".format(Uds))
    # 动态
    gm = 2*sqrt(Id*eval(Ido))/eval(Ugs_th)
    Au = -gm * 并联(eval(Rd), eval(Rl))
    ri = eval(Rg) + 并联(eval(Rg1), eval(Rg2))
    ro = eval(Rd)
    print("gm = {}; Au ={}".format(gm, Au))
    print("ri = {}; ro = {}".format(ri, ro))


def 场效应管分压式共漏级放大电路():
    i_data = input("请输入Rg1 Rg2 Rg Rd Udd Rs Ido Ugs(th) Rl(空格分隔，k用e3代替)").split(' ')
    Rg1, Rg2, Rg, Rd, Udd, Rs, Ido, Ugs_th, Rl = i_data
    # 静态
    a = (eval(Rs)*eval(Ido)) / eval(Ugs_th)**2
    b = 1 - (2*eval(Rs)*eval(Ido))/(eval(Ugs_th))
    c = eval(Ido)*eval(Rs) - eval(Udd) * (eval(Rg2))/(eval(Rg1)+eval(Rg2))
    print("a{} b{} c{}".format(a,b,c))
    delta = sqrt(b**2-4*a*c)
    print("delta{}".format(delta))
    Ugs1 = (-b + delta) / (2 * a)
    Id1 = eval(Ido) * (Ugs1 / eval(Ugs_th) - 1) ** 2
    Ugs2 = (-b - delta) / (2 * a)
    Id2 = eval(Ido) * (Ugs2 / eval(Ugs_th) - 1) ** 2
    if Ugs1 > eval(Ugs_th):
        print("选择解1")
        Ugs = Ugs1
        Id = Id1
    else:
        print("选择解2")
        Ugs = Ugs2
        Id = Id2
    Uds = eval(Udd) - Id*eval(Rd) - Id*eval(Rs)
    print("Ugs = {}; Id = {}".format(Ugs, Id))
    print("Uds = {}".format(Uds))
    # 动态
    gm = 2*sqrt(Id*eval(Ido))/eval(Ugs_th)
    分子 = gm * 并联(eval(Rs), eval(Rl))
    Au = 分子/(1+分子)
    ri = eval(Rg) + 并联(eval(Rg1), eval(Rg2))
    ro = (eval(Rs))/(1+gm*eval(Rs))
    print("gm = {}; Au ={}".format(gm, Au))
    print("ri = {}; ro = {}".format(ri, ro))


def 场效应管自给式共源级放大电路():
    i_data = input("请输入Rg1 Rg2 Rg Rd Udd Rs Ido Ugs(th) Rl(空格分隔，k用e3代替)").split(' ')
    Rg1, Rg2, Rg, Rd, Udd, Rs, Ido, Ugs_th, Rl = i_data
    # 静态
    a = (eval(Rs)*eval(Ido)) / eval(Ugs_th)**2
    b = 1 - (2*eval(Rs)*eval(Ido))/(eval(Ugs_th))
    c = eval(Ido)*eval(Rs)
    print("a{} b{} c{}".format(a,b,c))
    delta = sqrt(b**2-4*a*c)
    print("delta{}".format(delta))
    Ugs1 = (-b + delta) / (2 * a)
    Id1 = eval(Ido) * (Ugs1 / eval(Ugs_th) - 1) ** 2
    Ugs2 = (-b - delta) / (2 * a)
    Id2 = eval(Ido) * (Ugs2 / eval(Ugs_th) - 1) ** 2
    if Ugs1 > eval(Ugs_th):
        print("选择解1")
        Ugs = Ugs1
        Id = Id1
    else:
        print("选择解2")
        Ugs = Ugs2
        Id = Id2
    Uds = eval(Udd) - Id*eval(Rd) - Id*eval(Rs)
    print("Ugs = {}; Id = {}".format(Ugs, Id))
    print("Uds = {}".format(Uds))
    # 动态
    gm = 2*sqrt(Id*eval(Ido))/eval(Ugs_th)
    Au = -gm * 并联(eval(Rd), eval(Rl))
    ri = eval(Rg) + 并联(eval(Rg1), eval(Rg2))
    ro = eval(Rd)
    print("gm = {}; Au ={}".format(gm, Au))
    print("ri = {}; ro = {}".format(ri, ro))


def 场效应管自给式共漏级放大电路():
    i_data = input("请输入Rg1 Rg2 Rg Rd Udd Rs Ido Ugs(th) Rl(空格分隔，k用e3代替)").split(' ')
    Rg1, Rg2, Rg, Rd, Udd, Rs, Ido, Ugs_th, Rl = i_data
    # 静态
    a = (eval(Rs)*eval(Ido)) / eval(Ugs_th)**2
    b = 1 - (2*eval(Rs)*eval(Ido))/(eval(Ugs_th))
    c = eval(Ido)*eval(Rs)
    print("a{} b{} c{}".format(a,b,c))
    delta = sqrt(b**2-4*a*c)
    print("delta{}".format(delta))
    Ugs1 = (-b + delta) / (2 * a)
    Id1 = eval(Ido) * (Ugs1 / eval(Ugs_th) - 1) ** 2
    Ugs2 = (-b - delta) / (2 * a)
    Id2 = eval(Ido) * (Ugs2 / eval(Ugs_th) - 1) ** 2
    if Ugs1 > eval(Ugs_th):
        print("选择解1")
        Ugs = Ugs1
        Id = Id1
    else:
        print("选择解2")
        Ugs = Ugs2
        Id = Id2
    Uds = eval(Udd) - Id*eval(Rd) - Id*eval(Rs)
    print("Ugs = {}; Id = {}".format(Ugs, Id))
    print("Uds = {}".format(Uds))
    # 动态
    gm = 2*sqrt(Id*eval(Ido))/eval(Ugs_th)
    分子 = gm * 并联(eval(Rs), eval(Rl))
    Au = 分子/(1+分子)
    ri = eval(Rg) + 并联(eval(Rg1), eval(Rg2))
    ro = (eval(Rs))/(1+gm*eval(Rs))
    print("gm = {}; Au ={}".format(gm, Au))
    print("ri = {}; ro = {}".format(ri, ro))

if __name__ == '__main__':
    print("******************************")  # 30
    print("{0:^30}".format("1-单管共发射极电路"))
    print("{0:^30}".format("2-静态工作点稳定电路"))
    print("{0:^30}".format("3-射极输出电路"))
    print("{0:^30}".format("4-并联工具"))
    print("{0:^30}".format("5-场效应管分压式共源级放大电路"))
    print("{0:^30}".format("6-场效应管分压式共漏级放大电路"))
    print("{0:^30}".format("7-场效应管自给式共源级放大电路"))
    print("{0:^30}".format("8-场效应管自给式共漏级放大电路"))
    print("******************************")  # 30
    print("便捷计算 童叟无欺")
    a = input("输入要计算的电路")
    if a == '1':
        单管共发射极()
    elif a == '2':
        静态工作点稳定电路()
    elif a == '3':
        射极输出电路()
    elif a == '4':
        并联工具()
    elif a == '5':
        场效应管分压式共源级放大电路()
    elif a == '6':
        场效应管分压式共漏级放大电路()
    elif a == '7':
        场效应管自给式共源级放大电路()
    elif a == '8':
        场效应管自给式共漏级放大电路()
