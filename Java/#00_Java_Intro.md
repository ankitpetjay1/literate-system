# Setting Up Java

## **Contents**

1. Installing and Running Java
2. Using IntelliJ for Development
3. Packaging Java Applications

---

<br>

### **Java code**

```Java
public class Hello {
    public static void main(String[] args) {
        System.out.println("Hello Pluralsight!");
    }
}

```

- The program has a single method called `main` which is called by default when you run this class.
- `args` is the parameter for Main method.
- In all, we are trying to output `Hello Pluralsight!` for our application.

<br>

**Compiling and Running Code**

- We use `javac` to complile the Java source code inside Hello.java into Java bytecode which lives in .class files.
- Hello.class file will be the outcome of the running `javac`.
- This bytecode is sytem independent can run on any kind of processor architectures.
- To run the bytecode in Hello.class we need 2 another components.
  - Java Standard Edition (SE) APIs
  - Java Virtual Machine (JVM)
- Our bytecode uses System class which we did not write to execute.
- System Class being part of the Java SE API is what makes our code useful.
- To run our Hello.class file, we are going to start our JVM using the command `java`.
- JVM knows how to read bytecode and execute the instructions in there.

- The tools like Java Standard Edition (SE) API and Java Virtual Machine (JVM) combine to form our Java Development Kit (JDK)

> Similar to Java SE APIs there are another set of APIs called Java Enterprise Edition (EE) APIs.
>
> These are geared to web application developements and enterprise application integrations, database access, etc.
>
> Java SE API are foundational APIs geared towards networking, file access, creating managing collections in your code.
>
> JEE are not part of JDK. You will need an application server that's on top of the JDK offers the JEE APIs to your application.
>
> JEE or also known as Jakarta EE now, was donated by Oracle to eclipse foundation.

<br>

### **Installing SE JDK**

1. Download latest JDK
   - Download from [jdk.java.net](jdk.java.net)
   - Extract downloaded file to C:\Program files.
   - Go on step in Java folder and copy the path.
2. Setup Java_Home variable (Points to directory containing Java folder)
   - Open windows setting > Search for environment
   - Click on Edit system env variables.
   - In Advanced tab > Env Variables.
   - In the top we have user env variables for current user and bottom we see System env variables.
   - In System env variables section click New.
   - Give name `JAVA_HOME`.
   - Paste the variable value as Java location directory.
3. Update PATH variable (Point to directory containing Java Compiler and Java runtime)
   - Select Path from System variables list and click edit.
   - Add entry using New.
   - Paste the Java installation directory path that was copied and append \bin
4. Verify using Windows cmd
   - Run `java --version` to check if the installtion was successful.

<br>

### **Getting Started**

1. Create a new folder and save the below code in a notepad file in the same folder.

   ```Java
   public class Hello {
       public static void main(String[] args) {
           System.out.println("Hello Pluralsight!");
       }
   }

   ```

2. Rename the notepad file to Hello.java
3. Open CMD and cd into the folder directory. Run the java code using below cmd.

   ```cmd
   javac Hello.java
   ```

4. A new file named Hello.class gets created in the same directory which is our bitecode.

5. We can now run this bytecode using JVM. Run the below cmd in the same CMD window.
   ```cmd
   java Hello
   ```
   > We do not need to add type here.
