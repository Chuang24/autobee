from flask import Flask, render_template , request
from generate import generate, createScriptZendesk,createScriptCisco
import phone_number 
from phone_number import getTimeZone,getAreaName,getLocalTime
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        id=request.form["id"]
        name=request.form["cx_name"]
        pNumber=request.form["cx_pNumber"]
        email=request.form["cx_email"]
        sNumber=request.form["cx_sNumber"]
        ticketID=request.form["cx_ticketID"]
        
        generate(name,pNumber,email,ticketID,sNumber)
    
        zendeskScript=createScriptZendesk(id,name,pNumber,email,sNumber)
        ciscoScript=createScriptCisco(name,pNumber,email,ticketID,sNumber)
        areaName = getAreaName(pNumber)
        timeZone = getTimeZone(pNumber)
        localTime=getLocalTime(timeZone)
        
        return render_template("success.html",zendesk=zendeskScript, cisco=ciscoScript, areaName=areaName, timeZone=timeZone, localTime=localTime) 
      
@app.route('/button_goback')
def button_goback():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug =True
    app.run()
