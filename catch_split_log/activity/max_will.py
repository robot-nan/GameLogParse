#coding:utf-8
import datetime
import sys
from util.save_out_put_fun import Los_Class
from util import dat_log_util
from util.logs_out_in_path import OUT_PUT_PATH_LST
from util.logs_out_path_of_parse import get_parse_path
first, second, third, fourth= 0,0,0,0


def start(search_date):
    """
    满额返利
    """
    O, OUT_PUT_PATH_LST = get_parse_path(search_date)
    for server_id in OUT_PUT_PATH_LST.keys():
        try:
            row_list = make_action_file(search_date,server_id)
            los = Los_Class(search_date,'tables','MAX_WILL')
            los.save_one_server(row_list,server_id)
        except:
            pass


def make_action_file(search_date,server_id):
    global first, second, third, fourth,fifth,sixth,seventh    # 取事件的文件
    table_lst = []
    seven_lv_data = dat_log_util.read_one_day_data('',search_date,'all_action',server_id)
    for _server_list in seven_lv_data:
        for _action_dict in _server_list:
            log_time = _action_dict['log_time'].strftime('%Y-%m-%d')
            if _action_dict['recharge_sum_id']   == 1  :   first += 1
            elif _action_dict['recharge_sum_id'] == 2  :   second += 1
            elif _action_dict['recharge_sum_id'] == 3  :   third += 1
            elif _action_dict['recharge_sum_id'] == 4  :   fourth += 1

            row = [log_time,first, second, third, fourth]
        table_lst.append(row)
    return table_lst


if __name__ =='__main__':
    start(sys.argv)
