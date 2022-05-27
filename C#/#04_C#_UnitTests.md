# Unit Tests

Goal of unit tests is to test your code and check if it behaves correctly.

<br>

### **What is unit Testing**

**Testing** is to verify our code is behaving correctly.

So in our grade if we are writing software to compute average grade I want to make sure the result is the average of all grades but I also want to test edge conditions. Eg: How will software behave if there are "0" grades.

A **unit** is the source code that we want to test. Usually we want to test small unites of code. Eg: We might test the code inside of an individual method that calculates the average. Here the method will be the unit.

Unit testing is automated, meaning anytime we run a test we can run that test with no effort in the future using a tool known as **Test Runner**.

Test runner finds all the unit tests that you have written, executes each test and gives you a report to tell you if the test passed or anything failed. We can make changes and immediately see if the change creates a bug or fixes a bug.

Every languae environment comes with a unit test library and test runner that helps write and run these tests. We will be usign test library known as xUnit.net

<br>

### **Creating a unit test Project**

Initially when setting up the directory structure of our GradeBook project, we placed our GradeBook in src folder and created another folder called test.

This is where we will be creating our unit test project.

The general convention is to write your test project seperate from your production code.

cd to the location of test folder using cmd and create a new dot net project.

```cmd
mkdir GradeBook.Tests

cd GradeBook.Tests
```

Previously we selected the .NET console template for creating console application but now we want a unit test project. We will choose xunit project out of the many unit tests templates.

```cmd
dotnet new xunit
```

This creates a new Unit test project with UnitTest1.cs file.

> xunit is one of the nuget packages that is available for .NET Core and is not part of .NET Core
>
> nuget is the package manager for .NET and .NET Core
>
> When we execute the `dotnet new xunit` command it automatically downloads the xunit packages from nuget.org. To view the downloaded packages you can cd to the test project and run `dotnet list package` or check the .csproj file.

The syntax of UnitTest1.cs file contains

```C#
using System;
using Xunit;

namespace GradeBook.Tests
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {

        }
    }
}
```

`using Xunit` is one of the namespace provided by NuGet package. Within this namespace we will find all the types and API's that are needed to interact with testing framework.

Out test code must be executable statements. We know one of the ways is to organize the statements in our methods.

In current case `Test1()` is the member of the class named `UnitTest1`

We also see `[Fact]` which is called an attribute in C#. Attributes are little pieces of data that are attached to the symbol that follows it. so [Fact] is little piece of data attached to method `Test1()`

When Xunit loads up your test project to find tests inside, execute them and tell you what passed and what failed, it then goes looking for methods that have [Fact] attribute attached.

One might have 3 methods in a class. But only 2 represent unit tests. So we would decorate those 2 methods with [Fact] attribute. The other method might contain some code that we just want to call from other 2 test methods. Therefore Xunit will ignore that method and invoke only the 2 as tests methods to produce pass or fail result.

<br>

**Test Runner**

All the test discovery and excution happens when we run the **test runner**.

The test runner may be executed within VSCode using extension but it also comes with the .NET sdk.

To run a test simply cd to the test folder and run the cmd:

```cmd
dotnet test
```

The output will always consider the test to be passed until we specifcally mention in our unit tests what is passed or failed.

Let's see how to tell the framework how to pass and how to fail.

This requires an API provided by the class name Assert. We can make assertions based on conditions of our tests using the methods provided by Assert class. For Eg: We want to check if some object is equal to another object:

```C#

public class UnitTest1
{
    public void Test1
    {
        var x = 5;
        var y = 2;
        var expected = 7;
        var actual = x * y;
        Assert.Equal(expected, actual)
    }
}

```

The parameters of Equal method is: Expected value and Actual value where Expected value is what we want to get and Actual Value is what our code computed.

Now when you run the above code using cmd:

```cmd
dotnet test
```

It returns an error with lot of red text stating the parameter values of the Assert method.

You can try correcting the values and test again which should run successfully.

Most of the times unit tests are broken into 3 sections.

1. Arrange Section: This is where you put together test data and you arrange objects that you are going to use.

2. Act Section: Where you invoke a method to perform a computation that gives a result.

3. Assert Section: Where you assert something about the value that was computed inside of Act Section.

```C#
public class UnitTest1
{
    public void Test1
    {
        // arrange section
        var x = 5;
        var y = 2;
        var expected = 7;

        // act section
        var actual = x * y;

        // assert section
        Assert.Equal(expected, actual)
    }
}
```

### **Writing Tests**

Our goal is to write unit tests that will verify the logic within Book class that lies inside the GradeBook namespace.

Let us first rename the Test class from UnitTest1 to BookTest. Also need to change the filename from UnitTest1.cs to BookTest.cs.
This is general convention in many projects.

Within our Test1 method, in our arrange section we want to create an instance of Book class to gain access to Book class.

```C#
public class UnitTest1
{
    public void Test1
    {
        // arrange section
        var book = new Book("");

        // act section


        // assert section

    }
}
```

Note that we also have to provide a parameter "name" with the Book class.

<br>

**Adding project references**

However this will result in an error as C# is not able to reference Book class which is in another project in different directory.

To resolve this we need to tell C# to reference to other project and find Book class there.

Recall the .csproj file which contains reference to NuGet package. We can use similar config to reference to another project.

We previously automatically added reference to xunit package by creating test from xunit template. However if we want to reference to a package we would use `dotnet add package`

```cmd
dotnet add package xunit
```

Similarly to reference to another project we will use `dotnet add reference`

cd into the GradeBook.Test directory and run below cmd with the path of the target project.

