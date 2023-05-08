from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
from flask_cors import CORS, cross_origin
import fileReader
import os, time

BASE_DIR =  os.getcwd()
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"} })
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/AllQuizes')
@cross_origin()
def getQuizes():
    names = [x["name"] for x in fileReader.get_all_quizes()]
    
    return jsonify(names)
@app.route("/audio/GetIntros")
def get_intros():
    dir = "data/audio" + getAudioPathOfType("intro")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    return jsonify(all_intros)
@app.route("/audio/GetOutros")
def get_outros():
    dir = "data/audio" + getAudioPathOfType("outro")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    return jsonify(all_intros)
@app.route("/audio/GetBGs")
def get_bgs():
    dir = "data/audio" + getAudioPathOfType("bg")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    return jsonify(all_intros)

@app.route("/audio/GetScoreSound")
def get_random_score():
    dir = "data/audio" + getAudioPathOfType("score")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    selected = all_intros[int(time.time()*17/13.0) % len(all_intros)]
    serve_audio("score",selected)
    return ""
@app.route("/audio/GetPenaltySound")
def get_random_penalty():
    dir = "data/audio" + getAudioPathOfType("penalty")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    selected = all_intros[int(time.time()*17/13.0) % len(all_intros)]
    serve_audio("score",selected)
    return ""
@app.route("/audio/GetGreenMarbleSound")
def get_random_greenmarble():
    dir = "data/audio" + getAudioPathOfType("GreenMarble")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    selected = all_intros[int(time.time()*17/13.0) % len(all_intros)]
    serve_audio("score",selected)
    return ""

@app.route("/audio/GetRedMarbleSound")
def get_random_redmarble():
    dir = "data/audio" + getAudioPathOfType("RedMarble")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    selected = all_intros[int(time.time()*17/13.0) % len(all_intros)]
    serve_audio("score",selected)
    return ""

@app.route("/audio/GetJackpotSound")
def get_random_jackpot():
    dir = "data/audio" + getAudioPathOfType("jackpot")
    all_intros = os.listdir(os.path.join(os.getcwd(),dir))
    selected = all_intros[int(time.time()*17/13.0) % len(all_intros)]
    serve_audio("score",selected)
    return ""

@app.route('/audio/<filetype>/<filename>')
def serve_audio(filetype, filename):
    dir = "data/audio/" + getAudioPathOfType(filetype)
    return send_from_directory(dir, filename)


@app.route('/MCQuestion', methods=["GET"])
def MCQuestion():
    quizSelection = request.args.get("quizSelection")
    idx = request.args.get("idx")
    
    #print(quizSelection)
    question = getQuestion(quizSelection, idx)
    answer = question["Answer"]
    question, answers =  pairAndShuffle(question)
    response = {"quizSelection":quizSelection, "question": question, "answers": answers, "answer": answer, "idx": int(idx)+1}
    return jsonify(response)



@app.route('/answer', methods=["GET"])
def Answer():
    idx = request.args.get("idx")
    quizz = request.args.get("quizSelection")
    answer = request.args.get("answer")
    type = request.args.get("quizType")
    correct = request.args.get("isRight")
    if answer == "True":
        fileReader.incrementWin()
    else:
        fileReader.incrementLoss()
    return render_template('Answer.html', quizSelection=quizz, quizType=type, idx=idx, answer=answer, correct=correct)

@app.route("/complete", methods=["GET"])
def Complete():
    answers = fileReader.getScore()
    rightanswers = [answers[0], int(answers[0])+int(answers[1])]
    return render_template("Complete.html", answers=rightanswers)

@app.route('/quiz',methods=["GET"])
def handle_get_quiz():
    name = request.args.get('quizSelection')
    type= request.args.get("quizType")
    print(type)
    return redirect(url_for(type, quizSelection=name, idx=0))

@app.route('/question')
def get_question():
    print("get_question", request.args)
    quizType = request.args.get("quizType")
    quizName = request.args.get("quizName")
    print(quizName)
    idx = int(request.args.get("idx"))
    data = getQuestion(quizName, idx)
    if data == -1:
        response = {"quizName":None,"question":None, "quizType":None, "answer":None, "hint":None, "idx":idx, "isComplete":True}
        return jsonify(response)
    print(f"\nquestion: {data}")
    answer = data["Answer"]
    hint = data["Hint"]
    question = data["Question"]
    response = {"quizName":quizName,"question":question, "quizType":quizType, "answer":answer, "hint":hint, "idx":idx+1}
    if quizType== "MultipleChoice":
        pass
    
    return jsonify(response)
@app.route("/setVid")
def setVid():
    data = request.args.get("vidResponse")
    print("setVid",data, request.args)
    runVideo(data)
    return jsonify({})
def pairAndShuffle(question):
    print('pairAndShuffle',question)
    answers = [(question["Answer"], True), (question["Faker1"], False), (question["Faker2"], False), (question["Faker3"], False) ]
    print(answers)
    for answer in answers:
        print(time.time()*7)
        x = int(time.time()*10**7/3.1459) % 4
        print(x)
        tmp = answers[0]
        answers[0] = answers[x]
        answers[x] =  tmp
        time.sleep(.0000001)
    print(answers)
    return question["Question"], answers

def getQuestion(quizName, idx):
    quizes = fileReader.get_all_quizes()
    print("getQuestion",quizName, idx)
    try:
        for quiz in quizes:
            print(quiz, quizName)
            if quiz["name"] == quizName:
                print(idx, quiz)
                print(f"question num {idx} {quiz['data'][str(idx)]}")
                return quiz['data'][str(idx)]
    except:
        return -1
def runVideo(result):
    with open("./Qresult", 'w') as file:
        file.writelines([result])


def getAudioPathOfType(filetype):
    match filetype:
        case "GreenMarble":
            return "effects/GreenMarble"
        case "RedMarble":
            return "effects/RedMarble"
        case "intro":
            return "intros"
        case "outro":
            return "outros"
        case "score":
            return "effects/score"
        case "penalty":
            return "effects/penalty"
        case "jackpot":
            return "effects/jackpot"
        case "bg":
            return "effects/bgs"
    return ""
if __name__=="__main__":
    app.run("0.0.0.0", port=5000)

