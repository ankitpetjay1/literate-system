# Classes and Objects

Before we can create custom objects we need to create classes that can define those objects.

<br>

### **Module Overview**

1. Syntax for defining a class.

2. What is Object-Oriented Programming?

---

In C# a class defines a new type.

In order for our code to have a behavior we need a class.

We need to create a new class whenever the current class contains too much code or it is getting very complex.

We can encapsulate our code to create abstractions so that we don't have to go through the entire code but can use the method directly to get the output. For Eg: In previous module we created a program to calculate average grade, instead we can just write a single line of code to which we pass the grades as parameter and it gives us the output of average grade.

```C#
ComputeAverageGrade(grades);
```

This is how we implement abstraction and have proper encapsulation to manage software complexity.

In this module we will create a class to encapsulate our previous code.

The syntax for defining a class:

```C#
namespace GradeBook
{
    class Program
    {
        ...
        ...
    }
}
```

Every class should be in a namespace. If namespace is not present you are in Gloal namespace which is dangerous cause if someone else places a Program class in global namespace there will be a conflict.

You can have "." in namespace. For Eg:  
`namespace GradeBook.Math`. GradeBook.Math might contain a number of classes related to the math operations for a gradebook. Eg: `List` type that we defined earlier is in the namespace `System.Collections.Generic`

<br>

### **Creating class**

Goal is to create a new class so that we can assign it a new instance of a class. For Eg:

```C#
var book = new Book();
```

The minimum that we require for this is:

```C#
class Book
{

}

class Program
{
    static void Main(String[] args)
    {
        var book = new Book();
    }
}
```

So it is possible to create as many classes inside of a namespace. However as per convention we only allow one class per file. So the Program.cs file is dedicated to Program class and we will create a new Book.cs class in our "GradeBook folder" and update syntax:

```C#
namespace GradeBook
{
    class Book
    {

    }
}
```

Whenever we create classes we think about 2 things:

1. The right abstraction that we can give to the class. Building the right abstraction means giving this class the right members so other developers can understand what it is doing. For Eg: Recall when we used Lists. We instantiated double List type to variable `grades`. This List can now perform many things or invoke methods like Add, Sort, Clear, etc. This defines what is the behavior or things it can do.

   ```C#
   var grades = new List<double>() {....};

   grades.Add()
   grades.Clear()
   grades.Count
   ```

2. The state that is going to be stored inside the instances of this type, class. In List we are giving numbers to the list to hold.

> **In Summary**
>
> So a class consists of two things, the state or the data it holds and the behavior which typically acts on that state.

<br>

_So how do we want to use our Book class?_

1. The state should be that it should be able to hold grades coming into the application.

2. The behavior should be that it allows us to add grades to the book, compute statistics for all the grades.

### **Defining class**

So we want to give people the ability to be able to add a grade into the Book. For Eg: We can invoke something like below in Program.cs file:

```C#
var book = new Book();
book.AddGrade(89.1);
```

This means that our Book will need a method called `AddGrade`:

Recall how the method Main was defined in our Program class in Program.cs. We can replicate same with little changes in our Book class:

```C#
class Book
    {
        public void AddGrade(double grade)
        {
            ...
            ...
        }

    }
```

In the above code we want our method name to be AddGrade which should take a double type value named grade as parameter. And for now this method should be public not static.

Within our code we would want to store state or data that is instantiated.

```C#
class Book
    {
        public void AddGrade(double grade)
        {
            grades.Add(grade)
        }
        List<double> grades;

    }
```

A popular approach to add state in your code is to use field definition.

- If you create the double List variable inside the method it will only be available when we are inside of the AddGrade method. We want the the Book type to carry state with it and not only when we are inside the method.

- Therefore we define the grades outside of any method. grades is no longer a variable it is a field. Therefore implicity typing does not work and we only mention `List<double> grades;`

- Any methods that we have inside the Book class will have access to the grades field.

<br>

When we run our program we get a null reference exception for a line with code `grades.Add(grade)` in the Book.cs file.

Recall we instantiated new List in Program.cs file using `List<double> grade = new List<double>();`. An easy way to resolve above error is to instantiate field definition `List<double> grades = new List<double>();`.

```C#
class Book
    {
        public void AddGrade(double grade)
        {
            grades.Add(grade)
        }
        List<double> grades = new List<double>();

    }
```

Before we identify a better way we will first step back and define what class, object and null really mean.

**class**

Is a blueprint. Describes how we build objects.

A good way to understand class is using a cookie cutter.

