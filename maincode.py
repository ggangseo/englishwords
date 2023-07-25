
import time
spellings = []
mean = []
title = input("단어장 제목을 입력하세요 :")
print("지금부터 단어의 철자와 뜻을 각각 입력해 주세요.")
time.sleep(0.2)
print("최대50개 까지 작성하실 수 있으시며 end를 입력시 50회 이전에 입력이 완료됩니다.")
time.sleep(0.3)
for i in range(0,50):
    spellings.append(input("철자를입력하세요."))
    if spellings[i].lower() == "end":
        break
    mean.append(input("뜻을입력하세요:"))
    print(spellings)
    
f = open("C:/Users/ggangseo/Desktop/englishwords/%s.txt"%title, mode='w')#저장파일생성

cnt = len(spellings)
for k in range(0,cnt):
    f.write("%s %s"%(spellings[k],mean[k]))
f.close

     
    