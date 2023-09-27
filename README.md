# API README

This is a simple API to hash passwords using the bcrypt algorithm and check their security level. It utilizes the FastAPI framework and Passlib for password hashing.

## How to Install and Run the API

1. Clone the repository from GitHub: `git clone https://github.com/your/repository.git`
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Run the API server: `uvicorn main:app --reload`

## API Endpoints

### Hash Password [/hash/]

This endpoint allows you to hash a password and check its security level.

#### Request

- Method: POST
- URL: `http://localhost:8000/hash/`
- Body:
  ```json
  {
    "password": "your_password"
  }
  ```

#### Response

- Status Code: 200
- Body:
  ```json
  {
    "hashed_password": "your_hashed_password",
    "security": "security_level"
  }
  ```

#### Possible Security Levels

- `unsafe`: Password is considered unsafe and doesn't meet the minimum requirements.
- `moderately safe`: Password meets some security requirements but can be improved.
- `secure password`: Password meets all security requirements and is considered secure.

#### Possible Errors

- Status Code: 400
  - Detail: `"Password too short"` - The provided password is too short (less than 8 characters).
  - Detail: `"Password is not secure"` - The provided password doesn't meet the security requirements.

## Security Verification

The security level of a password is calculated based on the following criteria:

- At least one uppercase letter
- At least one lowercase letter
- At least one digit

Each criterion met increases the security level by one. A password with only one criterion met is considered unsafe, with two criteria met is moderately safe, and with all three criteria met is a secure password.

## Tech Stack

- FastAPI - Web framework for building APIs
- Passlib - Password hashing library
- Pydantic - Data validation and parsing library

## Contribution Guidelines

Please feel free to contribute to this project by opening a pull request. Make sure to follow the best practices and conventions outlined in the repository.