from flask import Flask, jsonify, request
app = Flask(__name__)

appointments = [
  { 'id': "1",'doctor': "1", 'date': "21 Nov 2023", 'rating':"Good"  },
  { 'id': "2",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "3",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "4",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "5",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "6",'doctor': "3", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "7",'doctor': "4", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "8",'doctor': "5", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "9",'doctor': "6", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "10",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "11",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "12",'doctor': "3", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "13",'doctor': "4", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "14",'doctor': "5", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "15",'doctor': "6", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "16",'doctor': "1", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "17",'doctor': "2", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "18",'doctor': "3", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "19",'doctor': "4", 'date': "22 Nov 2023", 'rating':"Good"  },
  { 'id': "20",'doctor': "5", 'date': "22 Nov 2023", 'rating':"Bad"  },
  { 'id': "21",'doctor': "6", 'date': "22 Nov 2023", 'rating':"Good"  }
]
@app.route('/hello')
def hello():
  greeting = "Hello world!"
  return greeting

@app.route('/appointments', methods=["GET"])
def getAppointments():
  return jsonify(appointments)

@app.route('/appointment/<id>', methods=["GET"])
def getAppointment(id):
  id = int(id) - 1
  return jsonify(appointments[id])

if __name__ == "__main__":
  app.run(host="0.0.0.0",port=7070)