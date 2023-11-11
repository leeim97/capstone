from flask import Flask,render_template,request,flash,redirect,url_for
from flask_cors import CORS,cross_origin
import os
from werkzeug.utils import secure_filename
from model import model_f

app =Flask(__name__)
cors = CORS(app)

UPLOAD_FOLDER='/uploads'

b=model_f()
print(len(b))
for i in range(len(b)):
    print(b[i])

#첫화면
@app.route("/")
def home():
    return render_template('index.html') 
#세번째 페이지 태스트
@app.route("/3")
def test():
    return render_template('index3.html')

#두번째페이지를 렌더링
@app.route("/second")
def second_page():
    return render_template('index2.html') 

#두번째 화면에서 업로드 버튼을 누를때
@app.route('/upload',methods=['POST'])
def upload_file():
    if request.method=='POST':
        f=request.files['file']
        
        f.save('./uploads/'+f.filename)
        #딕셔너리 정의(모델에서 딕셔너리 형태로 받을예정)
        grade=dict()
        grade={'adress':40,'take_away':{'iron_parallel':20,'arm_stretch':70},'back_swing':{'head_arm':60,'hand_position':30},'impact':50,'finish':55}
        #코멘트 리스트. 나중에 웹으로 값 전송
        sc=list()
        #코멘트 알고리즘, 점수는 50점일때 각이 일치하는걸 가정, 오차는 5
        for key,value in grade.items():
            if(key=='adress'):
                if(value<45):
                    sc.append('발의 각도가 좁아요 어깨만큼 넓혀주세요ㅜㅜ.')
                elif(value<=55 & value>=45):
                    sc.append('어드레스의 발 사이의 거리가 좋아요^^.')
                elif(value>55):
                    sc.append('발 사이의 거리가 너무 멀어요ㅜㅜ.')
                    
            elif(key=='take_away'): #채 수평(손목좌표)과 팔 쭉 펴진지 나중에
                for inner_key,inner_value in value.items():
                    
                    if(inner_key=='iron_parallel'): # 채부분
                        if(inner_value<45):
                            sc.append('채가 아래로 향해 있어요. 채를 수평에 맞추어 주세요.')
                        elif(inner_value<=55 & inner_value>=45):
                            sc.append('채의 각도와 손목이 훌륭해요^^.')
                        elif(inner_value>55):
                            sc.append('채가 위로로 향해 있어요. 채를 수평에 맞추어 주세요.')
                            
                    #팔
                    elif(inner_key=='arm_stretch'):                      
                        if(inner_value<45):
                            sc.append('팔을 쭉 펴주세요!')
                        else:
                            sc.append('팔이 잘 펴져있어요^^.')
                          
            #뱌ㅐㄱ스윙
            elif(key=='back_swing'): 
                for inner_key,inner_value in value.items():
                    
                    #왼팔어깨와 머리 사이의 거리값?
                    if(inner_key=='head_arm'):
                        if(inner_value<45):
                            sc.append('왼쪽 어깨가 얼굴 아래에 잘 부착 되있어요!')
                        elif(inner_value>=45):
                            sc.append('왼쪽 어깨를 얼굴아래로 부착시켜주세요!')
                            
                    #손의 위치기 너무 낮거나 머리를 넘어가면 안되는 부분
                    elif(inner_key=='hand_position'):                      
                        if(inner_value<45):
                            sc.append('팔을 더 위로 올려주세요!.')
                        elif(inner_value<=55 & inner_value>=45):
                            sc.append('손의 위치기 적절해요.')
                        elif(inner_value>55):
                            sc.append('손이 머리를 넘어가지 않도록 주의 해주세요!.')
                    
            elif(key=='impact'): #고개 위치
                if(value<=55 & value>=45):
                    sc.append('볼을 끝까지 보는 시선 좋아요^^.')
                else:
                    sc.append('임팩트에서 볼을 끝까지 봐야해요!.')
                    
            #시간으로 값을 전달받을듯
            elif(key=='finish'):
                if(value<45):
                    sc.append('피니쉬 자세를 좀 더 유지해 볼까요?')
                else:
                    sc.append('좋아요!')
                       
        #넘기는 리스트 sc의 값은 총 7개
            # 어드레스 한개
            # 테이크어웨이 두개(채가 지면과 평행,팔 쭉펴주기)
            # 백스윙 두개(왼쪽 어깨와 머리사이 거리,손 위치)
            # 임팩트 한개
            # 피니시 한개
            
        for i in range(7):
            print(sc[i])
        
        #딕셔너리 값을 html로 넘김
        return render_template('index3.html',values=sc)
    else:
        return render_template('index2.html')
    
#마지막 페이지 점수,피드백 그리고 추가적으로 그래프
@app.route('/third')
def func():
    return '완료'
        
    

if __name__=='__main__':
    app.run(host="127.0.0.1",port="5000")