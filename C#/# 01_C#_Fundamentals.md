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
   cd Gradebook
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
