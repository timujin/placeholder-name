import pymysql
import json
#from datetime import datetime, timedelta
import datetime
import lib.db
import lib.util
import urllib
import urllib.request

mysql = {"server":"127.0.0.1",
         "user":"hallofprophecy",
         "password":"hallofprophecy123",
         "port":"3306",
         "database":"hallofprophecy",
         }

conn = 0

def rescheduleDue(due):
        lib.db.addTwitterDue(due, conn)

def scheduleConfirm(due, success):
        due["confirm"] = 1
        due["responseTweetID"] = success
        lib.db.addTwitterDue(due, conn)

def confirmDue(due):
        try:
                post_params = {
                        "key":due["key"],"tweetID":due["tweetID"],"arbiter":due["arbiterHandle"],"responseTweetID":due["responseTweetID"]
                }
                params = json.dumps(post_params).encode('utf-8')
                req = urllib.request.Request("http://hallofprophecy.xyz:8080/confirm/twitter/confirm", data=params,
                             headers={'content-type': 'application/json'})
                response = urllib.request.urlopen(req)
                response = urllib.request.urlopen(req)
                jsonObj = json.loads(response.read().decode('utf-8'))
                print("this->" + str(jsonObj["success"]))
                return jsonObj["success"]
        except Exception as e:
                print("error" + str(e))
                return False

def checkTwitterDues():
        dues = lib.db.popUpcomingTwitterDues(num=20, connection=conn)
        success = None #print("!"+ str(dues))
        for due in dues:
                if (due["confirm"]):
                        success = confirmDue(due)
                        recordJudgement(due, success, conn)
                else:
                        success = askDue(due)
                        if (success):
                                scheduleConfirm(due, success)
                print(success)
                if (not success or success in ["", "Unconfirmed"]):
                        rescheduleDue(due)

def askDue(due):
        try:
                post_params = {
                        "key":due["key"],"tweetID":due["tweetID"],"arbiter":due["arbiterHandle"],"dueDate":due["dueDate"],
                }
                params = json.dumps(post_params).encode('utf-8')
                req = urllib.request.Request("http://hallofprophecy.xyz:8080/confirm/twitter/ask", data=params,
                             headers={'content-type': 'application/json'})
                response = urllib.request.urlopen(req)
                #print ("111" + response.read().decode('utf-8'))
                res = "".join([x for x in response.read().decode('utf-8') if x in list("1234567890")])
                print(res)
                return res
                #jsonObj = json.loads(response.read().decode('utf-8'))
                #print (jsonObj["responseTweetID"])
                #return jsonObj["responseTweetID"]
        except Exception as e:
                print(str(e))
                return False

def recordJudgement(due,success, conn):
    print("Judge: " + str(success))
    if (success):
        lib.db.passJudgement(due["predictionID"], success=="Yes", conn)

if __name__ == "__main__":
    server = mysql["server"]
    user = mysql["user"]
    password = mysql["password"]
    database = mysql["database"]
    conn = pymysql.connect(host=server, user=user, password=password, db=database,cursorclass=pymysql.cursors.DictCursor)

    checkTwitterDues()



