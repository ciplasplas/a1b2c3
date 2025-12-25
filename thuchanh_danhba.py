n = input('Enter "s" to go to Start Menu: ')
danh_ba = []
while n == 's':
    print('---' + 'Menu' + '---')
    print('Options:')
    print('Thêm liên lạc')
    print('Xóa liên lạc')
    print('Cập nhật liên lạc')
    print('Tìm kiếm liên lạc')
    print('Hiển thị tất cả')
    print('Thoát ứng dụng')

    choice = input('Please select an option: ')

    if 'oat' in choice or 'oát' in choice:
        print('Good bye!')
        break

    elif 'hêm' in choice or 'hem' in choice:
        so_luong = int(input('Hãy nhập số lượng liên lạc bạn muốn thêm: '))
        for x in range(1,so_luong+1):
            choice1 = input('Please enter name and phone number: ').split()
            danh_ba.append(choice1)
            print('Đã thêm liên lạc vào danh bạ !')
            print(f'Danh bạ của bạn hiện tại: {danh_ba}')
        exitt = input('Chọn quay lại để quay trở về Menu: ')
        if 'quay' in exitt or 'Quay' in exitt:
            continue

    elif 'óa' in choice or 'oa' in choice:
        if len(danh_ba) == 0 :
            t = input('Bạn không có liên lạc để xóa, hãy chọn quay lại để thêm liên lạc: ')
            if 'quay' in t or 'Quay' in t:
                continue
        else:
            choice2 = input('Chọn tên hoặc số của liên lạc trong danh bạ bạn muốn xóa: ')
            for x in danh_ba:
                if choice2 or int(choice2) in x:
                    danh_ba.remove(x)
                    print('Đã xóa liên lạc')
                    break
            exitt2 = input('Chọn quay lại để quay trở về Menu: ')
            if 'quay' in exitt2 or 'Quay' in exitt2:
                continue

    elif 'cập' in choice or 'Cập' in choice or 'cap' in choice or 'Cap' in choice:
        if len(danh_ba) == 0 :
            y = input('Bạn chưa có liên lạc để cập nhật, hãy chọn quay lại Menu để thêm liên lạc: ')
            if 'quay' in y or 'Quay' in y:
                continue
        else:
            a = 0
            choice3 = input('Hãy chọn tên của liên lạc bạn muốn sửa: ')
            for x in danh_ba:
                if danh_ba[a][0] != choice3 and a!= len(danh_ba)-1:
                    a+=1
                elif danh_ba[a][0] != choice3 and a == len(danh_ba) - 1:
                    choice3_phu =input('Bạn chưa có tên này trong danh bạ, hãy chọn quay lại Menu để thêm hoặc cập nhật liên lạc khác: ')
                    if 'quay' in choice3_phu or 'Quay' in choice3_phu:
                        break
                else:
                    a = 0
                    choice3_2 = input('Bạn muốn sửa tên, số hay sửa cả tên cả số ?: ')
                    if (('số' not in choice3_2) and ('Số' not in choice3_2)) and (('tên' in choice3_2) or ('Tên' in choice3_2)):
                        choice3_3 = input('Nhập tên mới: ')
                        for b in danh_ba:
                            if choice3 not in b:
                                a+=1
                            if choice3 in b:
                                danh_ba[a][0] = choice3_3
                                a = 0
                                print('Đã cập nhật tên liên lạc mới')
                        exitt3 = input('Chọn quay lại để quay trở về Menu: ')
                        if 'quay' in exitt3 or 'Quay' in exitt3:
                            break
                    elif (('số' in choice3_2) or ('Số' in choice3_2)) and (('tên' in choice3_2) or ('Tên' in choice3_2)):
                        choice3_4 = input('Nhập tên và số mới: ').split()
                        for y in danh_ba:
                            if choice3 not in y:
                                a+=1
                            if choice3 in y:
                                danh_ba[a][0] = choice3_4[0]
                                danh_ba[a][1] = choice3_4[1]
                                a = 0
                                print('Liên lạc đã được cập nhật')
                        exitt4 = input('Chọn quay lại để quay trở về Menu: ')
                        if 'quay' in exitt4 or 'Quay' in exitt4:
                            break
                    elif (('số' in choice3_2) or ('Số' in choice3_2)) and (('tên' not in choice3_2) and ('Tên' not in choice3_2)):
                        choice3_5 = input('Nhập số mới: ')
                        for z in danh_ba:
                            if choice3 not in z:
                                a+=1
                            if choice3 in z:
                                danh_ba[a][1] = choice3_5
                                print('Số mới đã được cập nhật')
                        exitt5 = input('Chọn quay lại để quay trở về Menu: ')
                        if 'quay' in exitt5 or 'Quay' in exitt5:
                            break

    elif 'tìm' in choice or 'tim' in choice or 'Tìm' in choice or 'Tim' in choice:
        if len(danh_ba) == 0 :
            choice4_phu2 = input('Danh bạ trống, hãy chọn quay lại để thêm liên lạc: ')
            if 'quay' in choice4_phu2 or 'Quay' in choice4_phu2:
                break
        else:
            a = 0
            choice4 = input('Hãy nhập tên liên lạc cần tìm kiếm: ')
            for x in danh_ba:
                if choice4 not in x and a!= len(danh_ba)-1:
                    a+=1
                elif choice4 not in x and a== len(danh_ba)-1:
                    choice4_phu = input('Tên này chưa có trong liên lạc, hãy chọn quay lại Menu để thêm liên lạc hoặc tìm liêm lạc khác: ')
                    if 'quay' in choice4_phu or 'Quay' in choice4_phu:
                        break
                else:
                    a = 0
                    for i in danh_ba:
                        if choice4 not in i:
                            a+=1
                        if choice4 in i:
                            print(danh_ba[a])
                    exitt6 = input('Chọn quay lại để quay trở về Menu: ')
                    if 'quay' in exitt6 or 'Quay' in exitt6:
                        break
    elif 'hiển' in choice or 'hien' in choice or 'Hiển' in choice or 'Hien' in choice:
        if len(danh_ba) == 0 :
            thoat = input('Danh bạ củ bạn hiện chưa có liên lạc nào, chọn quay lại để thêm liên lạc: ')
            if 'quay' in thoat or 'Quay' in thoat:
                continue
        else:
            print(f'Danh bạ của bạn: {danh_ba}')
            exitt7 = input('Chọn quay lại để quay trở về Menu: ')
            if 'quay' in exitt7 or 'Quay' in exitt7:
                continue



























