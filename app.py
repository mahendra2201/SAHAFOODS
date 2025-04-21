from flask import Flask, request, render_template,url_for,redirect,jsonify,session
from werkzeug.security import generate_password_hash, check_password_hash
import pymysql
import flash
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import razorpay
razorpay_key_id=""
razorpay_key_secret=""
client=razorpay.Client(auth=(razorpay_key_id,razorpay_key_secret))
from datetime import datetime

verify_otp = "0"
db = {
    "host": "localhost",
    "user": "root",
    "password": "root",  # Replace with your local MySQL password
    "database": "foodhotel"
}
global drinksandicecreams
global items
global vegitems
global nonvegitems

# Email configuration
from_email = ''
email_password = ''

# secret_key = ''

app = Flask(__name__)

@app.route("/")
def basepage():
    return render_template("home.html")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@app.route("/FAQS")
def FAQS():
    return render_template("FAQS.html")

@app.route("/policies")
def policies():
    return render_template("our_policies.html")

@app.route("/logout")
def logout():
    return render_template("home.html")
@app.route("/register",methods=["POST","GET"])
def registerdata():
    if request.method=="POST":
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        cpassword=request.form['confirm-password']
        # print(name)
        # print(username)
        # print(email)
        # print(mobile)
        # print(password)
        # print(cpassword)
        if password==cpassword:
            otp1 = random.randint(111111, 999999)
            global verify_otp
            verify_otp=str(otp1)
            from_email = ''
            to_email = email
            subject = 'OTP For Validation'
            body = f'OTP for Validation is {verify_otp}'

            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', '587')
            server.starttls()
            server.login('', '')
            server.send_message(msg)
            server.quit()

            return render_template("verifyemail.html",name = name,username=username,email=email,mobile=mobile,password=password)
        else:
            return 'make sure that password and confirm password are same'

    else:
        return "<h3 style='color : red'; >Data Get in Wrong Manner</h3>"

@app.route("/verifyemail", methods=["POST", "GET"])
def verifyemail():
    if request.method == "POST":
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        mobile = request.form['mobile']
        password = request.form['password']
        otp = request.form['otp']
        if otp == verify_otp:
            try:
                conn = pymysql.connect(**db)
                cursor = conn.cursor()
                check_query = "SELECT * FROM registers WHERE email = %s OR username = %s"
                cursor.execute(check_query, (email, username))
                existing_user = cursor.fetchone()

                if existing_user:
                    return render_template("invalidregister.html")

                insert_query = "INSERT INTO registers(name, username, email, mobile, password) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(insert_query, (name, username, email, mobile, password))
                conn.commit()
                return render_template("login.html")

            except Exception as e:
                print(e)
                return "<h3 style='color: red;'>An error occurred while processing your request.</h3>"

            finally:
                conn.close()

        else:
            return "<h3 style='color: red;'>Invalid OTP. Please try again.</h3>"

    else:
        return "<h3 style='color: red;'>Invalid request method.</h3>"
    

@app.route("/userlogin", methods=["POST", "GET"])
def userlogin():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        try:
            conn=pymysql.connect(**db)
            cursor=conn.cursor()
            q="select * from registers where username=%s"
            cursor.execute(q,(username,))
            row=cursor.fetchone()
            if(row==None):
                return render_template("invalid_user.html")
            else:
                if password!=row[4]:
                    return "Incorrect Password"
                else:
                        conn=pymysql.connect(**db)
                        cursor=conn.cursor()
                        q="insert into login(username,password) values(%s,%s)"
                        cursor.execute(q,(username,password))
                        conn.commit()
                        return render_template("userhome.html",name=username)

        except Exception as e:
            print(e)
            return "some random errors occured"

        else:
            return render_template("login.html")
    else:
        return "<h3 style='color : red';>Data Get in Wrong Manner</h3>"




