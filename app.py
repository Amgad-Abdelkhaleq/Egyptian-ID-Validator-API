from flask import Flask, request, jsonify

app = Flask(__name__)
governorates_codes={
        1: 'Cairo',
        2: 'Alexandria',
        3: 'Port Said',
        4: 'Suez',
        11: 'Damietta',
        12: 'Dakahlia',
        13: 'Ash Sharqia',
        14: 'Kaliobeya',
        15: 'Kafr El - Sheikh',
        16: 'Gharbia',
        17: 'Monoufia',
        18: 'El Beheira',
        19: 'Ismailia',
        21: 'Giza',
        22: 'Beni Suef',
        23: 'Fayoum',
        24: 'El Menia',
        25: 'Assiut',
        26: 'Sohag',
        27: 'Qena',
        28: 'Aswan',
        29: 'Luxor',
        31: 'Red Sea',
        32: 'New Valley',
        33: 'Matrouh',
        34: 'North Sinai',
        35: 'South Sinai',
        88: 'Foreign'
    }

@app.route('/validate_id', methods=['POST'])
def validate_id():
    national_id = request.args.get('national_id')
    if validate_national_id(national_id):
        info = extract_info(national_id)
        return jsonify({'valid': True, 'info': info})
    else:
        return jsonify({'valid': False})



def validate_national_id(national_id):
    # Check that the national ID is 14 digits long
    if len(national_id) != 14:
        print('length is not valid')
        return False
    
    # Check that the birth year is valid (between 1900 and the current year - 15 "legal age to apply for an ID")
    birth_year = int(national_id[1:3])
    current_year = datetime.datetime.now().year
    if birth_year < 0 or birth_year > (current_year - 1900 - 15):
        print('birth year is not valid')
        return False
    
    # Check that the birth month is valid (between 1 and 12)
    birth_month = int(national_id[3:5])
    if birth_month < 1 or birth_month > 12:
        print('birth month is not valid')  
        return False
    
    # Check that the birth day is valid (between 1 and 31)
    birth_day = int(national_id[5:7])
    if birth_day < 1 or birth_day > 31:
        print('birthday is not valid')
        return False
    
    # Check that the governorate code is valid
    governorate_code = int(national_id[7:9])
    if governorate_code not in governorates_codes.keys():
        print("governorate_code is not valid")
        return False
    
    # If all checks pass, return True
    return True

def extract_info(national_id):
    # Extract the birth year, month, and day from the national ID
    century_code=int(national_id[0])
    birth_year = int(national_id[1:3])
    birth_month = int(national_id[3:5])
    birth_day = int(national_id[5:7])
    gender_code=int(national_id[12])
    
    # Determine the birth century based on the birth year
    birth_century = 19 if century_code == 2 else 20
    
    # Determine the gender
    gender = 'Female' if gender_code % 2 == 0 else 'Male' 
    
    # Determine the governorate based on the governorate code
    governorate_code = int(national_id[7:9])
    governorate = governorates_codes.get(governorate_code, 'Unknown')
    
    
    # Return a dictionary containing the extracted information
    return {
        'birth_year': birth_century * 100 + birth_year,
        'birth_month': birth_month,
        'birth_day': birth_day,
        'gender': gender,
        'governorate': governorate
    }

if __name__ == '__main__':
    app.run(debug=True)
