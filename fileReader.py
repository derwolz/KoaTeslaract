import os
def get_all_quizes():
    quizes = []
    dir = os.getcwd() + "/data/"
    
    for  filename in os.listdir(dir):
    
        if filename[-3:] == "csv":
            with open(os.path.join(dir, filename)) as file:
                lines = file.readlines()
                keys = lines[0].split(',')
                lines.pop(0)
                quiz ={}
                qnumber = 0
                for line in lines:
                    data = line.split(',')
                    
                    question = {}
                    for d in range(len(data)):
                        question[keys[d].replace("\n","")] = data[d].replace("\n", "")
                    quiz[str(qnumber)] = question
                    qnumber += 1
                quizes.append({"name":filename[:-4] ,"data": quiz})
    return quizes
             
def getScore():
    with open(os.getcwd()+"/data/.winnLoss") as file:
        line = file.readline()
        return line.split(":")
    pass
def resetScore():
    with open(os.getcwd()+"/data/.winnLoss", "w") as file:
        file.write("0:0")
    pass
def incrementWin():
    score = getScore()
    num = int(score[0])
    
    num += 1
    line = f"{num}:{score[1]}"
    with open(os.getcwd() + "/data/.winnLoss", "w") as file:
        
        file.write(line)
    
def incrementLoss():
    score = getScore()
    num = int(score[1])
    num += 1
    line = f"{num}:{score[0]}"
    with open(os.getcwd() + "/data/.winnLoss", "w") as file:
        file.write(line)