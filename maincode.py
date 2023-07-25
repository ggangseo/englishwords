
title = input("단어장 제목을 입력하세요")

for i in range(0,50):
    spellings[i] = input("철자를입력하세요.")
    mean[i] = input("뜻을입력하세요:")

f = open("c:\Users\user\Desktop\영어단어암기%s.txt"%title,'w')#저장파일생성

cnt = len(spellings)
for k in range(0,cnt):
    f.write("%s %s"%(spellings[k],mean[k]))
f.close

     
    