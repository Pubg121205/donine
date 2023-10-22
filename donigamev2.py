import os, sys
d = '\x1b[1;91m'
xl = '\x1b[1;92m'
v = '\x1b[1;93m'
xb = '\x1b[1;96m'
t = '\x1b[1;97m'
vio = '\x1b[1;95m'
key = input('Nhập key tại đây: ')
if key == '':
   print('sai key')
   os.sys.exit()
elif key == 'DGAME':
   print('key đúng')
else:
   print('key sai')
   os.sys.exit()
def yn():
  write(f)
  cnbn = input('Bạn muốn chơi lại hay về menu? [y/n/A] :')
  if cnbn == 'y' or cnbn == 'Y':
    menu()
  elif cnbn == 'n' or cnbn == 'N':
    print(' Cám ơn bạn đã sử dụng công cụ của tôi')
    os.sys.exit()
  else:
    print('[!] Nhập sai')
    os.sys.exit()

import os 
banner = """
██████╗  ██████╗  █████╗ ███╗   ███╗███████╗
██╔══██╗██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ██║██║  ███╗███████║██╔████╔██║█████╗
██║  ██║██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
██████╔╝╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝"""

bang = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ➩ Nhập [1] Game kéo búa bao       ┃
┃ ➩ Nhập [2] Đi lễ                  ┃
┃ ➩ Nhập [0] Menu                   ┃
┃ ➩ Nhập [4] null                   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""
f="""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
def menu():
  print("Đang vào tool, chúc ngày mới vui vẻ")
  print(banner)
  print("Developers:"+" Doni")
  print(f)
  print("Tool trải nghiệm cho mọi người")
  print("Bản quyền by Doni")
  print("Có vấn đề về tool ib zalo: 0936485851")
  print(f)
  print("Cấp độ: FREE")
  print("Tên chủ key: UNKNOWN")
  print(f)
  print("Thông báo: Sắp có tool python bản VIP ")
  print(f)
  print(bang)
  print(f)
  ls = input("Nhập chế độ: ")
  if ls == '01' or ls == '1':
    game1()
  elif ls == '02' or ls == '2':
    di_le()
  elif ls == '00' or ls == '0':
    menu()
  else:
    print("Ghi sai rồi!!!")
    time.sleep(3)
  print("Đang vào tool, chúc ngày mới vui vẻ")
  print(banner)
  print("Developers:"+" Doni")
  print(f)
  print("Tool trải nghiệm cho mọi người")
  print("Bản quyền by Doni")
  print("Có vấn đề về tool ib zalo: 0936485851")
  print(f)
  print("Cấp độ: FREE")
  print("Tên chủ key: UNKNOWN")
  print(f)
  print("Thông báo: Sắp có tool python bản VIP ")
  print(f)
  print(bang)
  print(f)

name = input('Tên bạn là gì: ')
print('Hello bạn '+name+' thanks bạn đã xem tool <3')

print("update game, done")

  
def game1():
    import random   # “nhập cảng” đúng ra là gọi chương trình random của Python 
    choices = ["búa", "lá", "kéo"] # danh sách tên các thứ bạn/computer chọn 
    print("búa thắng kéo. kéo thắng lá. lá thắng búa.") # luật lệ của trò chơi
    player = input("bạn chọn búa, lá hay kéo (or quit)? ") # bạn ra cái gì? búa, giấy hay kéo hay quit?
    while player != "quit":           # Tiếp tục chơi trong khi bạn chưa gõ chữ quit 
        player = player.lower()   # Chuyển cái bạn chọn ra thành chữ thường (lower case)
        computer = random.choice(choices)   # computer chọn ngẫu nhiên một cái trong danh sách choices
        print("You chose " +player+ ", and the computer chose " +computer+ ".") # cho hiện ra cái bạn chọn và cái computer chọn. Dấu + để nối các biến player và computer vào với các string (text) mà thôi
        if player == computer: # nếu giống nhau
            print("hòa rồi!") # giống nhau thì huề
        elif player == "búa":  # nếu bạn chọn búa
            if computer == "kéo": # nếu computer chọn kéo
                print("bạn thắng rồi, chúc mừng <3!")  # bạn thắng
            else:  # nếu không
                print("tôi win rồi, bạn thua!") # computer thắng
        elif player == "lá":  # nếu bạn ra giấy
            if computer == "búa": # và nếu computer ra búa
                print("bạn thắng rồi!") # thì bạn thắng
            else: # nếu không
                print("tôi thắng rồi, bạn thua!") # computer thắng
        elif player == "kéo": # nếu bạn ra kéo
            if computer == "lá": # và nếu computer ra giấy
                print("bạn thắng rồi!") # thì bạn thắng 
            else: # nếu không
                print("tôi thắng rồi, bạn thua!") # computer thắng
        else: 
            print("tôi nghĩ có gì đó sai rồi, báo cho chủ nhân tôi với nhé ")
        print()                             
        player = input("bạn muốn chơi với tôi tiếp không (y/n)? ") 
        if player == "y" or player == "Y":
            game1()
        else:
            menu()

def di_le():
  print('[!]Lưu ý: tool chỉ mang tính chất giải trí và không có mục đích xúc phải 1 cá nhân hay 1 tổ chức nào đó.')
  phat = """
                             _`			
                          _ooOoo_				
                         o8888888o				
                         88" . "88				
                         (| -_- |)				
                         O\  =  /O				
                      ____/`---'\____				
                    .'  \\|     |//  `.			
                   /  \\|||  :  |||//  \			
                  / _||||| -:- |||||_  \			
                  |   | \\\  -  /'| |   |			
                  | \_|  `\`---'//  |_/ |			
                  \  .-\__ `-. -'__/-.  /			
                ___`. .'  /--.--\  `. .'___			
             ."" '<  `.___\_<|>_/___.' _> \"".			
            | | :  `- \`. ;`. _/; .'/ /  .' ; |		
            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		
=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================
                           `=--=-'                    



          _.-/`)
         // / / )
      .=// / / / )
     //`/ / / / /
    // /     ` /
   ||         /
    \\       /
     ))    .'
    //    /
         /"""
  print(phat) 
  uoc = input("Hãy ước điều bạn muốn: ")
  print('Mong bạn 1 ngày tốt lành <3')
  print('Và điều ước sẽ tới với bạn')
  player = input("bạn muốn chơi với tôi tiếp không (y/n)? ") 
   if player == "y" or player == "Y":
         game1()
   else:
         menu()
