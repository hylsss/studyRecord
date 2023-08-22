## C#程序结构

C# 程序由一个或多个文件组成。 每个文件均包含零个或多个命名空间。 一个命名空间包含类、结构、接口、枚举、委托等类型或其他命名空间。

```c#
using System;

namespace c.biancheng.net {
    class Rectangle {
        // 成员变量
        double length;
        double width;
      
        // 成员函数
        public void Acceptdetails() {
            length = 4.5;  
            width = 3.5;
        }
      
        public double GetArea() {
            return length * width;
        }
      
        public void Display() {
            Console.WriteLine("Length: {0}", length);
            Console.WriteLine("Width: {0}", width);
            Console.WriteLine("Area: {0}", GetArea());
        }
 
    }
    class ExecuteRectangle {
        static void Main(string[] args) {
            Rectangle r = new Rectangle();
            r.Acceptdetails();
            r.Display();
            Console.ReadLine();
        }
    }
}
```



`using` 关键字用来在程序引入 `System` 命名空间

`namespace` 关键字用来声明一个命名空间，命名空间是用于组织代码的一种方式，以避免命名冲突。在这里，所有的类、结构、接口等都被放在了 `YourNamespace` 命名空间下，命名空间是类的集合。

`class` 通过一个已有的类 `（class）` 创建出这个类的对象 `（object）` 的过程叫做类的实例化。

`Main ` 为定义的函数名称，`Main`  函数是整个 C# 程序的入口，其中包含了程序运行时需要执行的操作。`static ` 和` void` 都是用来修饰 `Main` 函数的关键字。`Main`方法是 C# 应用程序的入口点，`Main`  方法是应用程序启动后调用的第一个方法。 **如果多个类包含 `Main` 方法，必须使用 StartupObject 编译器选项来编译程序，以指定将哪个 `Main` 方法用作入口点。 **

`成员变量` 是用来存储类中要使用的数据或属性的。

`成员函数` （也可以称为成员方法）是执行特定任务的语句集，一个类的成员函数需要在类中声明。上述代码中`Rectangle`  类包含三个成员函数，分别是  `AcceptDetails `、`GetArea`  和 `Display`。



## C#反射

反射（Reflection）是指程序可以访问、检测和修改它本身状态或行为的一种能力，反射中提供了用来描述程序集、模块和类型的对象，可以使用反射动态地创建类型的实例，并将类型绑定到现有对象，或者从现有对象中获取类型，然后调用其方法或访问其字段和属性

### 反射的优缺点

- 优点：提高了程序的灵活性和扩展性，降低耦合度
- 缺点：由于反射多了一道程序，性能上相较于直接代码要慢

### 通过反射获取类型

在C#中，通过反射获取类型的信息主要依赖于`System.Type`类。

- 获取对象的类型

  ```c#
  object obj = "Hello, World!";
  Type type = obj.GetType();
  Console.WriteLine(type.FullName);  // 输出：System.String
  ```
  
- 通过类型名称获取类型:已知完整的类型名称（包括命名空间），使用Type.GetType方法。

  ```c#
  Type type = Type.GetType("System.String");
  Console.WriteLine(type.FullName);  // 输出：System.String
  ```
  
- 从程序集中获取类型:从特定的程序集中获取类型,可以首先加载程序集，然后查询它的类型。

  ```c#
  Assembly assembly = Assembly.Load("AssemblyName");
  Type type = assembly.GetType("Namespace.TypeName");
  ```

- 获取类型的成员:有了Type对象，你可以查询其成员，如属性、方法、字段
  
  ```c#
  Type type = typeof(string);
  MethodInfo[] methods = type.GetMethods();
  foreach (MethodInfo method in methods)
  {
      Console.WriteLine(method.Name);
  }
  ```

-  使用`typeof`关键字:编译时已知类型，可以说使用 `typeof` 关键字直接获取类型

  ```c#
  Type type = typeof(int);
  Console.WriteLine(type.FullName);  // 输出：System.Int32
  ```

这只是获取类型信息的基础。反射API提供了大量的方法和属性，允许你深入查询类型的各种信息，如其构造函数、属性、方法、事件、接口、泛型参数等。但请注意，频繁使用反射可能会影响性能，因此在性能关键的代码中应谨慎使用
