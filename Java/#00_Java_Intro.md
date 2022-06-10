# Setting up Java

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

<br>

### **IntelliJ for Java Development**

<br>

1. Popular IDE's

   - IntelliJ by JetBrains
   - Eclipse Foundation (Open Source)
   - NetBeans by Apache Foundation

2. Download IntelliJ Community Edition from [jetbrain.com/idea/download](jetbrain.com/idea/download)

3. Install exe.

<br>

**Create project**

1. Create New Project
2. In the Wizard, select Java version.
3. Do not create Project from template.
4. Name the project "TitleCaseConverter" and Finish.

**Writing and Running Project**

1. Expand project "TitleCaseConverter"
   > ".idea" and ".iml" are IntelliJ specific and contain settings.
   >
   > "src" directory will contain Java source file.
2. Right click on the src folder and click New > Java Class
3. Name the class `Main`
4. Copy the below Java GUI code:

```Java
package com.ankitsingh;

import javax.swing.*;
import java.awt.*;

public class Main {

    public static void main(String... args) {
        JFrame application = createGUI();
        application.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        application.setVisible(true);
    }

    private static JFrame createGUI() {
        JTextField input = new JTextField();
        input.setPreferredSize(new Dimension(300, 40));

        JButton convertButton = new JButton("Convert");

        JLabel output = new JLabel();
        output.setPreferredSize(new Dimension(300, 40));

        convertButton.addActionListener(event -> {
            output.setText(TitlecaseConverter.convertToTitleCase(input.getText()));
        });

        JFrame gui = new JFrame("Title case converter");
        gui.setLayout(new FlowLayout());
        gui.add(input);
        gui.add(convertButton);
        gui.add(output);
        gui.pack();
        gui.setLocationRelativeTo(null); // Centering the screen

        return gui;
    }

}
```

5. Press Alt + Enter on red highlighted codes to automatically import types.

6. Right click on the Main class and click Run to compile and run the code.

7. We need to create a Title case converter so we will go ahead and create a new Java class and name it "TitleCaseConverter".

8. Copy the below code snippet.

```Java
package com.ankitsingh;

public class TitlecaseConverter {

    public static String convertToTitleCase(String input) {
        StringBuilder builder = new StringBuilder();

        for (String word : input.split("\\s")) {
            if (word.length() < 4) {
                builder.append(word.toLowerCase());
            } else {
                builder.append(word.substring(0, 1).toUpperCase());
                builder.append(word.substring(1).toLowerCase());
            }
            builder.append(" ");
        }

        return builder.toString();
    }
}

```

9. Now if we run our Main class file, we see the output where any word greater than 3 letters have their first letter capitalized.

> Where is the .class bytecode stored when IntelliJ compliles our code?
>
> After running our code for the first time, an new folder "out" is created which stores all our .class files.

10. Expand the "out" folder > "production" > "TitleCaseConverter". This contains our 2 compiled class files.

<br>

**Packaging Project**

You use packages when you create larger applications containing multiple classes and types.

1. Select both source code files, right click > Refactor > Move Classes

2. Provide name of the package. Eg: "com.ankitsingh"

3. Click Refactor

4. Now we can see our package under the "src" file system.

5. IntelliJ adds package statements to the source code as well.

<br>

### **Packaging Java Applications**

1. Java Applications are packaged into JAR files i.e... Java Archive.

2. JAR file is basically a zip file containing all application classes.

> For Eg: Our TitleCaseConverter.jar file will contain two classes:
>
> com/  
> ankitsingh/  
>  Main.class  
>  TitleCaseConverter.class

3. To execute the files we need .class file which contains platform independent bytecode generated by Java compiler.

4. Besides class files, JAR files may also contain additional metadata. This is stored in MANIFEST.MF file nested inside META-INF folder.

<br>

**Creating JAR files outside IDE**

We can create JAR files which combines our class files and can run on any system that has Java Virtual Machine JVM installed.

1. Besides JAVA SDK and Java runtime, there is an additional tool in the JDK called jar. This is used to create jar files.

2. Call the cmd `jar cvf` to create verbose to see what it is doing and an f to indicate that we are providing a file to the cmd. Eg:

   ```cmd
   jar cvf TitleCaseConverter.jar .
   ```

3. We execute the cmd in the output directory where the compiler has placed the classes. We do this by placing the "." at the end.

4. This is what it takes to create a TitleCaseConverter.jar file.

   > A MANIFEST.MF files is also generated by the JAR tool during the process.

5. To run the jar file we need to use `java -jar` cmd along with the file.

   ```cmd
   java -jar TitleCaseConverter.jar
   ```

   > However as you will discover that the above cmd outputs an error.
   >
   > This is because java does not know which class contains the Main method.
   >
   > This can be done by creating jar file in slightly different way.

6. We can have the TC-MANIFEST.MF file contain the information of our Main class so it knows which class contains main method. Eg: Let's say our TC-MANIFEST.MF conains below entry:

   ```txt
   Main-Class: com.ankitsingh.Main
   ```

   Therefore we will run the below cmd:

   ```cmd
   jar cvmf TC-MANIFEST.MF TitleCaseConverter.jar .
   ```

   > The m parameter is added which expects a file name that contains the entries and need to be immersed into resulting MANIFEST.MF file.

7. The the final MANIFEST.MF file will now look like:

   ```txt
   Manifest-Version: 1.0
   Created-By: 13.0.1 (Oracle Corporation)
   Main-Class: com.ankitsingh.Main
   ```

8. Now we can run the java cmd `java -jar TitleCaseConverter.jar` to execute our bytecode.
   > With this our bytecode runs independent of our IDE.

<br>

**Creating JAR files inside IDE**

1. In IntelliJ, File > Project Structure

2. In the next window, select Artifacts tab.

3. Add an artifact > JAR > From modules

4. Module is already selected as TitleCaseConverter and we only need to provide class that contains our main method that runs first. Browse and select and click ok.

5. The newly defined JAR artifact shows up.

6. Check Include in project build, to tell IntelliJ to include this JAR file when we build the project.

7. Click Ok

   > We can see that IntelliJ generated a META-INF file inside the src folder that contains MANIFEST.MF

8. When we click build project, we also see an artifact folder created in out folder which conains the jar file.

9. This is where the IntelliJ will run the jar file from. We can also copy the path of the file.

10. cd into the copied path and run the jar file using the same command `java -jar TitleCaseConverter.jar`

> In large organizations there are multiple jar files with it's own dependencies. Creating the jar file is not a manual process as we did, this is part of the a build tool that orchestrates the steps.
>
> Build tools first **build** or compile the code.
>
> Build tools will then run unit **tests** or integration against the code base.
>
> Next the build tools invoke static **analysis** on the code base.
>
> Last step is to **package** the files.
>
> Popular build tools include **Maven** and **Gradle**