Think of different cookie cutters stars, triangles, etc as classes. Each time we stamp out a piece of cookie from dough using the start cookie cutter the cookie becomes an object of the class star cookie cutter.

Each object is location in memory that the class instantiates to a variable.

The methods are part of the class definitions. Like how we intend to use AddGrade method for state.

**Object**

Every object is created by instantiating a class type to it.

Similar to how we created grades:

```C#
var grades = new List<double>() {12.7 , 10.3, 6.11};
```

**state**

Though we can instantiate an object of same class many times, each object may have a different state. For Eg:

```C#
var book2 = new Book();
var book1 = new Book();

book1.AddGrade(12.5);
book2.AddGrade(22.5);
```

In above code snippet we have 2 objects of class Book however both have seperate state. One object has the value 12.5 other has the value 22.5

Though the objects may have same behavior but every object can carry different and unique pieces of state.

At this point we will give our Book object a state called "null"

```C#
/*How we instantiate a new object from class Book: */
var book = new Book();

//Or
Book book1 = new Book();

// How we instantiate a null object

Book book2 = null;
book2.AddGrade(89.1);
```

With this we are not directly assigning any value to the object but we are indicating C# that the only way to interact with the object is to use the .AddGrade method.

> **Important**
>
> null can be the source of major errors in your program. Therefore avoid using null objects.

<br>

### **Constructor**

Coming back to our code Program.cs:

```C#
var book = new Book();
book.AddGrade(89.1);

var grades = new List<double>() { 12.7, 10.3, 6.11, 4.1 };
grades.Add(56.1);
```

When we are instantiating our object with class Book. Looking at the syntax `= new Book();` it appears like a method is being invoked with `Book()`.

Behind the scenes .NET runtime is invoking a **contructor method** on class `Book()`. The idea is a contructor constructs objects of type Book similar to how `var grades = new List<double>();` constructs grades object of type List.

So constructor is like another method on your class. Therefore if we choose to write our own constructor method, it's possible to take control of the initialization of the object produced by the class.

Writing an explicit constructor in Book.cs:

```C#
...
class Book
{
    public Book() //Constructor
    {
        grades = new List<double>();
    }
    public void AddGrade(double grade)
    {
        grades.Add(grade);
    }
    List<double> grades;
}
...
```

Some conventions for writing constructor:

1. A constructor should have same name as class.
2. Cannot have return type.
3. Anything within the constructor executes when we use the `new` keyword against the class. And it will execute before any other method like .AddGrade() method is invoked.

<br>

**Access Modifiers**

Whenever we create a Book object we are gauranteed to have `.AddGrade` method as it is part of the class definition.

We know within our book we have a List that we use to store our grades.

```C#
...
class Book
{
    public Book() //Constructor
    {
        grades = new List<double>();
    }
    public void AddGrade(double grade)
    {
        grades.Add(grade);
    }
    List<double> grades;
}
...
```

If at any point of time we want to add grade directly, why not use:

```C#
var book = new Book();
book.grades.Add(98.1)
```

We will see that book.grades will be inaccessible. This is due to it's protection. Since we have built our class to provide abstraction, we try to hide the complexity of our class. This makes us make method call without displaying the complex contents of our logic.

> **Important**
>
> Encapsulation means hiding the complexity of our program that are unimportant at that point.

To control the access we use something called access modifiers.

One of the access modifiers is `public` which means code outside of the class have access to this method.

We can add access modifiers to methods and also add them to fields. If we want to allow grades to be accessible in the previous code we can make the field `public`.

```C#
...
class Book
{
    public Book()
    {
        grades = new List<double>();
    }
    ...
    ...
    public List<double> grades;
}
...
```

Now when we invoke the previous code, it can access `Book.grades`

We will revert this as we do not want to allow illegal access. Instead we will use `private` access modifier to explictily mention that this is protected method.

```C#
...
class Book
{
    public Book()
    {
        grades = new List<double>();
    }
    ...
    ...
    private List<double> grades;
}
```

> **Important**
>
> The constructor and the .AddGrade method will still be able to access the field definition as they are members of the class.
>
> Code outside of the Book.cs will not be able to access the field.

<br>

**Constructor Parameter**

Let's say we want to give every book a name.

We would want to store that state inside of the class.

A good way to do this is to require a name as parameter while instantiating the book object.

We can make changes to the constructor to pass a name.

And then we will assign name to the field called name.