```cmd
dotnet add reference ..\..\src\GradeBook\GradeBook.csproj
```

This adds a new reference into the GradeBookTest.csproj

> While building complex systems it is common to find a dozen references in this fashion.

A second step after referencing the object is to always ensure that you bring namespace of the referenced project. This is done through using the `using` statement. However in our current project we have used `namespace GradeBook.Tests` which means we are already in a namespace that is underneath the GradeBook.

<br>

**Accessing reference project**

Adding reference allows C# to point in the direction of the class we are looking for in another project however in order to access the class we need to think around access modifiers around the target class.

Going back to our Book.cs file, we have not specified any access modifier for class Book. If we do not specify an access modifier you will essentially be given access modifier of `internal`. This means the class can only be used inside of the same project GradeBook. In order to expose this we can simply update the access modifier to public.

> If our class is only written to be referenced internally we would not need to worry about encapsulation.

<br>

Our next step is to add some data into the book and invoke ShowStats() method

```C#
namespace GradeBook.Tests
{
    public class BookTest
    {
        [Fact]
        public void Test1()
        {
            // arrange
            var book = new Book("");
            book.AddGrade(89.1);
            book.AddGrade(90.5);
            book.AddGrade(77.3);

            // act
            book.ShowStats();

            // assert



        }
    }
}
```

Ideally when we write ShowStats we would get a result. If we have a variable that stores the result we could write asserts on it.

```C#
namespace GradeBook.Tests
{
    public class BookTest
    {
        [Fact]
        public void Test1()
        {
            // arrange
            var book = new Book("");
            book.AddGrade(89.1);
            book.AddGrade(90.5);
            book.AddGrade(77.3);

            // act
            var result = book.ShowStats();

            // assert
            Assert.Equal(85.6, result);
        }
    }
}
```

> In the above code snippet we have assigned result variable to the output of the ShowStats(). We need to pay attention when a piece of code is doing too many things.
>
> ShowStats() computes the lowest and highest grade as well as the average grade and it shows those grades on console.
>
> You always want to write smaller pieces of code and classes as they are easy to maintain as well as seperate deciding from the doing.

Therefore for ShowStats(), we want to seperate executing of the calculations from displaying the result of those calculations.

Our test would need a different method and different ways to be able to call parts of the method. Eg:

```C#
public class BookTest
{
    [Fact]
    public void Test1()
    {
        // arrange

        var book = new Book();
        book.AddGrade(89.1);
        book.AddGrade(90.5);
        book.AddGrade(77.3);

        // act

        var result = book.GetStats();

        // assert

        Assert.Equal(85.6,result.Average);
        Asset.Equal(90.5, result.High);
        Assert.Equal(77.3, result.Low);
    }
}
```

We will change the name from `ShowStats()` to `GetStats()` in the Book.cs file.

Currently the GetStats() method is returning void. We need the method to return an object. An object that has the states High, Low and Average.

Therefore we would be creating a new class of file named Statistics.cs in our GradeBook namespace and then create methods High, Low and Average within it.

The goal is to return the GetStats() method as instance of class Statistics.

Creating Statistics.cs

```C#
namespace GradeBook
{
    public class Statistics
    {
        public double Average;
        public double Low;
        public double High;
    }
}
```

Creating an instance of Statistics in Book.cs

```C#
...
...
    class Statistics GetStats()
    {
        ...
        ...
    }
...
...
```

Now what we want is to be able to invoke the states High, Low and Average. As these states are now field definitions in Statistics.cs we will be able to call them by first instantiating Statistics to an object.

```C#
...
...
    class Statistics GetStats()
    {
        var result = new Statistics();
        ...
    }
...
...
```

The rest of the code in Book.cs can be modified accordingly.

```C#
...
public class Book
    {
        public Book(string name)
        {
            grades = new List<double>();
            this.name = name;
        }
        public void AddGrade(double grade)
        {
            grades.Add(grade);
        }

        public Statistics GetStats()
        {
            var result = new Statistics();
            result.Average = 0.0;
            result.High = double.MinValue;
            result.Low = double.MaxValue;
            foreach (var grade in grades)
            {
                result.High = Math.Max(grade, result.High);
                result.Low = Math.Min(grade, result.Low);
                result.Average += grade;
            }
            result.Average /= grades.Count;

            return result;
        }

...
```

We would perform similar refactoring in our Program.cs file.

```C#
class Program
    {
        static void Main(string[] args)
        {
            var book = new Book("Ankit's Grade Book");
            book.AddGrade(89.1);
            book.AddGrade(90.5);
            book.AddGrade(77.85);
            var stats = book.GetStats();
            Console.WriteLine($"The highest grade is {stats.High:N1}");
            Console.WriteLine($"The lowest grade is {stats.Low:N1}");
            Console.WriteLine($"The average grade is {stats.Average:N1}");

        }
    }
```

The final state of our BookTests.cs file

````C#
```C#
public class BookTest
{
    [Fact]
    public void Test1()
    {
        // arrange

        var book = new Book();
        book.AddGrade(89.1);
        book.AddGrade(90.5);
        book.AddGrade(77.3);

        // act

        var result = book.GetStats();

        // assert

        Assert.Equal(85.6,result.Average, 1);
        Asset.Equal(90.5, result.High, 1);
        Assert.Equal(77.3, result.Low, 1);
    }
}
````

We have added a 3rd Assert.Equal parameter which signifies the decimal places to consider when checking actual result.

cd into the GradeBook.Tests and run the test now and check if there are any errors.

```cmd
dotnet test
```
