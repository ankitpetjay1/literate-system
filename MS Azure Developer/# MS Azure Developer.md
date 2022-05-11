# MS Azure Developer

## **Is serverless computing right choice**

<br>

**What is serverless computing?**

Function as a Service or FaaS.

Microservice hosted on a cloud platform.

If your business logic runs as functions and you do not provision servers or scale infrastructure.

Cloud provider manages infrastructure.
courercc

> App is automatically scaled out or down depending on load.

Common approaches are:

- Logic Apps
- Azure Functions

<br>

**Azure Functions:**
Azure Functions is the serverless application paltform.

- With Azure functions in Azure, you are charged only when service runs.
- Code can be written in C#, F#, JS, Python and PowerShell.
- Support for Packet Managers like NuGet and NPM.
- Auto Scaling
  - Allows only 1 function app instance every 10 seconds for up to 200 instances.
    > Each instance can service multiple concurrent executions.
  - Different triggers have different scaling requirements.
- Functions are event driven and run only in response to an event called trigger.
  > Trigger can be an HTTP request or a message being added to a queue.
- Can be deployed in a non serverless environment should the needs change.
- Limits:
  - Functions have a timeout of 5 mins, up to 10 mins
  - For more than 10 minutes, host it on a VM.
  - Service initiated through HTTP request have 2.5 min limit.
  - Durable functions allows orchestrate of multiple functions without any time out.
- If functions need to be executed continuously by multiple clients, the cost of using functions can get really high. It might then be cheaper to host service on a VM.

<br>

_**Exercise Links**_

