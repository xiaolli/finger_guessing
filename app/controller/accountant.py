
# 用于会计计算的类
class Accountant():
    # 无类成员变量
    def set_guess_times(self, first_limit, weight, total):  # 类方法：用于设定游戏次数；
        # 参数first_limit：首次达到可抽奖的额度
        # weight：递减值（加权）
        # total：订单消费总额

        surplus = total
        limit_l = []
        i = 0
        guess_times = 0
        if total < first_limit:  # 如果总订单额小于第一次可抽奖限制额度，pass
            pass
        else:  # 制定限定额规则
            limit_l.append(first_limit)
            while surplus >= weight:  # 生成临时的抽奖额度列表，将len()用于计算可猜拳的次数
                if i == 1:  # 第一次时pass
                    pass
                elif i == 2:  # 第二次达到限额设置：第一次的2倍-递减值
                    limit_l.append(first_limit * 2 - weight)
                    surplus = total - limit_l[1]
                elif i > 2:  # 第三次以后达到的限额设置：第n-1次的额+第一次额 - 递减值
                    a = limit_l[i - 2] + limit_l[0] - (i - 1) * weight
                    if a <= limit_l[i - 2]:  # 当第n次 小于等于 第n-1次时，规则变化：递减值变递增值
                        limit_l.append(limit_l[i - 2] + weight)
                    else:
                        limit_l.append(a)
                    surplus = total - limit_l[i - 1]
                i += 1
        guess_times = len(limit_l)  # 计算出可参与猜拳游戏的次数（消费越多则参与次数越多）

        return guess_times  # 返回可参与次数

    def get_bill(self, total, award_off, award_gift):  # 类方法：用于计算最后所需支付额及所获得的奖励
        award_gift_info_keys = []
        award_gift_info_values = []
        award_gift_info = None
        bill = 0
        #
        if len(award_off) > 0:  # 如果获得的现金off奖励不为空则计算总off额：sum(award_off)
            bill = total + sum(award_off)  # 计算off后的需支付额
        else:
            bill = total
        #
        if len(award_gift) > 0:
            # award_gift_info = "You have got gift as follow:"
            award_gift_t = list(set(award_gift))  # 列表转集合转字典（去重），用于列表中各项的份额
            for i in range(0, award_gift_t):
                award_gift_info_keys.append(award_gift_t[i])  # 去重后列表作为dict的keys
                award_gift_info_values.append(award_gift.count(award_gift_t[i]))  # 各项的份额统计值作为Values
                award_gift_info = dict(zip(award_gift_info_keys, award_gift_info_values))  # 列表转字典
        else:
            pass
        return bill, award_gift_info  # 返回需支付额及获得礼品的词典