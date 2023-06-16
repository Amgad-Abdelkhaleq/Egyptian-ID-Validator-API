# Egyptian-ID-Validator-API
Egyptian National ID Validator and Data-Extractor API
This is a Flask-based API that validates and extracts information from Egyptian national IDs.

### How to Run the Application
To run the application, follow these steps:

1- Clone the git repository to your local machine

2- Navigate to the project directory

3- Install the required dependencies:
```pip install flask ```

4- Start the Flask development server:
```python app.py ```

The API should now be running on http://localhost:5000/validate_id.

API Schema
The API has a single endpoint at /validate_id, which accepts a POST request containing a national_id parameter. The endpoint returns a JSON response containing the validation result (valid) and any extracted information (info).

Example request

```bash http
POST /validate_id HTTP/1.1
Host: localhost:5000
Content-Type: application/x-www-form-urlencoded

national_id=29001011234567
```

Example response

```bash http
HTTP/1.1 200 OK
Content-Type: application/json

{
'valid': True,
 'info': {'birth_year': 1990,
  'birth_month': 1,
  'birth_day': 1,
  'gender': 'Female',
  'governorate': 'Dakahlia'}
}
```
### Implementation Notes

The implementation of the API consists of two main functions: validate_national_id and extract_info. The validate_national_id function checks the validity of the national ID by performing several checks on its format and content. The extract_info function extracts relevant information from the national ID, such as the birth year, month, day, gender, and governorate.
