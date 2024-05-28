from decimal import Decimal
import json
import boto3

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Std_table')

def retrieve_student_details(registration_number):
    response = table.get_item(
        Key={
            'registration_number': registration_number
        }
    )
    student_details = response.get("Item", {})
   
    # Convert Decimal types to standard Python types
    for key, value in student_details.items():
        if isinstance(value, Decimal):
            student_details[key] = float(value)  
    
    if student_details:
        return student_details
    else:
        return None
        
# Function to add student details to DynamoDB
def add_student_details(name, year, course, registration_number):
    table.put_item(
        Item={
            'registration_number': registration_number,
            'name': name,
            'year': year,
            'course': course
        }
    )

# Helper function to build Lex response
def build_lex_response(intent_name, message_content):
    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name,
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": message_content
            }
        ]
    }
    
# Lambda function handler
 def lambda_handler(event, context):
    try:
        # Extract intent name
        intent_name = event['sessionState']['intent']['name']
        
        # Check intent name
        if intent_name == 'RetrieveStudentDetails':
            # Extract registration number from slots
            registration_number = event['sessionState']['intent']['slots']['registration_number']['value']['interpretedValue']
            
            # Retrieve student details from DynamoDB
            student_details = retrieve_student_details(registration_number)
            
            if student_details:
                message_content = f"Student details: {json.dumps(student_details)}"
            else:
                message_content = "Student with registration number not found"
            
            return build_lex_response(intent_name, message_content)
        
        elif intent_name == 'AddStudentDetails':
            # Extract slot values
            slots = event['sessionState']['intent']['slots']
            name = slots['name']['value']['interpretedValue']
            year = slots['year']['value']['interpretedValue']
            course = slots['course']['value']['interpretedValue']
            registration_number = slots['registration_number']['value']['interpretedValue']
            
            # Add student details to DynamoDB
            add_student_details(name, year, course, registration_number)
            
            # Return response
            message_content = "Student details added successfully"
            return build_lex_response(intent_name, message_content)
        
        else:
            # Unknown intent
            message_content = "Unknown intent"
            return build_lex_response(intent_name, message_content)
    
    except Exception as e:
        # Error handling
        print('Error handling intent:', e)
        return build_lex_response("RetrieveStudentDetails", "Error handling intent")
    
    


