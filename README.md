# aws-api-gateway-rest-api

This repository consists of lambda function code in python 3.8 that enables you to handle api requests from api gateway. It also includes json swagger documentation of a basic CRUD API along with the iam policy to be attached with the lambda. 

## Things to do

1. Add two environment variables to the lambda function.
    1. DYNAMODB_TABLE - DynamoDB table name
    2. HASH_KEY - DynamoDB hash key name
2. Add a new role with the policy (use the contents of the lambda-policy.json) and attach it as the execution role of the lambda. Replace the <accountId> with actual account id, <bucketName> with actual s3 bucket name and <tableName> with actual DynamoDB table name within the file.
3. The zip file Archive.zip contains the lambda function along with the dependant python 3.8 packages which can be uploaded to the lambda function code. If you are using a different python version, please use the corresponding packages.
# aws-api-gateway-rest-api-
API GW + Lambda + Dynamo DB
**
lambda_function.py**

Python script designed to handle operations on a DynamoDB table representing books. It seems to be structured for use in an AWS Lambda function, which can be invoked by an API Gateway for handling HTTP requests.

Here's a breakdown of the main components:

Class Definition (books):

The class is initialized with the DynamoDB table name (table) and the hash key (hash_key).
It includes various methods for handling CRUD operations on the DynamoDB table.
Private Methods (_get_dynamodb_table, _get_dynamodb_key, _problem, _json_serial, _exists):

_get_dynamodb_table: Returns a reference to the DynamoDB table.
_get_dynamodb_key: Constructs and returns the DynamoDB key for a given hash key value.
_problem: Logs errors, constructs an error response, and returns it.
_json_serial: Serializes Decimal types to int. Used in JSON serialization.
_exists: Checks if an item with a given hash key exists in the DynamoDB table.
Public Methods (list_books, get_book, post_book, put_book, delete_book):

list_books: Retrieves a list of books based on query parameters.
get_book: Retrieves details of a specific book based on the hash key.
post_book: Adds a new book to the DynamoDB table.
put_book: Updates an existing book in the DynamoDB table.
delete_book: Deletes a book from the DynamoDB table.
Lambda Handler (lambda_handler):

Handles Lambda function invocation.
Retrieves environment variables for DynamoDB table name (DYNAMODB_TABLE) and hash key (HASH_KEY).
Determines the operation to perform based on the request context's operation name.
Invokes the corresponding method from the books class and returns the result.
Usage of Boto3:

Boto3, the AWS SDK for Python, is used for interacting with DynamoDB.
The boto3.resource method is used to get a reference to the DynamoDB table.
Request Processing:

The Lambda function processes incoming events (presumably from an API Gateway).
The method to execute is determined based on the operation specified in the request context.
It's important to note that the script assumes certain conventions, such as the existence of specific environment variables and the structure of incoming events. Also, the code doesn't include proper error handling in some cases, and you might want to enhance it based on your specific requirements and error scenarios. Additionally, the use of json.dumps for serialization in several places could be improved using a more centralized approach.





