import os
url = 'https://ck101.com/forum.php?mod=forumdisplay&fid=3581&page={}'
for row in range(1, 50):
    url_ = url.format(row)
    cmd = 'start C:\\Users\\jimga\\AppData\\Local\\Programs\\Python\\Python37\\python.exe '+ "D:\卡提若\ck101.py " + "" + str(row) + "" 
    # print(cmd)
    os.system(cmd)
