import openpyxl

def excel_generate(list_file,dict_file,leixing):
    wb = openpyxl.workbook.Workbook()
    ws1 = wb.create_sheet(0,title = leixing[1:])
    for i in range(1,len(list_file)+1):
        temp_list = [i,list_file[i-1],dict_file[list_file[i-1]]]
        ws1.append(temp_list)
    wb.save(leixing[1:]+'.xlsx')

if __name__ == '__main__':
    file_list =['hello.pdf','aaa.pdf']
    dict_file = {file_list[0]: 1, file_list[1]:2}
    excel_generate(file_list,dict_file,'.pdf')
