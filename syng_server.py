from db_work import not_send_info
import requests
import json
from socket import gethostbyname_ex, gethostname


def get_user_ip():
    find_ip = gethostbyname_ex(gethostname())[2]
    return ''.join(find_ip)


def create_json():
    not_send_info_ls = not_send_info()
    data_packet = []
    user_ip = get_user_ip()
    for row in not_send_info_ls:
        data_info = {
                    'row_id': row.id,
                    'user_ip': user_ip,
                    'active_tab_url': row.active_tab_url,
                    'pycharm_project': row.pycharm_project,
                    'sublime_path': row.sublime_path,
                    'app_name': row.app_name,
                    'timestamp': row.timestamp.isoformat()
                     }
        data_packet.append(data_info)

    return json.dumps(data_packet)


def send_json_to_server():
    json_send = create_json()
    server_url = 'http://127.0.0.1:5000/api/v1/save_info_data'
    try:
        send_data = requests.post(server_url, json = json_send)
        if send_data.status_code in [200, 201]:
            print(send_data.text)
        else:
            print('Что то пошло не так. Код: {}'.format(send_data.status_code))

    except requests.exceptions.ConnectionError:
        print('Подключение не установлено. Попробуйте позже')



if __name__ == '__main__':
    #print(create_json())
    send_json_to_server()