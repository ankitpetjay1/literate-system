# C# Syntax

**Requirement**

We need an electronic grade book to read the scores of an individual student and then compute some simple statistics from the scores.

The grades are entered as floating point numbers from 0 to 100, and the statistics should show us the highest grade, the lowest grade, and the average grade.

> Generally it's the system design and how components will come together is the hardest part but we learn the language so that we don't have to think about syntax details and can focus on these bigger, harder challenges.
>
> The goal is always to start small and tackle little problems so that you can get them out of the way and can see the bigger picture.
>
> Eg: Given the collection of grades we need to show the average grade. This will require math operations. We will see how we can do the syntax for same.

<br>

---

<br>

**Variables**

Variables are storage location to hold some value.

Similar to parameters of Main method every variable has name and a type.

To declare a float variable named x:

```c#
float x;
```

To declare double precise float (Takes more storage space):

```C#
double x;
```

Declaration and Initialization of variables:

```C#
double x = 34.1;
```

> You can tell C# to implcitly identify the type of value that is being assigned using the type `var`. In below code C# automatically assigns double type due to the existence of decimal in the assigned value.

    ```C#
    var x = 34.1;
    ```

> You cannot later change the type being assigned to x.
>
> var type requires that you initialize values, you cannot leave it without initialization.

<br>

**Grading**

We would need to pass the numbers in some format to our code. We will be using array type for collection of all numbers.

```C#
double[] numbers;
```

In above syntax we are declaring a double array with "numbers" as the name of the variable.

> This is however incorrect. In C# we need to instantiate the variable before initializing values to it. In our case "numbers" is not initialized to any value. So we instantiate first and also mention 3 as the size of that array meaning our array can hold 3 floating point numbers.

```C#
double[] numbers = new double[3];
numbers[0] = 12.7;
numbers[1] = 10.3;
numbers[2] = 6.11;
```

1. We will use array initialization syntax to initialize array values. Since we are initializing values we can also use var type to ask C# to identify type.
   We also don't need to specify array size. This simplifies our code as:

   ```C#
   var numbers = new[] {12.7,10.3,6.11};
   ```

2. We can now add the elements in our array.

   ```C#
   var numbers = new[] {12.7,10.3,6.11};

   var result = numbers[0];
   result += numbers[1];result += numbers[2];
   ```

   We do not know how many items are exactly present in our array to add each item. Also it is really tedious to add new array value to result each time. To simplify this we can use foreach loop to parse through the size of our array.

   ```C#
   var numbers = new[] {12.7,10.3,6.11};

   var result = 0.0;

   foreach(var number in numbers)
   {
       result += number;
   }
   Console.WriteLine(result);
   ```

3. Another challenge is we don't know how many grades are possible. And given an array we have to specify the size of our double array when initializing.

   > One of the .NET libraries provide a solution for this in the namespace System.Collections.Generic.
   >
   > It contains number of classes we can use that contains Data Structures like stack queue and lists.

   A list class is a dynamic data structure we can use to keep and add list of items. In order to use lists you need to do 2 things:

   - Use the System.Collections.Generic namespace.
   - What types of things you are going to put into that list. Eg: Invoice objects or employee objects, integers, date times, strings or double precision float values. In our case we only need double precision float numbers.

    <br>

   Initializing list with double:

   ```C#
   using System;
   using System.Collections.Generic;

   namespace GradeBook
   {
       class Program
       {
           static void Main(string[] args)
           {
               var grades = new List<double>() { 12.7, 10.3, 6.11 };
               ...
               ...
           }
       }
   }
   ```

   When using lists we do not use + operator to add values. We can simply call List method Add()

   ```C#
   using System;
   using System.Collections.Generic;

   namespace GradeBook
   {
       class Program
       {
           static void Main(string[] args)
           {
               var grades = new List<double>() { 12.7, 10.3, 6.11 };
               grades.Add(47.1);

               var result = 0.0;
               foreach(number in grades)
               {
                   result += number;
               }
               result /= grades.Count;
               Console.WriteLine($"The average of the grades is {result}");
           }
       }
   }

   ```

4. Now we can find average grade from our list of numbers and output to the console the average grade.

   ```C#
   using System;
   using System.Collections.Generic;

   namespace GradeBook
   {
       class Program
       {
           static void Main(string[] args)
           {
               var grades = new List<double>() { 12.7, 10.3, 6.11 };
               grades.Add(47.1);

               var result = 0.0;
               foreach(number in grades)
               {
                   result += number;
               }
               result /= grades.Count;
               Console.WriteLine($"The average of the grades is {result:N1}");
           }
       }
   }
   ```

   > We can use several types of formatting in displaying the float value. In above code snippet we have used N1 which tells C# that we want only 1 decimal place in our output.
