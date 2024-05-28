Serverless Student Management System




This project is a serverless application that allows managing student details using AWS Lambda, DynamoDB, and Amazon Lex. Users can interact with the application via a chatbot interface provided by Amazon Lex.

Features
CRUD Operations: Create, Read, Update, Delete student details.
Amazon Lex Integration: Natural language processing to handle user inputs.
AWS Lambda: Serverless functions to process requests.
DynamoDB: NoSQL database for storing student details.

Prerequisites
Before you start, make sure you have the following:

An AWS account
AWS CLI configured with appropriate permissions
Node.js and npm installed
Python and boto3 library installed
AWS SDK for Python (boto3)
IAM role with permissions to access DynamoDB, Lambda, and Lex
Step-by-Step Procedure
1. Set Up DynamoDB Table
Go to the AWS Management Console.
Navigate to DynamoDB.
Create a new table named ManageMent_Student with registrationNumber as the primary key.
2. Create IAM Role
Go to the IAM service in the AWS Management Console.
Create a new role for Lambda.
Attach the following policies:
AmazonDynamoDBFullAccess
AWSLambdaBasicExecutionRole
AmazonLexFullAccess
3. Develop Lambda Functions
Create a file named lambda_function.py and paste the code given

### 4. Deploy Lambda Function

1. Go to the AWS Lambda service in the AWS Management Console.
2. Create a new function.
3. Choose the runtime as Python 3.x.
4. Attach the IAM role created in Step 2.
5. Copy and paste the `lambda_function.py` code into the function code editor.
6. Deploy the function.

### 5. Create Amazon Lex Bot

1. Go to the Amazon Lex service in the AWS Management Console.
2. Create a new bot.
3. Add an intent named `RetrieveStudentDetails`:
   - Add slots: `registrationNumber`.
   - Configure the Lambda function to be triggered on fulfillment.
4. Add another intent named `AddStudentDetails`:
   - Add slots: `name`, `year`, `course`, `registrationNumber`.
   - Configure the Lambda function to be triggered on fulfillment.
5. Build and test the bot.

### 6. Test the Application

1. Go to the Lex console and open the test window.
2. Interact with the bot using phrases like:
   - "Add student details: name John Doe, year 2, course Computer Science, registration number 12345."
   - "Retrieve student details for registration number 12345."
3. Ensure the responses are accurate and reflect the changes in the DynamoDB table.

### 7. Add Resource-Based Policy for DynamoDB Table

Create a resource-based policy to allow your Lambda function to access the DynamoDB table. Here is an example policy:

json:-
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::841120952735:role/service-role/DataBase_Student-role-ji2lcecr"
            },
            "Action": "dynamodb:*",
            "Resource": "arn:aws:dynamodb:ap-southeast-2:841120952735:table/ManageMent_Student"
        }
    ]
}
8. Conclusion
This project demonstrates how to build a serverless student management system using AWS Lambda, DynamoDB, and Amazon Lex. It showcases the integration of a conversational interface with a backend service to provide a seamless user experience.
