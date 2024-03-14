from flask import Flask, render_template, request
import json
import os
import csv
from datetime import date
from datetime import datetime


id_lst = ['btn_1', 'btn_2', 'btn_3', 'btn_4', 'btn_5', 'btn_6', 'btn_7', 'btn_8', 'btn_9', 'btn_10', 'btn_11', 'btn_12', 'btn_13', 'btn_14', 'btn_15', 'btn_16', 'btn_17']
def get_date():
	curr_date = date.today()
	print( curr_date)
	return curr_date

def get_time():
	curr_time = datetime.now().strftime("%H:%M")
	print(curr_time)
	return curr_time



app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/button-click", methods=["POST"])
def button_click():
    return "Chấm tăng ca rồi nha."

@app.route("/button", methods=["POST"])

# def handle_button():
#     button_id = request.json['buttonId']
#     person_name = request.json['content']
#     print(person_name)
#     desktop_folder = os.path.expanduser("~/Desktop")
#     file_path = os.path.join(desktop_folder, "history.json")
#     with open(file_path, 'a') as file:
#         file.write(json.dumps(person_name))
#         file.write('\n')
#     return 'Button content received'

# def handle_button():

#     button_id = request.json['buttonId']
#     person_name = request.json['content']
#     person_date = request.json['date']
#     person_time = request.json['time']
#     person_json = {
#         'name' : person_name, 
#         'date' : person_date, 
#         'time' : person_time
#     }
#     for i in id_lst:
#         if button_id == i:
#             print(f'{i} button clicked')
#             print(person_name)
#             print(person_date)
#             print(person_time)
#             desktop_folder = os.path.expanduser("~/Desktop")
#             file_path = os.path.join(desktop_folder, "history.json")
#             with open(file_path, 'a') as file:
#                 file.write(json.dumps(person_json))
                
    
#     return 'Button content received.'

def handle_button():

    button_id = request.json['buttonId']
    person_name = request.json['content']
    person_date = get_date()
    person_time = get_time()
    print('type of: ', type(person_name))
    # person_json = {
    #     'name' : person_name, 
    #     'date' : person_date, 
    #     'time' : person_time
    # }
    for i in id_lst:
        if button_id == i:
            print(f'{i} button clicked')
            print(person_name)
            print(person_date)
            print(person_time)
            desktop_folder = os.path.expanduser("~/Desktop")
            file_path = os.path.join(desktop_folder, "history.csv")
            
            with open(file_path, 'a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([person_name, person_date, person_time])
                
    
    return 'Button content received.'



if __name__ == "__main__":
    app.run(port=5500)