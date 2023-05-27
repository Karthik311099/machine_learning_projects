from flask import Flask, request
import sys
from HousingE

app= Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
 
def hel():
    return 'HELLO WORLD'

if __name__=='__main__':
    app.run(debug=True)
 