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

Creating Function App

- Function apps are part of Compute in Azure Portal.
- Select relevant Subscription, Resource Group.
- Name must be globally unique and will become part of the function app URL
- Publish will be code
- Select language you want to implement your function in. Version default.
- Region will be closest region to your users.
- Plan will be Consumption (Serverless).

> After the function app is created, you can access the URL to verify the app is ready.

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

Out JSON config specifies:

- Function will be triggered when a message is added to a queue named **myqueue-items**.
- Function then executes and it's return value is written to the **outTable** in Azure Table Storage.
-
