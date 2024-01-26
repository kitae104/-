#1 필요한 라이브러리 설치하기
import pandas as pd
import os

#기초 폴더
bacic_folder = 'new_data' #new_data 한글데이터입니다/ 하지만 코랩에서 압축해제시 한글파일이 문제가 있을 수 있음
#영어로 전환을 원할경우 'new_dats2' 로 바꿔줘야함

#2 엑셀취합자료의 자료 가져오기
file_list = os.listdir(f"./{bacic_folder}")
file_list_xls = []
for a in file_list:
    if ".xls" in a:
        file_list_xls.append(a)
file_list_xls

#3.각각의 엑셀파일을 편집후와 함께 저장한다.
data_unit_sum = pd.DataFrame()
for b in file_list_xls:
    df = pd.read_excel(f"./{bacic_folder}/"+b)
    df['나라'] = b.split("_")[1]
    data_unit = df[['나라','조사제품','제목','내용']]
    data_unit_sum = pd.concat([data_unit_sum, data_unit], axis = 0)
data_unit_sum.to_excel('combined_excel.xlsx')

#4. 만들어진 파일을 기반으로 제품별로 구분하여 분할 저장하기
product_list = data_unit_sum['조사제품'].value_counts()
for d in dict(product_list):
    xls_name = data_unit_sum[data_unit_sum['조사제품']==d]
    xls_name.to_excel(f"{d}.xlsx")