import webbrowser
import pymongo
import ssl
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
#connect program to database monogodb
def  connect_to_monogodb():

    connection_string = "mongodb+srv://dbUser:overseas1313@cluster0.6uynl.mongodb.net/HotelReservation?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string, ssl_cert_reqs=ssl.CERT_NONE)
    # print(my_client)
    db = my_client["HotelReservation"]
    return db;

# http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
#to show hotelIndex webpage
def hello_world():
    return render_template('hotelIndex.html') # Using render function from flask


# Using Jinja2 template
# http://127.0.0.1:5000/Gallery
@app.route('/Gallery')
#to show Gallery webpage
def Gallery():
    return render_template('Gallery.html')  # Using render function from flask



# http://127.0.0.1:5000/services
@app.route('/services')
#to show services webpage
def services():
    return render_template('services.html')  # Using render function from flask

#http://127.0.0.1:5000/booking2
@app.route('/booking')
#to show booking2 webpage
def booking():
    return render_template('booking2.html')  # Using render function from flask

#http://127.0.0.1:5000/cancel
@app.route('/cancel')
#to show cancel webpage
def cancel():
    return render_template('cancel.html')  # Using render function from flask
@app.route('/contact')
#to show contact webpage
def contact():
    return render_template('contact.html')  # Using render function from flask

#http://127.0.0.1:5000/avail
@app.route('/avail')
#to show avalibility webpage
def avail():
    return render_template('avalibility.html')  # Using render function from flask


# http://127.0.0.1:5000/History
@app.route('/history')
#to show history webpage
def history():
    return render_template('History.html')  # Using render function from flask

# http://127.0.0.1:5000/Login
@app.route('/login')
#to show Login webpage
def login():
    return render_template('Login.html') # Using render function from flask





@app.route('/setFeedBackDetials', methods=['GET', 'POST'])
#to store feedback in database
def setFeedBackDetials():
    if request.method == 'POST':
        #retrieve data from textbox
        firstname = request.form.get('fname')
        email = request.form.get('email')
        phone= request.form.get('phone')
        message=request.form.get('message')
    
       # result ='''  <h1>First Name : {}<h1>  <h1>Email : {}<h1> <h1>phone: {}<h1> <h1>message : {}<h1>'''
        #return result.format(firstname,email ,phone,message)
    
    # call a method for connect with database
    db=connect_to_monogodb()
    print(db.list_collection_names())
    #collection
    cBookingDetials = db["FeedBackDetials"]
     
    #insert data into mongodb
    cBookingDetials.insert({'firstname':firstname,'email':email,'phone':phone,'message':message})
  
    #retreive data from mongodb
    results = cBookingDetials.find()
    print(results)
    #print data
    for row in results:
        print(row)
    message="Booking successfully complete"

    return render_template('hotelIndex.html',message=message)

#http://127.0.0.1:5000/setContactDetials
@app.route('/setContactDetials', methods=['GET', 'POST'])
#method for contact hotel staff and send message save in database
def setContactDetials():
    #for connection call method
    db = connect_to_monogodb()
    
    #print list of all collections
    print(db.list_collection_names())
    
    #ContactDetials collection 
    cBookingDetials = db["ContactDetials"]
    if request.method == 'POST':
        #retreive data from textbox
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        Message= request.form.get('Message')
        Email=request.form.get('Email')
        result ='''  <h1>First Name : {}<h1>
                              <h1>Last Name : {}<h1> 
                              <h1>Message: {}<h1>
                '''

    #return result.format(firstname, lastname,Message)
    
    #save data in monogodb
    cBookingDetials.insert({'firstname': firstname, 'lastname': lastname, 'Message': Message,'Email':Email})

    #retreive data from monogodb
    results = cBookingDetials.find()
    print(results)
    
    #print data
    for row in results:
        print(row)
    message = "Meessage send Successfully"

    return render_template('hotelIndex.html', message=message)


@app.route('/getBookingDetials', methods=['GET', 'POST'])
#method for insert booking detials in database
def getBookingDetials():
    if request.method == 'POST':
        #retrieve data fom textbox
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        country= request.form.get('country')
        Email=request.form.get('Email')
        PhoneNumber=request.form.get('PhoneNumber')
        No_of_adult= request.form.get('No_of_adult')
        No_of_kids = request.form.get('No_of_kids')
        room = request.form.get('room')
        typeroom = request.form.get('typeroom')
        CheckIn = request.form.get('CheckIn')
        CheckOut = request.form.get('CheckOut')
        #result =
        '''  <h1>First Name : {}<h1>
                              <h1>Last Name : {}<h1> 
                              <h1>country: {}<h1>
                              <h1>email : {}<h1>
                              <h1>tel: {}<h1>
                              <h1>Adult : {}<h1>
                              <h1> Kids : {}<h1>
                              <h1> CheckIn : {}<h1>
                              <h1> CheckOut : {}<h1>'''

    #return result.format(firstname, lastname,country,Email,PhoneNumber,No_of_adult, No_of_kids,CheckIn,CheckOut)
    #connection create by  call method connect_to_monogodb()
    db=connect_to_monogodb()
    print(db.list_collection_names())
    
    #collection BookingDetials
    cBookingDetials = db["BookingDetials"]
    result={'firstname':firstname,'lastname':lastname,'country':country,'Email':Email,'PhoneNumber':PhoneNumber,
                            'No_of_adult':No_of_adult,'No_of_kids':No_of_kids,'No_of_rooms':room,'Room_Type':typeroom,'CheckIn':CheckIn,'CheckOut':CheckOut}
    
    #insert booking details in monodb collection "BookingDetials"
    cBookingDetials.insert({'firstname':firstname,'lastname':lastname,'country':country,'Email':Email,'PhoneNumber':PhoneNumber,
                            'No_of_adult':No_of_adult,'No_of_kids':No_of_kids,'No_of_rooms':room,'Room_Type':typeroom,'CheckIn':CheckIn,'CheckOut':CheckOut})

    #retrieve all data from mongodb
    results = cBookingDetials.find()
    print(results)
    for row in results:
        print(row)
    message="Booking successfully complete"
    #return render_template('hotelIndex.html',message=message)
    return render_template('BookingMessage1.html', results=result)