@app.route("/adminlogin", methods=["POST", "GET"])
def adminlogin():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Basic validation
        if not username or not password:
            return render_template("login.html")
            
        try:
            conn = pymysql.connect(**db)
            cursor = conn.cursor()
            
            # Check if admin exists with matching credentials
            cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", 
                          (username, password))
            admin = cursor.fetchone()
            
            if admin:
                # Login successful - redirect to dashboard with username as parameter
                return render_template("admin.html",username=username)
            else:
                return render_template("login.html", error="Invalid credentials", username=username)
            
        except Exception as e:
            print(f"Error: {e}")
            return render_template("login.html", error="Login failed. Please try again.")
            
        finally:
            if 'conn' in locals() and conn.open:
                conn.close()
                
    return render_template("login.html")


@app.route('/admin_dashboard',)
def admin_dashboard():
    try:
        conn = pymysql.connect(**db)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        # Get total orders count
        cursor.execute("SELECT COUNT(*) as total FROM orders")
        total_orders = cursor.fetchone()['total']
        
        # Get total revenue
        cursor.execute("SELECT SUM(total_price) as revenue FROM orders")
        total_revenue = cursor.fetchone()['revenue'] or 0
        
        # Get unique customers
        cursor.execute("SELECT COUNT(DISTINCT username) as customers FROM orders")
        total_customers = cursor.fetchone()['customers']
        
        # Get recent 5 orders
        cursor.execute("""
            SELECT username, fooditem, total_price, dat_time 
            FROM orders 
            ORDER BY dat_time DESC 
            LIMIT 5
        """)
        recent_orders = cursor.fetchall()
        
        return render_template("admin_dashboard.html",
            total_orders=total_orders,
            total_revenue=total_revenue,
            total_customers=total_customers,
            recent_orders=recent_orders
        )
        
    except Exception as e:
        print(f"Error: {e}")
        return render_template("error.html",
            message="Failed to load dashboard data"
        )
        
    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

@app.route("/userhome", methods=["POST", "GET"])
def userhome():
    user1=request.args.get('username')
    return render_template("userhome.html",name=user1)
@app.route("/forgotpassword", methods=["POST", "GET"])
def forgotpassword():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if not email or not username or not new_password or not confirm_password:
            return "All fields are required."

        if new_password != confirm_password:
            return "New password and confirm password do not match."

        try:
            conn = pymysql.connect(**db)
            cursor = conn.cursor()

            # Check if email and username exist in the database
            check_query = "SELECT * FROM registers WHERE email = %s AND username = %s"
            cursor.execute(check_query, (email, username))
            user = cursor.fetchone()

            if not user:
                return "Email or username does not exist."

            # Update the password in the database (Plain-Text Password)
            update_query = "UPDATE registers SET password = %s WHERE email = %s AND username = %s"
            cursor.execute(update_query, (new_password, email, username))
            conn.commit()

            return "Password updated successfully. <a href='/login'>Login here</a>"

        except Exception as e:
            print("Error:", e)
            return "An error occurred. Please try again."

        finally:
            cursor.close()
            conn.close()

    return render_template("forgotpassword.html")




@app.route('/products')
def products():
    conn = None
    cursor = None
    try:
        conn = pymysql.connect(**db)
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # Use DictCursor to get results as dictionaries
        
        # Get counts for each category
        cursor.execute("SELECT COUNT(*) as count FROM vegetarian_items")
        veg_count = cursor.fetchone()['count']
        
        cursor.execute("SELECT COUNT(*) as count FROM non_vegetarian_items")
        non_veg_count = cursor.fetchone()['count']
        
        cursor.execute("SELECT COUNT(*) as count FROM drinks_and_icecreams")
        drinks_icecreams_count = cursor.fetchone()['count']
        
        total_items = veg_count + non_veg_count + drinks_icecreams_count
        
        # Get all items from each table
        cursor.execute("SELECT * FROM vegetarian_items")
        veg_items = cursor.fetchall()
        
        cursor.execute("SELECT * FROM non_vegetarian_items")
        non_veg_items = cursor.fetchall()
        
        cursor.execute("SELECT * FROM drinks_and_icecreams")
        drinks_icecreams_items = cursor.fetchall()
        
        return render_template('products.html',
                            total_items=total_items,
                            veg_count=veg_count,
                            non_veg_count=non_veg_count,
                            drinks_icecreams_count=drinks_icecreams_count,
                            veg_items=veg_items,
                            non_veg_items=non_veg_items,
                            drinks_icecreams_items=drinks_icecreams_items)
    
    except pymysql.Error as e:
        print(f"Database error: {e}")
        return "A database error occurred. Please try again later."
    except Exception as e:
        print(f"Unexpected error: {e}")
        return "An unexpected error occurred. Please try again."
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()



