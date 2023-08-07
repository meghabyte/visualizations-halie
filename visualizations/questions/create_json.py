import json
import os


with open('accuracies.json') as json_file:
    accuracies = json.load(json_file)

json_list = []
for model in os.listdir("static"):
    for f in os.listdir("static/"+model+"/"):
        json_dict = {"username":[], "visualization":[], "model":[]}
        username = f.split("_")[1]
        accuracy = accuracies[username]
        link = "https://meghabyte.github.io/visualizations-halie/visualizations/questions/static/"+model+"/"+f
        html = '''gridjs.html("<form action='LINK' method='get' target='_blank'><button class='button' type='submit'>Open</button></form>")'''
        html = html.replace("LINK", link)
        json_dict["username"] = username
        json_dict["visualization"] = html
        json_dict["model"] = model
        json_dict["accuracy"] = accuracy*10
        json_list.append(json_dict)

with open("question_static.json", "w") as f:
    json.dump(json_list, f)
