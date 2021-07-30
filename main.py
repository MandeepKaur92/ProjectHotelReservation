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





if __name__ == '__main__':
    app.run()