@app.route("/menu", methods=["POST", "GET"])
def menu():
    username=request.args.get('username')
    items = [
        {"name": "Chicken Dum Biryani", "price": 180, "image_url": "/static/images/Hyderbad_chicken_biriyani.jpg"},
        {"name": "Cheese Cake", "price": 40, "image_url": "/static/images/chesecake.jpg"},
        {"name": "Veg Noodles", "price": 80, "image_url": "/static/images/veg_noodles.jpg"},
        {"name": "Veg Fried Rice", "price": 70, "image_url": "/static/images/veg_friedrice.jpg"},
        {"name": "Chicken Noodles", "price": 90, "image_url": "/static/images/chicken_noodles.jpg"},
        {"name": "Chicken Fried Rice", "price": 120, "image_url": "/static/images/chicken_friedrice.jpg"},
        {"name": "Chapathi", "price": 40, "image_url": "/static/images/chapathi.jpg"},
        {"name": "Butter Naan", "price": 80, "image_url": "/static/images/buter_nans.jpg"},
        {"name": "Kajju Tomato Curry", "price": 180, "image_url": "/static/images/kajju_tomato_curry.jpg"},
        {"name": "Momos", "price": 130, "image_url": "/static/images/momos.jpg"},
        {"name": "Shawarma", "price": 100, "image_url": "/static/images/shawarma.jpg"},
        {"name": "Pulkas", "price": 10, "image_url": "/static/images/pulka's.jpg"},
        {"name": "Mutton Curry", "price": 350, "image_url": "/static/images/mutton_curry.jpg"},
        {"name": "Chicken Curry", "price": 120, "image_url": "/static/images/chicken_curry.jpg"},
        {"name": "Paneer Butter Masala Curry", "price": 230, "image_url": "/static/images/paneer_butter_masala.jpg"},
        {"name": "Japanese Ramen", "price": 250, "image_url": "/static/images/japanese_ramen.jpg"},
        {"name": "Mutton Paya Soup", "price": 350, "image_url": "/static/images/mutton_payasoup.jpg"},
        {"name": "Thandoori", "price": 450, "image_url": "/static/images/thandoori.jpg"},
        {"name": "Chicken Wings", "price": 220, "image_url": "/static/images/chickenwings.jpg"},
        {"name": "Chicken Nuggets", "price": 230, "image_url": "/static/images/chicken_nuggets.jpg"}
    ]
    return render_template("menu.html",items=items,name=username)
@app.route("/veg")
def vegetarian_menu():
    user2=request.args.get('username')
    vegitems = [
        {"name": "Veg Noodles", "price": 80, "image_url": "/static/images/veg_noodles.jpg"},
        {"name": "Veg Fried Rice", "price": 70, "image_url": "/static/images/veg_friedrice.jpg"},
        {"name": "Chapathi", "price": 40, "image_url": "/static/images/chapathi.jpg"},
        {"name": "Butter Naan", "price": 80, "image_url": "/static/images/buter_nans.jpg"},
        {"name": "Kajju Tomato Curry", "price": 180, "image_url": "/static/images/kajju_tomato_curry.jpg"},
         {"name": "Pulka's", "price": 10, "image_url": "/static/images/pulka's.jpg"},
        {"name": "Cheese Cake", "price": 40, "image_url": "/static/images/chesecake.jpg"},
        {"name": "Paneer Butter Masala Curry", "price": 230, "image_url": "/static/images/paneer_butter_masala.jpg"},
        {"name": "Momo's", "price": 130, "image_url": "/static/images/momos.jpg"}
    ]
    return render_template("veg.html",items=vegitems,name=user2)