# http://127.0.0.1:5000/checkLogin
@app.route('/checkLogin', methods=['GET', 'POST'])
#method for login to check username and password is valid or not
def checkLogin():
    if request.method == 'POST':
        #retreive data
        username = request.form.get('username')
        password = request.form.get('password')
        message = "successfully complete"
        #compare username and password is valid or not
        if(username=="mandeep"):
             if(password=="123"):
                  #if valid than 'adminWelcome.html' show
                 return render_template('adminWelcome.html', message=message)
        else:
            #if not message show
            return render_template('message.html', message=message)
        
 
 

@app.route('/setbookcancel', methods=['GET', 'POST'])
#method for cancel booking
def setbookcancel():
    if request.method == 'POST':
        #retrieve data form textbox
        PhoneNumber=request.form.get('PhoneNumber')
        room = request.form.get('room')
        typeroom = request.form.get('typeroom')
        CheckIn= request.form.get('CheckIn')
        CheckOut=request.form.get('CheckOut')

      

   #call method for connection
    db = connect_to_monogodb()
    #collection BookingDetials
    cBookingDetials = db["BookingDetials"]
        try:
            
         #delete data from monogodb
        results = cBookingDetials.delete_one({'$and':[{"PhoneNumber":PhoneNumber,"No_of_rooms":room,"CheckIn":CheckIn,"CheckOut":CheckOut,"Room_Type":typeroom}]})
        print(results)
        x=0
        for x in results.find():
            print(x)
          #if data deleted than message show  BOOKING CANCEL SUCCESSFULLY with all detials
        if(x!=0):
            result = '''  <h1>{}<h1>
                                <h1>PhoneNumber:{}<h1>
                                <h1> Number of rooms :{}<h1>
                                <h1>typeroom:{}<h1>
                                <h1> CheckIn:{}<h1>
                                <h1> CheckOut:{}<h1>'''
            return result.format("BOOKING CANCEL SUCCESSFULLY", PhoneNumber, room, typeroom, CheckIn, CheckOut)
        #if data not deleted than message show BOOKING  NOT CANCEL with all detials
        else:
            result = '''  <h1>{}<h1>
                                        <h1>PhoneNumber:{}<h1>
                                        <h1>Number of rooms:{}<h1>
                                        <h1>typeroom:{}<h1>
                                        <h1> CheckIn:{}<h1>
                                        <h1> CheckOut:{}<h1>'''
            return result.format("BOOKING  NOT CANCEL ", PhoneNumber, room, typeroom, CheckIn, CheckOut)
    #if any error occure than message show BOOKING  NOT CANCEL with all detials
    except:
            result = '''  <h1>{}<h1>
                            <h1>PhoneNumber:{}<h1>
                            <h1>room:{}<h1>
                            <h1>typeroom:{}<h1>
                            <h1> CheckIn:{}<h1>
                            <h1> CheckOut:{}<h1>'''
            return result.format("BOOKING  NOT CANCEL ", PhoneNumber, room, typeroom, CheckIn, CheckOut)


@app.route('/setbookAvail', methods=['GET', 'POST'])
#to check rooms are available or not
def setbookAvail():
    if request.method == 'POST':
        #data retreive 
        room = request.form.get('room')
        typeroom = request.form.get('typeroom')
        CheckIn= request.form.get('CheckIn')
        CheckOut=request.form.get('CheckOut')

       
   #create connection
    db = connect_to_monogodb()
    
    #collection AvailableRooms
    cBookingDetials = db["AvailableRooms"]
    
    #match data
    results = cBookingDetials.find({'$and':[{"No_of_rooms":room,"CheckIn":CheckIn,"CheckOut":CheckOut,"Room_Type":typeroom}]})
    print(results)
    total=0
    for row in results:
          total+=int(row["No_of_rooms"])
          print(row)

    message = "Booking successfully complete"

    if(total!=0):
        return render_template('booking2.html', message=message)
    else:
        return render_template('message.html', message=message)
    
    
    @app.route('/sethistory', methods=['GET', 'POST'])
    #to show comfirmed old booking 
def sethistory():
    if request.method == 'POST':
        #retreive data
        typeroom = request.form.get('typeroom')
        CheckIn = request.form.get('CheckIn')
        CheckOut = request.form.get('CheckOut')
        
        #connection create
        db = connect_to_monogodb()
        
        #collection
        cBookingDetials = db["BookingDetials"]
        
        #specific columns that retreive from database
        col=['firstname', 'lastname', 'country', 'Email', 'PhoneNumber', 'No_of_adult', 'No_of_kids', 'No_of_rooms', 'Room_Type', 'CheckIn', 'CheckOut']
        
        #retreive according to query
        results = cBookingDetials.find({'$and':[{"CheckIn": CheckIn, "CheckOut": CheckOut, "Room_Type": typeroom}]},col)
        
        #show data on showhistory
        return render_template('showhistory.html', results=results)



if __name__ == '__main__':
    app.run()
