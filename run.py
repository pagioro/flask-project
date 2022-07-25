import os
import json
from flask import Flask, render_template 


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html") # importa o index.html

    
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data: # abre o arquivo json criado, r is ready only e joga na variavel json_data
        data = json.load(json_data) # Variável data recebe json_data acima e será carregada na array data = []
    return render_template("about.html", page_title="About", company=data) # Os dados acima são retornados na variável company
    
    

@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)