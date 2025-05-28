from flask import Flask, request, jsonify
import mysql.connector
import random
import smtplib
from email.mime.text import MIMEText
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enables API testing via Postman or frontend

# Configure MySQL connection
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_password',
    database='your_db_name'
)
cur = con.cursor()

# Email credentials
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_app_password'

otp_storage = {}

# ✅ Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    required_fields = ['name', 'username', 'email', 'mobile', 'password', 'confirm_password']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    if data['password'] != data['confirm_password']:
        return jsonify({'error': 'Passwords do not match'}), 400

    otp = str(random.randint(100000, 999999))
    otp_storage[data['email']] = {
        'otp': otp,
        'user_data': data
    }

    try:
        msg = MIMEText(f'Your OTP for registration is {otp}')
        msg['Subject'] = 'OTP Verification'
        msg['From'] = SENDER_EMAIL
        msg['To'] = data['email']

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        return jsonify({'message': 'OTP sent to your email'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ OTP verification route
@app.route('/verifyemail', methods=['POST'])
def verify_email():
    data = request.get_json()
    email = data.get('email')
    otp = data.get('otp')

    if email in otp_storage and otp_storage[email]['otp'] == otp:
        user_data = otp_storage[email]['user_data']
        try:
            cur.execute("INSERT INTO users (name, username, email, mobile, password) VALUES (%s, %s, %s, %s, %s)",
                        (user_data['name'], user_data['username'], user_data['email'],
                         user_data['mobile'], user_data['password']))
            con.commit()
            del otp_storage[email]
            return jsonify({'message': 'User registered successfully'}), 201
        except mysql.connector.Error as err:
            return jsonify({'error': str(err)}), 500
    else:
        return jsonify({'error': 'Invalid or expired OTP'}), 400

# ✅ User login
@app.route('/userlogin', methods=['POST'])
def user_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    if user:
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401

# ✅ Admin login
@app.route('/adminlogin', methods=['POST'])
def admin_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cur.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
    admin = cur.fetchone()
    if admin:
        return jsonify({'message': 'Admin login successful'}), 200
    else:
        return jsonify({'error': 'Invalid admin credentials'}), 401

# ✅ Forgot password
@app.route('/forgotpassword', methods=['POST'])
def forgot_password():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    if new_password != confirm_password:
        return jsonify({'error': 'Passwords do not match'}), 400

    cur.execute("SELECT * FROM users WHERE username = %s AND email = %s", (username, email))
    user = cur.fetchone()
    if user:
        cur.execute("UPDATE users SET password = %s WHERE username = %s AND email = %s",
                    (new_password, username, email))
        con.commit()
        return jsonify({'message': 'Password updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

# ✅ Root
@app.route('/')
def home():
    return jsonify({'message': 'Flask JSON API running'}), 200

if __name__ == '__main__':
    app.run(debug=True)
