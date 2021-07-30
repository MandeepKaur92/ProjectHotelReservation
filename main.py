import webbrowser
import pymongo
import ssl
from flask import Flask, request, render_template, url_for

app = Flask(__name__)
def  connect_to_monogodb():

    connection_string = "mongodb+srv://dbUser:overseas1313@cluster0.6uynl.mongodb.net/HotelReservation?retryWrites=true&w=majority"
    my_client = pymongo.MongoClient(connection_string, ssl_cert_reqs=ssl.CERT_NONE)
    # print(my_client)
    db = my_client["HotelReservation"]
    return db;

# http://127.0.0.1:5000/
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('hotelIndex.html')


# Using Jinja2 template
# http://127.0.0.1:5000/Gallery
@app.route('/Gallery')
def Gallery():
    return render_template('Gallery.html')  # Using render function from flask



# http://127.0.0.1:5000/services
@app.route('/services')
def services():
    return render_template('services.html')  # Using render function from flask

#http://127.0.0.1:5000/booking2
@app.route('/booking')
def booking():
    return render_template('booking2.html')  # Using render function from flask

#http://127.0.0.1:5000/cancel
@app.route('/cancel')
def cancel():
    return render_template('cancel.html')  # Using render function from flask
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Using render function from flask

#http://127.0.0.1:5000/avail
@app.route('/avail')
def avail():
    return render_template('avalibility.html')  # Using render function from flask


# http://127.0.0.1:5000/History

@app.route('/history')
def history():
    return render_template('History.html')  # Using render function from flask




@app.route('/setFeedBackDetials', methods=['GET', 'POST'])
def setFeedBackDetials():
    if request.method == 'POST':
        firstname = request.form.get('fname')
        email = request.form.get('email')
        phone= request.form.get('phone')
        message=request.form.get('message')
        print(firstname,email,phone,message)
        result ='''  <h1>First Name : {}<h1>  <h1>Email : {}<h1> <h1>phone: {}<h1> <h1>message : {}<h1>'''

    return result.format(firstname,email ,phone,message)

    db=connect_to_monogodb()
    print(db.list_collection_names())
    cBookingDetials = db["FeedBackDetials"]

    cBookingDetials.insert({'firstname':firstname,'email':email,'phone':phone,'message':message})

    results = cBookingDetials.find()
    print(results)
    for row in results:
        print(row)
    message="Booking successfully complete"

    return render_template('hotelIndex.html',message=message)
#http://127.0.0.1:5000/setContactDetials
@app.route('/setContactDetials', methods=['GET', 'POST'])
def setContactDetials():
    db = connect_to_monogodb()
    print(db.list_collection_names())
    cBookingDetials = db["ContactDetials"]
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        Message= request.form.get('Message')
        Email=request.form.get('Email')
        result ='''  <h1>First Name : {}<h1>
                              <h1>Last Name : {}<h1> 
                              <h1>Message: {}<h1>
                '''

    #return result.format(firstname, lastname,Message)
    cBookingDetials.insert({'firstname': firstname, 'lastname': lastname, 'Message': Message,'Email':Email})

    results = cBookingDetials.find()
    print(results)
    for row in results:
        print(row)
    message = "Meessage send Successfully"

    return render_template('hotelIndex.html', message=message)


@app.route('/getBookingDetials', methods=['GET', 'POST'])
def getBookingDetials():
    if request.method == 'POST':
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

    db=connect_to_monogodb()
    print(db.list_collection_names())
    cBookingDetials = db["BookingDetials"]
    result={'firstname':firstname,'lastname':lastname,'country':country,'Email':Email,'PhoneNumber':PhoneNumber,
                            'No_of_adult':No_of_adult,'No_of_kids':No_of_kids,'No_of_rooms':room,'Room_Type':typeroom,'CheckIn':CheckIn,'CheckOut':CheckOut}
    cBookingDetials.insert({'firstname':firstname,'lastname':lastname,'country':country,'Email':Email,'PhoneNumber':PhoneNumber,
                            'No_of_adult':No_of_adult,'No_of_kids':No_of_kids,'No_of_rooms':room,'Room_Type':typeroom,'CheckIn':CheckIn,'CheckOut':CheckOut})

    results = cBookingDetials.find()
    print(results)
    for row in results:
        print(row)
    message="Booking successfully complete"
    #return render_template('hotelIndex.html',message=message)
    return render_template('BookingMessage1.html', results=result)

# http://127.0.0.1:5000/checkLogin
@app.route('/checkLogin', methods=['GET', 'POST'])
def checkLogin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        message = "successfully complete"
        if(username=="mandeep"):
             if(password=="123"):

                 return render_template('adminWelcome.html', message=message)
        else:
            return render_template('message.html', message=message)
        
 
 
# http://127.0.0.1:5000/Login
@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/setbookcancel', methods=['GET', 'POST'])
def setbookcancel():
    if request.method == 'POST':
        PhoneNumber=request.form.get('PhoneNumber')
        room = request.form.get('room')
        typeroom = request.form.get('typeroom')
        CheckIn= request.form.get('CheckIn')
        CheckOut=request.form.get('CheckOut')

        #result ='''  <h1>No. room: {}<h1>  <h1>typeroom : {}<h1> <h1>CheckIn: {}<h1> <h1> CheckOut : {}<h1>'''

   # return result.format(room,typeroom , CheckIn, CheckOut)
    db = connect_to_monogodb()
    cBookingDetials = db["BookingDetials"]
    results = cBookingDetials.remove({'$and':[{"PhoneNumber":PhoneNumber,"No_of_rooms":room,"CheckIn":CheckIn,"CheckOut":CheckOut,"Room_Type":typeroom}]})
    print(results)


    result ='''  <h1>{}<h1> '''
    return result.format("BOOKING CANCEL SUCCESSFULLY")

@app.route('/setbookAvail', methods=['GET', 'POST'])
def setbookAvail():
    if request.method == 'POST':
        room = request.form.get('room')
        typeroom = request.form.get('typeroom')
        CheckIn= request.form.get('CheckIn')
        CheckOut=request.form.get('CheckOut')

        #result ='''  <h1>No. room: {}<h1>  <h1>typeroom : {}<h1> <h1>CheckIn: {}<h1> <h1> CheckOut : {}<h1>'''

   # return result.format(room,typeroom , CheckIn, CheckOut)
    db = connect_to_monogodb()
    cBookingDetials = db["AvailableRooms"]
    results = cBookingDetials.find({"No_of_rooms":room,"CheckIn":CheckIn,"CheckOut":CheckOut,"Room_Type":typeroom})
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
def sethistory():
    if request.method == 'POST':
        typeroom = request.form.get('typeroom')
        CheckIn = request.form.get('CheckIn')
        CheckOut = request.form.get('CheckOut')
        db = connect_to_monogodb()
        cBookingDetials = db["BookingDetials"]
        col=['firstname', 'lastname', 'country', 'Email', 'PhoneNumber', 'No_of_adult', 'No_of_kids', 'No_of_rooms', 'Room_Type', 'CheckIn', 'CheckOut']
        results = cBookingDetials.find({'$and':[{"CheckIn": CheckIn, "CheckOut": CheckOut, "Room_Type": typeroom}]},col)
        return render_template('showhistory.html', results=results)



if __name__ == '__main__':
    app.run()