@app.route("/nonveg")
def nonvegetarian_menu():
    user1=request.args.get('username')
    nonvegitems = [
        {"name": "Chicken Dum Biryani", "price": 180, "image_url": "/static/images/Hyderbad_chicken_biriyani.jpg"},
        {"name": "Chicken Noodles", "price": 90, "image_url": "/static/images/chicken_noodles.jpg"},
        {"name": "Chicken Fried Rice", "price": 120, "image_url": "/static/images/chicken_friedrice.jpg"},
        {"name": "Mutton Curry", "price": 350, "image_url": "/static/images/mutton_curry.jpg"},
        {"name": "Shawarma", "price": 100, "image_url": "/static/images/shawarma.jpg"},
        {"name": "Japanese Ramen", "price": 250, "image_url": "/static/images/japanese_ramen.jpg"},
        {"name": "Mutton Paya Soup", "price": 350, "image_url": "/static/images/mutton_payasoup.jpg"},
        {"name": "Thandoori", "price": 450, "image_url": "/static/images/thandoori.jpg"},
        {"name": "Chicken Wings", "price": 220, "image_url": "/static/images/chickenwings.jpg"},
        {"name": "Chicken Nuggets", "price": 230, "image_url": "/static/images/chicken_nuggets.jpg"}

    ]
    return render_template("nonveg.html",name=user1,items=nonvegitems)
@app.route("/drinks_and_icecreams")
def drinksandicecreams():
    user1 = request.args.get('username')
    drinksandicecreams = [
        {"name": "Chocolate Icecream", "price": 45, "image_url": "/static/drinksandicecreams/chocolate_icecream.jpg"},
        {"name": "Pepper Drink", "price": 35, "image_url": "/static/drinksandicecreams/pepper_drink.jpg"},
        {"name": "Icecream Biscuit", "price": 40, "image_url": "/static/drinksandicecreams/icecream_biscuit.jpg"},
        {"name": "Lemonade", "price": 30, "image_url": "/static/drinksandicecreams/lemonade.jpg"},
        {"name": "Cup Icecream", "price": 50, "image_url": "/static/drinksandicecreams/cupicecream.jpg"},
        {"name": "Mirinda", "price": 20, "image_url": "/static/drinksandicecreams/mirinda.jpg"},
        {"name": "Wostok", "price": 60, "image_url": "/static/drinksandicecreams/wostok.jpg"},
        {"name": "Special Lemonade", "price": 60, "image_url": "/static/drinksandicecreams/special_lemonade.jpg"},
        {"name": "Grape Juice", "price": 70, "image_url": "/static/drinksandicecreams/grapejuice.jpg"},
        {"name": "Strawberry With Vanilla", "price": 90, "image_url": "/static/drinksandicecreams/strawberry_with_vanilla.jpg"},
        {"name": "Strawberry Icecream", "price": 80, "image_url": "/static/drinksandicecreams/strawberry_icecream.jpg"},
        {"name": "Pepsi", "price": 30, "image_url": "/static/drinksandicecreams/pepsi.jpg"},
        {"name": "Rose Lemonade", "price": 50, "image_url": "/static/drinksandicecreams/rose_lemonade.jpg"},
        {"name": "Chocobar", "price": 70, "image_url": "/static/drinksandicecreams/chocobar.jpg"},
        {"name": "Choco Vanilla Combo Icecream", "price": 90, "image_url": "/static/drinksandicecreams/choco_vanilla_combo_icecream.jpg"},
        {"name": "Cococola", "price": 30, "image_url": "/static/drinksandicecreams/cococola.jpg"},
        {"name": "FrostyFeast", "price": 75, "image_url": "/static/drinksandicecreams/frostyfeast.jpg"},
        {"name": "Special Banana Icecream", "price": 60, "image_url": "/static/drinksandicecreams/special_banana_icecream.jpg"},
        {"name": "Vanilla Icecream", "price": 40, "image_url": "/static/drinksandicecreams/vanilla_icecream.jpg"},
        {"name": "Sugar Rush Icecream", "price": 35, "image_url": "/static/drinksandicecreams/sugar_rush_icecream.jpg"},
        {"name": "Icyisland Icecream", "price": 90, "image_url": "/static/drinksandicecreams/icyisland_icecream.jpg"},
    ]
    return render_template("drinksandicreams.html", name=user1, items=drinksandicecreams)
