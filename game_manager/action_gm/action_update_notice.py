# -*- coding:utf-8 -*-
"""
    编辑广播
"""
from game_manager.action_gm import action_base_gm
from util import game_define


def log(manager, notice):
    """
        输出日志
    """
    action = game_define.GM_ACTION_UPDATE_NOTICE
    log_lst = action_base_gm.log_base(manager)

    log_lst.append(str(action))
    log_lst.append(str(notice))

    log_str = '$$'.join(log_lst)
    return log_str


def parse(log_part_lst):
    """
        解析
    """
    result = dict()
    result['action'] = int(log_part_lst[0])
    result['notice'] = log_part_lst[1]

    return result