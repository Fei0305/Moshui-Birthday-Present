#! /usr/bin/env python

import datetime


def together_days(year, month, day) -> int:
    """ 计算在一起天数
    :param year, month, day: 日期
    :return together_days: 在一起天数整形
    """

    together_start_date = datetime.date(year, month, day)  # 在一起日期
    today_date = datetime.date.today()  # 今天日期
    together_days = (today_date - together_start_date).days  # 在一起天数
    return together_days


def which_week(year: int, month: int, day: int) -> int:
    """ 返回周数
    :param year, month, day: 开学日期
    :return weeks: 周数整形
    """
    today_date = datetime.date.today()  # 今天日期
    school_start_date = datetime.date(year, month, day)
    weeks = int((today_date - school_start_date).days / 7) + 1  # 计算第几周
    return weeks


def get_today_table():
    """ 获取当日课表
    :return: 课程表列表
    """
    # 单周课表
    single_table_dict = {
        '0': ('数电................(综合楼207)', '-', '马原................(电气楼201)', '-'),
        '1': ('信号系统........(综合楼208)', '大英................(综合楼307)', '-', '健美操.......................(操场)'),
        '2': ('数电................(综合楼207)', '-', '毛概................(电气楼201)', '-'),
        '3': ('-', '信号系统........(综合楼208)', '-', '-'),
        '4': ('EDA技术........(综合楼201)', '数据结构........(综合楼201)', '毛概................(电气楼201)', '-')
    }

    # 双周课表
    double_table_dict = {
        '0': ('数电................(综合楼207)', '-', '马原................(电气楼201)', '-'),
        '1': ('信号系统........(综合楼208)', '大英................(综合楼307)', '-', '健美操.......................(操场)'),
        '2': ('数电................(综合楼207)', '-', '毛概................(电气楼201)', '-'),
        '3': ('大英................(综合楼307)', '信息系统........(综合楼208)', '-', '马原................(电气楼401)'),
        '4': ('EDA技术........(综合楼201)', '数据结构........(综合楼201)', '-', '-')
    }

    if which_week(2022, 3, 5) % 2 == 1:
        table_dict = single_table_dict
    else:
        table_dict = double_table_dict

    # now_date = datetime.datetime.now()
    now_date = datetime.datetime(2022, 3, 11, 19)
    today_table = ''
    if now_date.weekday() + 1 >= 6:
        today_table = '下周一课表:\n一: 数电................(综合楼207)\n二: -\n三: 马原................(电气楼201)\n四: -'

    else:
        if now_date.hour < 18:
            today_table = '今日课表:\n一: {}\n二: {}\n三: {}\n四: {}'\
                .format(
                    table_dict[str(now_date.weekday())][0],
                    table_dict[str(now_date.weekday())][1],
                    table_dict[str(now_date.weekday())][2],
                    table_dict[str(now_date.weekday())][3])
        else:
            if now_date.weekday() + 1 == 5:
               today_table = '下周一课表:\n一: 数电................(综合楼207)\n二: -\n三: 马原................(电气楼201)\n四: -'
            else:
                today_table = '明日课表:\n一: {}\n二: {}\n三: {}\n四: {}'\
                    .format(
                        table_dict[str((now_date.weekday() + 1) % 5)][0],
                        table_dict[str((now_date.weekday() + 1) % 5)][1],
                        table_dict[str((now_date.weekday() + 1) % 5)][2],
                        table_dict[str((now_date.weekday() + 1) % 5)][3])

    return today_table.split('\n')