@app.route("/cartpage", methods=["GET"])
def cartpage():
    username = request.args.get('username')
    print(username)
    if not username:
        return "Username is required", 400

    conn = None
    cursor = None
    try:
        conn = pymysql.connect(**db)
        cursor = conn.cursor()

        # Check if user has any items in the cart
        cursor.execute("SELECT * FROM cart WHERE username = %s", (username,))
        rows = cursor.fetchall()

        # If cart is empty, redirect to nocart.html
        if not rows:
            return render_template("Ecart.html", name=username)

        # Calculate total
        grand_total = sum(float(row[4]) for row in rows)  # Assuming price is in column index 4
        amount_in_paise = int(grand_total * 100)

        # Create Razorpay order
        order = client.order.create({
            'amount': amount_in_paise,
            'currency': 'INR',
            'payment_capture': '1'
        })

        return render_template("cart.html",
                             data=rows,
                             grand_total=grand_total,
                             order=order,
                             name=username)

    except Exception as e:
        app.logger.error(f"Error occurred in cartpage: {str(e)}")
        # Return nocart.html on error as well
        return "<h1>ERROR</h1>"
    finally:
        if cursor:
            cursor.close()
        if conn and conn.open:
            conn.close()



@app.route("/orders", methods=["GET"])
def orders():
    try:
        # Fetch the username from query parameters
        username = request.args.get('username')
        if not username:
            return "<h1>User NOt Found</h1>"

        print(f"Fetching orders for user: {username}")

        # Establish database connection
        conn = None
        try:
            conn = pymysql.connect(**db)
            cursor = conn.cursor()

            # First check if the table exists
            cursor.execute("SHOW TABLES LIKE %s", (f"orders",))
            if not cursor.fetchone():
                return render_template("noorder.html", name=username)

            # Fetch orders with explicit column selection
            cursor.execute(f"""
                SELECT username, fooditem, quantity, price, total_price, dat_time
                FROM orders
                where username=%s
                ORDER BY dat_time DESC
            """,(username,))
            rows = cursor.fetchall()
            print(f"Orders fetched for user {username}: {rows}")

            if not rows:
                return render_template("noorder.html", name=username)

            # Group orders by day and calculate daily totals
            grouped_orders = {}
            daily_totals = {}

            for row in rows:
                try:
                    order_datetime = row[5]  # dat_time is at index 5
                    if order_datetime:
                        date_str = order_datetime.strftime("%A, %B %d, %Y")
                        if date_str not in grouped_orders:
                            grouped_orders[date_str] = []
                            daily_totals[date_str] = 0.0
                        grouped_orders[date_str].append(row)
                        daily_totals[date_str] += float(row[4])  # total_price is at index 4
                except (IndexError, ValueError, AttributeError) as e:
                    print(f"Error processing row {row}: {str(e)}")
                    continue

            return render_template("order.html",
                                grouped_orders=grouped_orders,
                                daily_totals=daily_totals,
                                name=username)

        except pymysql.MySQLError as e:
            print(f"Database error: {e}")
            return render_template("error.html",
                                message="Database error occurred. Please try again later.",
                                status_code=500), 500

    except Exception as e:
        print(f"Unexpected error: {e}")
        return render_template("error.html",
                            message="An unexpected error occurred. Please try again.",
                            status_code=500), 500

    finally:
        if conn and conn.open:
            conn.close()