[Create a function app using JavaScript](https://docs.microsoft.com/en-us/learn/modules/create-serverless-logic-with-azure-functions/3-create-an-azure-functions-app-in-the-azure-portal?pivots=javascript)  
[Create a function app using PowerShell](https://docs.microsoft.com/en-us/learn/modules/create-serverless-logic-with-azure-functions/3-create-an-azure-functions-app-in-the-azure-portal?pivots=powershell)

<br>

Choosing Service Plan

- Consumption Plan vs App Service Plan
  > Consumption Plan comes with a configurable timeout period. Default: 25, Max: 10
- Azure App service plan avoids timeout and allows function to run continuously on a VM that you define.
  > This method is not serverless as your resources are managed accordingly to the App Service Plan. Can configure more processing power and longer execution time than serverless.

Storage Requirements

- Function app must be linked to a storage account.
- This is used for internal operations such as logging executions and managing execution triggers.
  > In Consumption plan this will be used to store function code and configuration files.

<br>

### **Creating Function App**

- Function apps are part of Compute in Azure Portal.
- Select relevant Subscription, Resource Group.
- Name must be globally unique and will become part of the function app URL
- Publish will be code
- Select language you want to implement your function in. Version default.
- Region will be closest region to your users.
- Plan will be Consumption (Serverless).

> After the function app is created, you can access the URL to verify the app is ready.

<br>

Triggers

- Functions run in response to an event. We can configure these events as triggers.
- Each function must be configured with exactly one trigger.
- Triggers are supported for following services:
  - _Blob Storage_
  - _Azure Cosmos DB_
  - _Event Grid_
  - _HTTP_
  - _Microsoft Graph Events_
  - _Queue Storage_
  - _Service Bus_
  - _Timer_

<br>

Bindings

- Declarative way to connect data and services to your Function.
- Allows interaction with data sources, which means you don't have to write the code in your function to manage connections.
- Taken care of by the platform as part of binding code.
- Your code reads data from input bindings and writes data to output bindings.
- A function can have zero or more bindings to manage input and output.
- All Azure Bindings: [Supported Bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings#supported-bindings)

<br>

**Configuring a function with I/O binding (trigger)**

We want to write a new row to Azure Table Storage whenever a new message appears in Azure Queue Storage.

We can implement this using _Azure Queue Storage trigger_ and an Azure Table storage _output binding_.

Below is code snippet from _function.json_

```JSON
{
  "bindings": [
    {
      "name": "order",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "myqueue-items",
      "connection": "MY_STORAGE_ACCT_APP_SETTING"
    },
    {
      "name": "$return",
      "type": "table",
      "direction": "out",
      "tableName": "outTable",
      "connection": "MY_TABLE_STORAGE_ACCT_APP_SETTING"
    }
  ]
}
```

Our JSON config specifies:

- Function will be triggered when a message is added to a queue named **myqueue-items**.
- Function then executes and it's return value is written to the **outTable** in Azure Table Storage.

> Function Templates: You can select predefined triggers, development environments, dependencies for your function. You can later customize the code.

<br>

Functions and it's Files

- After you create a function from a template, two files are created:
  - Configuration file _function.json_
  - Source code file _index.js_
- Go to the Functions under Functions category to view the function.
- Select a function and go to Code + Test from the menu.
- The command bar gives several options:
  - Test/Run, allows to build and test the function.
    > You can add input query parameters to execute and view the Output.
  - Switch between files, in the function directory.
  - Get function URL to trigger function using HTTP trigger.
    > Use tools like Postman or cURL, to intiate request to the function endpoint URL.

<br>

### **Monitoring for Application Insights**

Monitor functions during development and in production using Application Insights integration.  
Provides quick way to view history of function operations by displaying timestamp, result code, duration, and operation ID.

- Turn on application insights by going to Settings > Application Insights.
- Turn on App Insights
- Hit Apply and click Yes.

<br>

Logging

The methods of each language in the function can be passed a "logging" object, which can be used to add log information to the Logs pane in the Code + Test pane when running a test.

- In JS, context object is passed to handler:

  ```JavaScript
  context.log('Enter the logging statement here');
  ```

- In C#, log.LogInformation method, the log object is passed:

  ```C#
  log.LogInformation('Enter the logging statement here');
  ```

- In PowerShell, Write-Host cmdlet to write the log:

  ```PowerShell
  Write-Host "Enter your logging statement here"
  ```

<br>

Errors, failures, warnings, and anomalies

You can use _Metrics_ or options in Investigate category to monitoring performance, diagnose failures, or configure predefined workbooks, compilation errors and warnings in the code, usage statistics by role

<br>

### **Adding Logic to Function**

Wetake the example of an escalator gear drive, and add the logic for the temperature service.  
We're going to receive data from an HTTP request.

<br>

**Requirements**

Temperatures from 0 up to 25 degrees should be flagged as OK.
Temperatures above 25 up to 50 degrees should be flagged as CAUTION.
Temperatures above 50 degrees should be flagged as DANGER.

**Add a function**

1. In the Function App menu, under Functions, select Functions. The Functions pane appears. This lists any functions you defined for your function app.
2. In the command bar, select Create. The Create function pane appears.
3. Under Select a template, select HTTP trigger. HttpTrigger1 is created.
   > Function app is a container that groups functions into a logical unit for easier management, deployment, and sharing of resources.
4. In the Developer menu on the left, select Code + Test. The code editor opens, displaying the contents of the index.js code file for your function.
5. The default code goes like:

   ```JavaScript
   module.exports = async function (context, req) {
     context.log('JavaScript HTTP trigger function processed a request.');

     const name = (req.query.name || (req.body && req.body.name));
     const responseMessage = name
         ? "Hello, " + name + ". This HTTP triggered function executed successfully."
         : "This HTTP triggered function executed successfully.";

     context.res = {
         // status: 200, /* Defaults to 200 */
         body: responseMessage
     };
   }
   ```

   - The function responds by returning the message Hello, name. This HTTP triggered function executed successfully.

<br>

6. From the source file dropdown list, select function.json to view the configuration of the function, which should look like the following code.

   ```JavaScript
   {
     "bindings": [
       {
         "authLevel": "function",
         "type": "httpTrigger",
         "direction": "in",
         "name": "req",
         "methods": [
           "get",
           "post"
         ]
       },
       {
         "type": "http",
         "direction": "out",
         "name": "res"
       }
     ]
   }
   ```

   - This configuration file declares that the function runs when it receives an HTTP request. The output binding declares that the response will be sent as an HTTP response.

<br>

7. To test the function, you can send an HTTP request to the function URL using cURL on the command line.

> HTTP triggers let you use API keys to block unknown callers by requiring a key as part of the request. When you create a function, you select the authorization level. By default, it's set to Function, which requires a function-specific API key, but it can also be set to Admin to use a global "master" key, or Anonymous to indicate that no key is required. You can also change the authorization level through the function properties after creation.
>
> We specified Function when we created this function, we need to supply the key when we send the HTTP request.
>
> We can send it as an HTTP header named _x-functions-key_.

8. To find the function and master keys, in the Function App menu, under Developer, select Function Keys. The Function Keys pane for your function opens. Click to show value in the Value. Copy the value to the clipboard.

9. Step back to _Code + Test_ to find the endpoint URL of the function. From the command bar, select Get function URL. Save this link.

10. On the command bar, select Test/Run.

11. In the Body text box, overwrite the embedded code by replacing line 2 in the Body with the cURL command below:

    ```Bash
    curl --header "Content-Type: application/json" --header "x-functions-key: <your-function-key>" --request POST --data "{\"name\": \"Azure Function\"}" <your-https-url>
    ```

    - _Content-Type_ header value of type application/json
    - Passed the Function Key as the header value _x-functions-key_ (Replace with the function key value you saved)
    - Used a _POST_ request.
    - Passed the Azure Function with the URL for your function. (Replace with the URL of the functon that you saved)

    <br>

12. Select Run

    - Under the Output pane, for HTTP response code, the function responds with the text 200 OK.
    - The Code + Test pane should open a session displaying log file output. The log file updates with the status of your request.

    ```
    2022-02-16T22:34:10.473 [Information] Executing 'Functions.HttpTrigger1' (Reason='This function was programmatically called via the host APIs.', Id=4f503b35-b944-455e-ba02-5205f9e8b47a)

    2022-02-16T22:34:10.539 [Information] JavaScript HTTP trigger function processed a request.

    2022-02-16T22:34:10.562 [Information] Executed 'Functions.HttpTrigger1' (Succeeded, Id=4f503b35-b944-455e-ba02-5205f9e8b47a, Duration=114ms)
    ```

**Adding Logic**

Let's replace the default code in our function with the following code, to implement our business logic.  
In the HttpTrigger1 function pane, open the index.js file, and replace it with the following code. Click Save

```JavaScript
module.exports = function (context, req) {
    context.log('Drive Gear Temperature Service triggered');
    if (req.body && req.body.readings) {
        req.body.readings.forEach(function(reading) {

            if(reading.temperature<=25) {
                reading.status = 'OK';
            } else if (reading.temperature<=50) {
                reading.status = 'CAUTION';
            } else {
                reading.status = 'DANGER'
            }
            context.log('Reading is ' + reading.status);
        });

        context.res = {
            // status: 200, /* Defaults to 200 */
            body: {
                "readings": req.body.readings
            }
        };
    }
    else {
        context.res = {
            status: 400,
            body: "Please send an array of readings in the request body"
        };
    }
    context.done();
};
```

Our function is expecting an array of temperature readings. The following JSON snippet is an example of the request body that we'll send to our function. Each reading entry has an ID, timestamp, and temperature.

```JSON
{
    "readings": [
        {
            "driveGearId": 1,
            "timestamp": 1534263995,
            "temperature": 23
        },
        {
            "driveGearId": 3,
            "timestamp": 1534264048,
            "temperature": 45
        },
        {
            "driveGearId": 18,
            "timestamp": 1534264050,
            "temperature": 55
        }
    ]
}
```

We're going to use the Test/Run feature in Developer > Code + Test to test our function.

In the Input tab, replace the contents of the Body text with the above JSON snippet to create our sample request. Select Run.

The output pane results with our HTTP response code and content.
