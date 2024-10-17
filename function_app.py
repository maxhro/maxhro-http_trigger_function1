
# Import the necessary Azure Functions SDK.
import azure.functions as func
# Import the logging module to enable logging of messages to track events and errors.
import logging

# Create an instance of the FunctionApp class, with the authentication level set to ANONYMOUS.
# This means that the function can be accessed without requiring authorization.
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Define an HTTP-triggered function with a specified route.
# This function will be triggered when an HTTP request is made to the route "http_trigger_function1".
@app.route(route="http_trigger_function1")
def http_trigger_function1(req: func.HttpRequest) -> func.HttpResponse:
    """
    An HTTP-triggered function that processes incoming requests to greet a user by name.

    Args:
        req (func.HttpRequest): The HTTP request object that contains query parameters
        and the request body.

    Returns:
        func.HttpResponse: An HTTP response object that contains greeting or an error message.
    """
    
    # Log an informational message indicating that the function has processed an HTTP request.
    logging.info('Python HTTP trigger function processed a request.')

    # Retrieve the 'name' parameter from the query string of the HTTP request.
    name = req.params.get('name')

    # Check if the 'name' parameter was not provided in the query string.
    if not name:
        # If 'name' isn't found in the query string, attempt to read the request body as JSON.
        try:
            req_body = req.get_json()
        except ValueError:
            # If the JSON is invalid, do nothing and simply fall through to the next checks.
            pass
        else:
            # If the JSON is valid, extract the 'name' value from the request body.
            name = req_body.get('name')

    # Check if a 'name' was provided either in query string or request body.
    if name:
        # If 'name' is found, return a personalized greeting as the HTTP response.
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        # If no 'name' is provided, return a generic response indicating that a name is required.
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200  # Return HTTP status code 200 (OK) for successful execution.
        )
    # test case 