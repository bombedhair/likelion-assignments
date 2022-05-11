QnAs = []
while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        QnAs.append({"질문" : question, "답변" : ""})

print("")

for QnA in QnAs:
    print(QnA["질문"])
    answer = input("답변을 입력해주세요 : ")
    QnA["답변"] = answer

print("")
for QnA in QnAs:
    print("Q.",  QnA["질문"])
    print("A.", QnA["답변"])
    print("")