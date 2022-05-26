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
