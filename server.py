from flask import Flask, make_response, render_template, request
from glad_glyphs import glad_glyphs
import os

# Quickstart
'''
cd /Users/annaleuchtenberger/desktop/dev/project/glad_glyphs (the rest of the extension to the folder this file is in)
export FLASK_ENV=development
export FLASK_APP=server.py
flask run

'''

# TODO:
# do I need to set up an environment? 
# how can I test this locally? 
# 

app = Flask(__name__)

@app.route("/")
def home(): 
    return render_template("index.html")
    
@app.route("/get_glad_glyphs", methods=["GET"]) 
def glyphs(): 
    first_word, second_word = request.args.get('w1'), request.args.get('w2')
    query = first_word + " " + second_word
    if len(first_word) == 0 or len(second_word) == 0:
        return render_template("index.html", query=query, result_array=["(no empty boxes plz)"])
    result_array = glad_glyphs(first_word, second_word)
    return render_template("index.html", query=query, result_array=result_array)

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=port) 