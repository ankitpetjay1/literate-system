# C# Fundamentals

<br>

**Tools**

1. .NET Core SDK
2. .NET Framework (Runtime) SDK

<br>

## .NET

When you write code on your machine there has to be some software to translate the C# code into instructions for machine.

This software is what we refer to as .NET

Within this we have:

- CLR (Common Language Runtime)
  Is the runtime that knows how to bring program to life and manage memory, send in instructions to the Intel, AMD or ARM processor.
  > .NET can run not only C# code but other languages as well such as Visual Basic .NET, F#, etc.
- FCL (Framework Class Library)
  Library of code already written and tested by other devs.
  > The code from this library may be used in C# program to do activities like communicate over the network with HTTP or send encrypted message or you need to open a file.

<br>

**.NET Command Line**

.NET is available over the windows command prompt with keyword dotnet.

```cmd
dotnet

dotnet --info

dotnet --help
```

If you have a C# code in a file, you need to first build the code into another file before you can run the program. You can do it using cmd:

```cmd
dotnet build
```

.NET runtime can then load and execute the code.

Other commands include `dotnet test` to perform unit tests if the C# code is working as expected, `dotnet new` to create new dotnet project.

> **Project** is a collection of source code files that you want to put together into a single application or library that you write to share with other devs.

<br>

## **Getting Started**

<br>

**1. dotnet new**

When you run `dotnet new` it asks for the templates that you want to use for the new project.

- A _Console Application_ is the simplest app that runs in the shell console.

- To create a project full of unit tests you could type `dotnet new mstest`

- To create a new web application using ASP.NET Core you could type `dotnet new web`

With these templates dotnet will create a basic project strucutre required based on the type of application you are building.

1. Create project directory:
   ```cmd
   mkdir gradebook
   cd gradebook
   ```
2. Create source directory:

   ```cmd
   mkdir src
   mkdir test
   ```

3. Create a new folder for project in src and create a simple console application in it.

   ```cmd
   cd src
   mkdir GradeBook
   cd GradeBook
   dotnet new console
   ```

GradeBook.csproj and Program.cs will be created in the project.

> ".csproj extension means this is a C# project.
> ".cs" file contains C# some code that is part of the console application.

**2. dotnet run**

Running `dotnet run` will look inside the folder in which we are in for a project and wiil find GradeBook.csproj and execute the project.

<br>

_How to change the contents of the file being executed?_

1. Go to the main directory of the project and open it in vs code.

   ```cmd
   cd ..\..\
   code .
   ```

2. You can find your code in program.cs file.

<br>

_What happens behind the scenes when we run `dotnet run`?_

`dotnet restore` run implicitly and checks NuGet for any external dependencies and grabs them.

NuGet packages contain code from other developers that you can use to build your application.

> Similar to `npm` for node and `pip` for Python.

`dotnet build` also runs imilicitly and compiles our code.

This produces a binary representation from your C# source code. This is a file with extension ".dll". This is also called an assembly in .NET. Location of file is in $location\src\gradebook\bin\debug\netcoreappv3.x\GradeBook.dll

> You can execute the dll files on CLI:
>
> ```cmd
> dotnet
> C:\code\Projects\literate-system\C#\gradebook\src\GradeBook\bin\Debug\net5.0\GradeBook.dll
> ```

Another folder named "obj" is present to put together restore and build process.

<br>

### **Syntax**

```C#
using System;

namespace GradeBook
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}

```

- We have the method, the name of the method is Main.

  ```C#
  static void Main(string[] args)
        {
              Console.WriteLine("Hello World!");
        }
  ```

- When we invoke the method Main, the code inside the method gets executed.

  > When we run our program via cmd line (build and assembly), Main method is the entry point of application and gets executed first.

- Every method can have 0 or some parameters. Parameters have a type and a name. The Main method have parameters of type `string[]` and name `args`. The square brackets after string say that it is a string array. Therefore we can pass a collection of strings as args.

- So if someone passes us 3 items, we can access the 2nd element of the array using `args[1]`

<br>

_From C# code above how will you replace World with an argument?_

By concat:

```C#
static void Main(string[] args)
        {
              Console.WriteLine("Hello " + args[0] + "!");
        }
```

String interpolation:

```C#
static void Main(string[] args)
        {
              Console.WriteLine($"Hello {args[0]} !");
        }
```

Testing output:

```cmd
dotnet run -- Ankit
```

> We use -- to indicate that "Ankit" is not a parameter for CLI but for the Main method.
>
> If you do not pass the parameter the cmd will run into a range exception as the args[0] does not exist.

Handling Exception:
.NET will not allow program to execute if there is an unhandled exception. A debugger allows to execute program in a controlled environment and inspect the source of problem as we go along.

```C#
static void Main(string[] args)
        {
            if (args.Length > 0)
            {
                Console.WriteLine($"Hello {args[0]}!");
            }
            else
            {
               Console.WriteLine("Hello!");
            }

        }
```

Go to .vscode folder > Launch.json and under configurations section find "args". The value to the args here is what will be used when running your code.

Experiment with passing 2 arguments using Launch.json and using CLI to see results.
