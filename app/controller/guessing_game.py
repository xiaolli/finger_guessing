#猜拳游戏
def guess(g, times):  # 参数g：代表传入的锤/剪刀/布，times：代表可以猜拳的次数
    import random
    l = ["J", "K", "P"]  # 列表存放的锤/剪刀/布，用于系统自动生成的结果
    # times = 1
    get_award_off = []  # 用于胜出时所中的奖励，存放现金减免额（数值类型）
    get_award_gift = []  # 用于胜出时所中的奖励，存放现金意外的礼品（非数值类型）
    award_off = [-1, -2, -5, -10, -20]  # 存放现金减免额:数值
    award_gift = ["$30", "$50", "FASHION_TOY", "ROBOT", "one time again"] # 存放礼品:非数值
    award_l =  award_off + award_gift  # 存放所有礼品
    message_guess = ''  # 用于猜拳游戏中提示胜负及中奖信息
    # print(random.randint(1,3))
    # print(random.choice(l))
    while times > 0:  # 拥有猜拳游戏参与资格的判定
        auto_s = random.choice(l)  # 系统随机生成的结果，用于和输入的值做比较
        print(auto_s)
        # g =  input("Let's PK:")
        if str.upper(g) not in l:  # 输入异常值时，用于input输入时
            message_guess = "oops!input is wrong! Try again"
            # times -= 1
        elif str.upper(g) == auto_s:  # 平局算负
            message_guess = "peace!you lost!"
            times -= 1
        elif (str.upper(g) == 'P' and auto_s == 'J') or (str.upper(g) == 'J' and auto_s == 'K') or (
                str.upper(g) == 'K' and auto_s == 'P'):
            # message_guess = "You win!"
            times -= 1
            award_p = random.choice(award_l)  # 胜出是系统随机抽取奖励
            if award_p in award_off:  # 现金off奖励时
                message_guess = "You win!!Congratulations!You earned one %s cash award " % award_p
                get_award_off.append(award_p)  # 因次数不同，用于多次中此类奖

                # return get_award_off
            elif award_p in award_gift:  # 现金意外奖励时
                message_guess = "You win!!Congratulation!You earned one %s gift " % award_p
                get_award_gift.append(award_p)  # 因次数不同，用于多次中此类奖

                # return get_award_gift
            else:  # 抽取再来一次奖励
                message_guess = "You win!!Congratulation!You earned PK chance %s" % award_p
                times += 1
        else:  # 意外场合算负
            message_guess = "You lost!!!!"
    return message_guess, get_award_off, get_award_gift, auto_s  # 函数返回值