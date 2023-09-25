scores = []#created a empty list

for i in range(3):
    score = int(input("score: "))
    #scores.append(score)

    scores += [score]
    #this will append

    average = sum(scores) / len(scores)
    print(f"average == {average:.1f}")