def baojing(strgl):
    if strgl.__eq__('6'):
        return "正常运行"
    elif strgl.__eq__('5'):
        return "停止运行"
    elif strgl.__eq__('4'):
        return "卡料报警"
    elif strgl.__eq__('3'):
        return "超量程报警"
    elif strgl.__eq__('2'):
        return "电压超限报警"
    else:
        return "空料报警"