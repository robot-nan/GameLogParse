# -*- coding:utf-8 -*-
"""
    宠物金币洗练个体值
"""

from action import action_base
from util import game_define


def log(user, cost_gold, mon_tid):
    """
        输出日志
    """
    action = game_define.EVENT_ACTION_RESET_INDIVIDUAL_MONSTER
    cur_gold = user.player.get_gold()
    total_cost_gold = user.player.total_cost_gold

    log_lst = action_base.log_base(user)

    log_lst.append(str(action))
    log_lst.append(str(cost_gold))
    log_lst.append(str(cur_gold))
    log_lst.append(str(total_cost_gold))
    log_lst.append(str(mon_tid))

    log_str = '$$'.join(log_lst)
    return log_str

def parse(log_part_lst):
    """
        解析
    """
    result = dict()
    result['action'] = int(log_part_lst[0])
    result['cost_gold'] = int(log_part_lst[1])
    result['cur_gold'] = int(log_part_lst[2])
    result['total_cost_gold'] = int(log_part_lst[3])
    result['monster_tid'] = int(log_part_lst[4])
    result['old_gold'] = result['cur_gold'] + result['cost_gold']
    return result