@app.route("/totalorders", methods=["GET"])
def all_orders():
    try:
        # Establish database connection
        conn = pymysql.connect(**db)
        cursor = conn.cursor()

        # First check if the table exists
        cursor.execute("SHOW TABLES LIKE 'orders'")
        if not cursor.fetchone():
            return render_template("noorder.html", message="No orders table exists")

        # Fetch all orders with explicit column selection
        cursor.execute("""
            SELECT username, fooditem, quantity, price, total_price, dat_time
            FROM orders
            ORDER BY dat_time DESC
        """)
        rows = cursor.fetchall()

        if not rows:
            return render_template("noorder.html", message="No orders found in system")

        # Group orders by day and calculate daily totals
        grouped_orders = {}
        daily_totals = {}
        grand_total = 0.0

        for row in rows:
            try:
                order_datetime = row[5]  # dat_time is at index 5
                if order_datetime:
                    date_str = order_datetime.strftime("%A, %B %d, %Y")
                    if date_str not in grouped_orders:
                        grouped_orders[date_str] = []
                        daily_totals[date_str] = 0.0
                    grouped_orders[date_str].append(row)
                    daily_totals[date_str] += float(row[4])  # total_price is at index 4
                    grand_total += float(row[4])
            except (IndexError, ValueError, AttributeError) as e:
                print(f"Error processing row {row}: {str(e)}")
                continue

        return render_template("all_orders.html",
                            grouped_orders=grouped_orders,
                            daily_totals=daily_totals,
                            grand_total=grand_total)

    except pymysql.MySQLError as e:
        print(f"Database error: {e}")
        return render_template("error.html",
                            message="Database error occurred. Please try again later.",
                            status_code=500), 500

    except Exception as e:
        print(f"Unexpected error: {e}")
        return render_template("error.html",
                            message="An unexpected error occurred. Please try again.",
                            status_code=500), 500

    finally:
        if 'conn' in locals() and conn.open:
            conn.close()

          

@app.route('/customers')
def customers():
    try:
        # Connect to the database
        conn = pymysql.connect(**db)
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        
        # Fetch all registered customers
        cursor.execute("""
            SELECT name, username, email, mobile, 
                   dateAndTime as registered_date 
            FROM registers
            ORDER BY dateAndTime DESC
        """)
        customers = cursor.fetchall()
        
        # Close connection
        cursor.close()
        conn.close()
        
        return render_template('customers.html', customers=customers)
        
    except Exception as e:
        print(f"Error fetching customers: {str(e)}")
        print('An error occurred while fetching customer data', 'error')
        return render_template('customers.html', customers=[])









@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    if request.method == "POST":
        try:
            user1 = request.args.get('username')
            fooditem = request.form.get("fooditem")
            quantity = request.form.get("quantity")
            price = request.form.get("price")

            if not user1 or not fooditem or not quantity or not price:
                raise ValueError("Missing required input data.")

            totalprice = str(int(price) * int(quantity))

            conn = pymysql.connect(**db)
            cursor = conn.cursor()
            q1 = "SELECT * FROM cart WHERE username = %s AND fooditem = %s"
            cursor.execute(q1, (user1, fooditem))
            row = cursor.fetchone()

            if row:
                update_quantity = str(int(row[2]) + int(quantity))
                updated_total_price = str(int(row[4]) + int(totalprice))
                print(update_quantity, updated_total_price)
                q2 = "UPDATE cart SET quantity = %s, total_price = %s WHERE fooditem = %s AND username = %s"
                cursor.execute(q2, (update_quantity, updated_total_price, fooditem, user1))
            else:
                q = "INSERT INTO cart (username, fooditem, quantity, price, total_price) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(q, (user1, fooditem, quantity, price, totalprice))

            conn.commit()
            return jsonify(success=True)
        except pymysql.MySQLError as db_error:
            return jsonify(success=False, error=f"Database error occurred: {str(db_error)}"), 500
        except ValueError as value_error:
            return jsonify(success=False, error=f"Input validation error: {str(value_error)}"), 400
        except Exception as e:
            return jsonify(success=False, error=f"An unexpected error occurred: {str(e)}"), 500
        finally:
            if 'conn' in locals() and conn.open:
                conn.close()
    else:
        return jsonify(success=False, error="Invalid request method"), 405


