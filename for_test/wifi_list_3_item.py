available_wifi_list = [['aaaa', 'Good'], ['bbbb', 'Good'], ['cccc', 'Good'], ['dddd', 'Good'], ['eeee', 'Good'], ['ffff', 'Good'], ['gggg', 'Good'], ['hhhh', 'Good'], ['iiii', 'Good'], ['jjjj', 'Good'], ['kkkk', 'Good']]
showing_wifi_list = []
last_num = len(available_wifi_list) -1

current_start_num = 0
current_end_num = 2


while(1):
    showing_wifi_list = available_wifi_list[current_start_num:current_end_num+1]
    print(showing_wifi_list)
    cmd = input()
    if cmd == 'u':
        print('Up Btn Clicked')
        if current_end_num < last_num:
            current_start_num += 1
            current_end_num += 1
        else:
            print('No More Items')
        
    elif cmd == 'd':
        print('Downu Btn Clicked')
        if current_start_num > 0:
            current_start_num -= 1
            current_end_num -= 1
        else:
            print('No Previous Items')