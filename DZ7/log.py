def input_write(data: str):
   open('file.txt','a', encoding = 'UTF-8').write(data + '\n')