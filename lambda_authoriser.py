# DemoAuthorizer

def lambda_handler(event, context):
    
    #1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    
    #2 - See if the person's token is valid
    if event['authorizationToken'] == 'abc123':
        auth_status = 'Allow'
    else:
        auth_status = 'Deny'
    
    #3 - Construct and return the response
    authResponse = {
        'policyDocument': {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Action': 'execute-api:Invoke',
                'Resource': [
                    'arn:aws:execute-api:us-east-1:AccountNumber:API ID/books/*/*'
                ],
                'Effect': auth_status
            }
        ]
    }
    }
    return authResponse
