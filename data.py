import json
from datetime import datetime
from get_info_from_app import get_url_from_active_tab


def save_data(app, tab_url):
    data_list = []
    with open('data.json', 'r', encoding = 'utf-8') as read_data:
        try:
            entrys_from_files = json.loads(read_data.read())
            for entry in entrys_from_files:
                data_list.append(entry)
        except ValueError:
            pass

    date = datetime.now().strftime('%Y-%m-%d T %H:%M:%S')
    new_info = {'app_name': app, 'active_tab_url': tab_url, 'timestamp': date}
    data_list.append(new_info)
    with open('data.json', 'w', encoding = 'utf-8') as write_data:
        write_data.write(json.dumps(data_list, sort_keys = True, indent = 4))


if __name__ == '__main__':
    url = get_url_from_active_tab()
    save_data('Google Chrome', url)