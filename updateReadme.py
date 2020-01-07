# 自动更新README.md中的目录内容

import os

# 获取当前文件下文件名列表存入listDir
listDir = [d for d in os.listdir('.')]
# 对获取的目录做筛选，忽略隐藏文件***
# 设置REAMD.md一级标题名字
title1 = '工程目录'


print('===开始更新README.md===')

# 判断当下目录有没有README.md，有则展示原内容
if 'README.md' in listDir:
    print('README.md 原内容：')
    with open('./README.md', 'r', encoding='utf-8', errors='ignore') as f:
        print(f.read())
else:
    print('在当前目录下创建一个README.md')

# 写入内容：
print('开始更新内容')
with open('./README.md', 'w', encoding='utf-8') as f:
    f.writelines('# ' + title1 + '\n\n')
    i = 0
    for ldir in listDir:
        i += 1
        f.writelines('   %d. ' % i + ldir + '\n')

# 更新后内容
print('README.md 更新后内容：')
with open('./README.md', 'r', encoding='utf-8', errors='ignore') as f:
    print(f.read())

print('更新成功')

# 将dirList中的文件名写入README.md中
print('===更新结束===')