import requests

url = 'https://www.mashangpa.com/api/problem-detail/2/data/?page={}'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'referer': 'https://www.mashangpa.com/problem-detail/1/',
}

cookies = {
    'sessionid': '77ovww4gy4l6d0w4p3n8ecg40dv435wf',
    'Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0': '1775275201,1776595532,1776786192,1777017275',
    'HMACCOUNT': 'AB9A039B8934E9B8',
    'Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0': '1777017648',
}


def get_single(page_num):
    response = requests.get(url=url.format(page_num), headers=headers, cookies=cookies)
    data = response.json()
    print(data)
    count = 0
    for i in range(0, 10):
        count += data["current_array"][i]
    print(f'第{page_num}页总和：' + f'{count}')
    return count


def main():
    sum_m = 0
    for i in range(1, 21):
        sum_m += get_single(i)
    print(sum_m)


if __name__ == '__main__':
    main()
