from datetime import datetime, timedelta
from collections import defaultdict


def check_b_day(b_day):
    current_day = datetime.now().date()
    next_monday = current_day + timedelta(7) - timedelta(current_day.weekday())
    start_period = next_monday - timedelta(2)
    end_period = next_monday + timedelta(5)
    if start_period <= b_day.date() <= end_period:
        return True
    return False


def group_list(b_list):
    b_dict = {}
    grouped_b_list = defaultdict(list)
    for i in b_list:
        group_f = i[:10]
        grouped_b_list[group_f].append(i[11:])

    for i in grouped_b_list:
        if datetime.strptime(i, '%Y-%m-%d').weekday() > 4:
            b_dict.setdefault('Monday', []).append(grouped_b_list[i])
        else:
            b_dict.setdefault(datetime.strptime(i, '%Y-%m-%d').strftime('%A'), []).append(grouped_b_list[i])
    return b_dict


def print_result(b_dict):
    result = ''
    for i in b_dict:
        result += i + ': '
        for m in b_dict[i]:
            result += m[0]
            
            if m[0] != b_dict[i][-1][0]:
                result += ', '
        result += '\n'
    print(result)


def congratulate(users):
    b_list = []
    for i in (i for i in users):
        b_day = datetime.strptime(i['birthday'], '%d.%m.%Y')
        curent_b_day = datetime(datetime.now().year, b_day.month, b_day.day)
        
        if check_b_day(curent_b_day):
            b_list.append(f'{curent_b_day.date()}:{i["name"]}')
    print_result(group_list(b_list))
    

if __name__ == '__main__':

    users = ({'name': 'Jane', 'birthday': '05.07.2002'},
             {'name': 'Lizz', 'birthday': '02.03.1990'},
             {'name': 'Jull', 'birthday': '03.03.2000'},
             {'name': 'Adellin', 'birthday': '28.02.2003'},
             {'name': 'Billy', 'birthday': '27.02.2000'},)

congratulate(users)