```C#
class Book
{
    public Book(string name) //passing parameter
    {
        grades = new List<double>();
        name = name; //Assigning parameter to field name.
    }
}
    ...
    ...
    private List<double> grades;
    private string name; //field definition
    ...
```

This creates a confusion within C# as it thinks we are making an assignment to the same variable.

To resolve this we use the keyword `this.` to direct C# that the `this.name` refers to the field object we are operating on.

```C#
class Book
{
    public Book(string name)
    {
        grades = new List<double>();
        this.name = name; // this keyword
    }
}
    ...
    ...
    private List<double> grades;
    private string name;
    ...
```

So now our invocation will look like:

```C#
...
var book = new Book("Ankit's Grade Book");
book.grades.Add(98.1)
...
```

<br>

### **Static Members**

From our Program.cs file, we saw the static keyword used with our Main method.

```C#
class Program
{
    static void Main(string[] args)
    {
        ...
        ...
    }
}

```

This refers to the fact that when calling a method with static keyword we need to call them by type. This means that we cannot call them by the variable we used to instantiate them and we must call them using class name. For Eg, for the Main method

```C#
class Program
{
    static void Main(string[] args)
    {
        var p = new Program();
        p.Main(args); // This will not be able to call Main method and run into an error

        Program.Main(args) // This will be able to call the static method
    }
}

```

In short, making a method static means that the method is no longer associated with an object instance.

> There are many static objects in our program, for eg `Console.WriteLine()`
>
> We do not create a new object to associate the class type to a new variable. We use Console class with WriteLine method.

<br>

### **Computing Statistics**

In order to prepare statistics let's look at what we need.

We would need our program to find the Highest Grade and the Lowest Grade.

We already know how to calculate average.

In order to identify the highest and lowest grade, we would need to individually compare the grades like below:

```C#
...
...
class Program
{
    static void Main(String[] args)
    {
        var book = new Book;
        book.AddGrade(98.5);
        book.AddGrade(77.6);
        book.AddGrade(54.55);

        var grades = new List<double>();
        grades.Add(65.4);
        grades.Add(87.65);
        grades.Add(77.5);

        var result = 0.0;
        highgrade = double.MinValue; //Assigning lowest value to highgrade
        lowgrade = double.MaxValue; //Assigning highest value to lowgrade
        foreach (var number in grades)
        {
            if(number >= highGrade) // Comparing highgrade with each element in list.
            {
                highGrade = number; //Storing the highest value in highgrade.
            }
            ...
            ...

        }
    }
}

```

To simplify our logic we can also use Math class for ease.

```C#
namespace GradeBook
{
    class Program
    {
        static void Main(String[] args)
        {
            var book = new Book;
            book.AddGrade(98.5);
            book.AddGrade(77.6);
            book.AddGrade(54.55);

            var grades = new List<double>();
            grades.Add(65.4);
            grades.Add(87.65);
            grades.Add(77.5);

            var result = 0.0;
            highgrade = double.MinValue; //Assigning lowest value to highgrade
            lowgrade = double.MaxValue; //Assigning highest value to lowgrade
            foreach (var number in grades)
            {
                highgrade = Math.Max(number, highgrade); //Compares list element with current highgrade and assigns max value to highgrade
                lowgrade = Math.Min(number, lowgrade); //Compares list element with current lowgrade and assigns min value to lowgrade
                result += number;
            }
            result /= grades.Count;
            Console.Write($"The highest grade is {highgrade}");
            Console.Write($"The lowest grade is {lowgrade}");
            Console.Write($"The average grade is {result}");
        }
    }
}
```

Now that we have the program ready we want to abstract all the code. We will create a method called `ShowStatistics` which will perform the necessary computation and give us the stats.

We will add a new member to our Book class file as ShowStatistics and add the compute logic.

```C#
namespace GradeBook
{
    class Book
    {
        public Book(string name)
        {
            var grades = new List<double>();
            this.name = name;
        }

        public void AddGrade(grade);
        {
            grades.Add(grade);
        }
        public void ShowStatistics()
        {
            var result = 0.0;
            highgrade = double.MinValue;
            lowgrade = double.MaxValue;
            foreach (var number in grades)
            {
                highgrade = Math.Max(number, highgrade);
                lowgrade = Math.Min(number, lowgrade);
                result += number;
            }
            result /= grades.Count;
            Console.WriteLine($"The highest grade is {highgrade:N1}");
            Console.WriteLine($"The lowest grade is {lowgrade:N1}");
            Console.WriteLine($"The average grade is {result:N1}");

        }
        private List<double> grades;
        private string name;
    }
}
```
