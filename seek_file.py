# -*- coding: utf-8 -*-
import sys
from easygui import *  
import os

def list_file(directory,leixing):
    file_list = []
    pwd_list = os.listdir(directory)
    for i in pwd_list:
        if '.' not in i: # 如果是目录的话
            try:
                now_pwd = directory + '\\' + i  #得到目录的绝对路径
                l_list= list_file(now_pwd,leixing) #在目录中统计代码行数
                if l_list:
                    file_list.extend(l_list)
            except:
                pass
        else:  #如果不是目录，对文件进行分析
            if leixing in i:
                file_list.append(i)
    return file_list

def dict_file(directory,leixing):
    file_dict = {}
    pwd_list = os.listdir(directory)
    for i in pwd_list:
        if '.' not in i: # 如果是目录的话
            try:
                now_pwd = directory + '\\' + i  #得到目录的绝对路径
                temp_dict= dict_file(now_pwd,leixing) #在目录中统计代码行数
                if temp_dict:
                    file_dict.update(temp_dict)
            except:
                pass
        else:  #如果不是目录，对文件进行分析
            if leixing in i:
                file_dict[i] = directory
    return file_dict

            
if __name__ == "__main__":
    directory = diropenbox('','请选择一个目录',default='G:\\博客文章')             
    #file_list = list_file(directory,'.pdf')
    file_dict = dict_file(directory,'.pdf')
    print(file_dict)