@app.route("/delete", methods=["POST", "GET"])
def delete():
    conn = None
    cursor = None
    try:
        if request.method == "POST":
            user1 = request.form.get('username')
            fooditem = request.form.get('fooditem')

            if not user1 or not fooditem:
                raise ValueError("Missing required input data.")
            if not user1.isalnum():
                raise ValueError("Invalid username format.")
            conn = pymysql.connect(**db)
            cursor = conn.cursor()

            cursor.execute(
            "DELETE FROM cart WHERE username = %s AND fooditem = %s",
            (user1, fooditem)
        )
            conn.commit()

            return redirect(url_for('cartpage', username=user1))

    except pymysql.MySQLError as e:
        app.logger.error(f"MySQL error occurred: {e}")
        return "Database error occurred. Please try again later.", 500
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return "An unexpected error occurred. Please try again later.", 500
    finally:
        # Ensure resources are properly closed
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route("/success", methods=["POST", "GET"])
def success():
    payment_id = request.form.get("razorpay_payment_id")
    order_id = request.form.get("razorpay_order_id")
    signature = request.form.get("razorpay_signature")

    dict1 = {
        'razorpay_order_id': order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
    }

    try:
        # Verify payment signature
        client.utility.verify_payment_signature(dict1)
        user1 = request.args.get('username')

        if user1 is None:
            return "User Not Found"

        # Connect to the database
        conn = pymysql.connect(**db)
        cursor = conn.cursor()

        # Fetch user's email from the register table
        query_email = "SELECT email FROM registers WHERE username = %s"
        cursor.execute(query_email, (user1,))
        email_result = cursor.fetchone()

        if email_result is None:
            return "Email not found for the user"

        email = email_result[0]

        # Fetch cart details
        query_cart = f"SELECT * FROM cart WHERE username = %s"
        cursor.execute(query_cart, (user1,))
        rows = cursor.fetchall()
        print(rows)

        # Calculate grand total
        grand_total = sum(float(row[4]) for row in rows)

        # Insert cart details into the order table
        current_datetime = datetime.now()
        for row in rows:
            query_order = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s, %s)".format(user1)
            cursor.execute(query_order, (row[0], row[1], row[2], row[3], row[4], current_datetime))

        # Clear the cart after successful payment
        query_truncate_cart = f"DELETE FROM CART WHERE username=%s"
        cursor.execute(query_truncate_cart,(user1,))

        conn.commit()
        conn.close()

        # Generate HTML table for email
        table_rows = "".join(
            f"""
            <tr>
                <td>{row[1]}</td>
                <td>₹{row[3]}</td>
                <td>{row[2]}</td>
                <td>₹{row[4]}</td>
            </tr>
            """ for row in rows
        )

        # HTML email content with enhanced styling and animations
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

                body {{
                    font-family: 'Poppins', sans-serif;
                    background: #f5f7fa;
                    margin: 0;
                    padding: 0;
                    color: #333;
                    line-height: 1.6;
                }}
                .email-container {{
                    max-width: 600px;
                    margin: 20px auto;
                    background: white;
                    border-radius: 10px;
                    overflow: hidden;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                }}
                .header {{
                    background: linear-gradient(135deg, #98D8AA, #5A7BB0);
                    padding: 30px;
                    text-align: center;
                    color: white;
                }}
                .header h1 {{
                    margin: 0;
                    font-size: 28px;
                    font-weight: 700;
                }}
                .content {{
                    padding: 30px;
                }}
                .greeting {{
                    margin-bottom: 20px;
                }}
                .order-table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin: 25px 0;
                    animation: fadeIn 0.8s ease-out;
                }}
                .order-table th {{
                    background: #5A7BB0;
                    color: white;
                    padding: 12px 15px;
                    text-align: left;
                    font-weight: 500;
                }}
                .order-table td {{
                    padding: 12px 15px;
                    border-bottom: 1px solid #eaeaea;
                }}
                .order-table tr:hover {{
                    background-color: rgba(152, 216, 170, 0.1);
                }}
                .total-row {{
                    font-weight: 600;
                    background-color: #f8f9fa;
                }}
                .total-row td {{
                    border-top: 2px solid #5A7BB0;
                }}
                .order-info {{
                    background: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin: 25px 0;
                    border-left: 4px solid #5A7BB0;
                }}
                .thank-you {{
                    text-align: center;
                    margin: 25px 0;
                    color: #5A7BB0;
                    font-size: 20px;
                    font-weight: 600;
                }}
                .footer {{
                    text-align: center;
                    padding: 20px;
                    background: #f8f9fa;
                    color: #666;
                    font-size: 14px;
                }}
                .track-btn {{
                    display: inline-block;
                    background: linear-gradient(135deg, #98D8AA, #5A7BB0);
                    color: white;
                    padding: 12px 25px;
                    text-decoration: none;
                    border-radius: 4px;
                    font-weight: 500;
                    margin: 15px 0;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; transform: translateY(10px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                @media (max-width: 600px) {{
                    .content {{
                        padding: 20px;
                    }}
                    .header {{
                        padding: 25px 20px;
                    }}
                }}
            </style>
        </head>
        <body>
            <div class="email-container">
                <div class="header">
                    <h1>Order Confirmation</h1>
                    <p>Your payment was successful!</p>
                </div>

                <div class="content">
                    <div class="greeting">
                        <p>Dear {user1},</p>
                        <p>Thank you for shopping with Saha Foods! Here are your order details:</p>
                    </div>

                    <table class="order-table">
                        <thead>
                            <tr>
                                <th>Item</th>
                                <th>Price</th>
                                <th>Qty</th>
                                <th>Subtotal</th>
                            </tr>
                        </thead>
                        <tbody>
                            {table_rows}
                            <tr class="total-row">
                                <td colspan="3"><strong>Grand Total</strong></td>
                                <td><strong>₹{grand_total:.2f}</strong></td>
                            </tr>
                        </tbody>
                    </table>

                    <div class="order-info">
                        <p><strong>Order ID:</strong> {order_id}</p>
                        <p><strong>Payment ID:</strong> {payment_id}</p>
                        <p><strong>Date:</strong> {current_datetime.strftime('%d %b %Y, %I:%M %p')}</p>
                    </div>

                    <div style="text-align: center;">
                        <a href="https://www.sahafoods.com/track-order?order_id={order_id}" class="track-btn">
                            Track Your Order
                        </a>
                    </div>

                    <div class="thank-you">
                        <p>Thank you for your order!</p>
                    </div>
                </div>

                <div class="footer">
                    <p><strong>Saha Foods</strong></p>
                    <p>123 Food Street, Bangalore, India</p>
                    <p>© {datetime.now().year} Saha Foods. All rights reserved.</p>
                </div>
            </div>
        </body>
        </html>
        """

        # Create and send email
        msg = MIMEMultipart('alternative')
        msg['From'] = "Saha Foods <>"
        msg['To'] = email
        msg['Subject'] = f'Your Saha Foods Order #{order_id[:8]} - Confirmed'

        # Attach HTML content
        msg.attach(MIMEText(html, 'html'))

        # Send the email with error handling
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login('', '')
                server.send_message(msg)
            print(f"Order confirmation email sent to {email}")
        except Exception as email_error:
            print(f"Failed to send email to {email}: {str(email_error)}")
            # Continue with the order even if email fails

    except Exception as e:
        print(f"Error processing order for {user1}: {str(e)}")
        return render_template("failure.html", name=user1)
    else:
        return render_template("success.html", name=user1)
    






if __name__ == "__main__":
    app.run()





