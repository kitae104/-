import zipfile
import os

# 압축할 파일과 압축 파일명 정의
source_file = "exam.csv"
zip_file_name = "exam.csv.zip"

# exam.csv를 exam.csv.zip으로 압축
with zipfile.ZipFile(zip_file_name, 'w') as zipf:
    zipf.write(source_file, os.path.basename(source_file))

print(f"{source_file} 파일이 {zip_file_name}으로 압축되었습니다.")

# 압축 풀기
extract_folder = "extracted"
with zipfile.ZipFile(zip_file_name, 'r') as zipf:
    zipf.extractall(extract_folder)

print(f"{zip_file_name}을 {extract_folder} 폴더에 압축 해제하였습니다.")