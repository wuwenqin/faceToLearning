# 												Spring面试题

## 												**什么是**spring?

Spring是**一个轻量级 Java 开发框架**,目的是为了解决企业级应用开发的业务逻辑层和其他各层的耦合问题。是一个分层的JavaSE/JavaEE full-stack（一站式）轻量级开源框架，为开发Java应用程序提供全面的基础架构支持。Spring负责基础架构，因此Java开发者可以专注于应用程序的开发。

Spring最根本的使命是  **解决企业级应用开发的复杂性，即简化 Java 开发** 。

Spring可以做很多事情，它为企业级开发提供给了丰富的功能，但是这些功能的底层都依赖于它的**两个核心特性**，也就是 **依赖注入**（ dependency injection ， DI ）**和面向切面编程**（ aspect -oriented programming ， AOP ） 。

为了降低Java开发的复杂性，Spring采取了以下4种关键策略**

1.基于POJO的轻量级和最小侵入性编程；

2.通过依赖注入和面向接口实现松耦合；

3.基于切面和惯例进行声明式编程；

4.通过切面和模板减少样板式代码

------



## 												Spring 的俩大核心概念

## 				请问什么是IoC和DI？并且简要说明一下DI是如何实现的？

**IOC（控制反转）：**

 IoC叫控制反转，是Inversion of Control的缩写，DI（Dependency Injection）叫依赖注入，是对IoC更简单的诠释。控制反转是把传统上由程序代码直接操控的对象的调用权交给容器，通过容器来实现对象组件的装配和管理。所谓的"控制反转"就是对组件对象控制权的转移，从程序代码本身转移到了外部容器，由容器来创建对象并管理对象之间的依赖关系。

 DI 依赖注入的基本原则是应用组件不应该负责查找资源或者其他依赖的协作对象。配置对象的工作应该由容器负责，查找资源的逻辑应该从应用组件的代码中抽取出来，交给容器来完成。DI是对IoC更准确的描述，即组件之间的依赖关系由容器在运行期决定，形象的来说，即由容器动态的将某种依赖关系注入到组件之中。

依赖注入可以通过setter方法注入（设值注入）、构造器注入和接口注入三种方式来实现，Spring支持setter注入和构造器注入，通常使用构造器注入来注入必须的依赖关系，对于可选的依赖关系，则setter注入是更好的选择，setter注入需要类提供无参构造器或者无参的静态工厂方法来创建对象。

**AOP（面对切面编程）**  

在运行时，动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。

使用AOP技术，可以将一些系统性相关的编程工作，独立提取出来，独立实现，然后通过切面切入进系统。

从而避免了在业务逻辑的代码中混入很多的系统相关的逻辑——比如权限管理，事物管理，日志记录等等。





## 							谈一谈Spring中自动装配的方式有哪些？

\- no：不进行自动装配，手动设置Bean的依赖关系。
\- byName：根据Bean的名字进行自动装配。
\- byType：根据Bean的类型进行自动装配。
\- constructor：类似于byType，不过是应用于构造器的参数，如果正好有一个Bean与构造器的参数类型相同则可以自动装配，否则会导致错误。
\- autodetect：如果有默认的构造器，则通过constructor的方式进行自动装配，否则使用byType的方式进行自动装配。

------



## 										Spring中Bean的作用域有哪些？

 

singleton: 在SpringIoc容器中仅存在一个bean实例,bean以单实例方式存在

prototype: 每次调用getbean() 都将返回一个新的实例

request: 每次Http请求都会创建一个新的bean,该作用域仅适合于WebApplicationContext 环境

session: 同一个Http Session 共享一个bean,不同的Http Session使用不同的bean.该作用域仅适合 WebApplicationContext 环境
 



------

## 				请说明一下Spring中BeanFactory和ApplicationContext的区别是什么？

BeanFactory：
Spring 容器最核心也是最基础的接口，本质是个工厂类，用于管理 bean 的工厂，最核心的功能是加载 bean，也就是 getBean 方法，通常我们不会直接使用该接口，而是使用其子接口。。因为比较古老，所以BeanFactory无法支持spring插件，例如：AOP、Web应用等功能。

ApplicationContext
ApplicationContext是BeanFactory的子类，因为古老的BeanFactory无法满足不断更新的spring的需求，于是ApplicationContext就基本上代替了BeanFactory的工作，以一种更面向框架的工作方式以及对上下文进行分层和实现继承，并在这个基础上对功能进行扩展：
<1>MessageSource, 提供国际化的消息访问
<2>资源访问（如URL和文件）
<3>事件传递
<4>Bean的自动装配
<5>各种不同应用层的Context实现

区别：

<1>如果使用ApplicationContext，如果配置的bean是singleton，那么不管你有没有或想不想用它，它都会被实例化。好处是可以预先加载，坏处是浪费内存。
<2>BeanFactory，当使用BeanFactory实例化对象时，配置的bean不会马上被实例化，而是等到你使用该bean的时候（getBean）才会被实例化。好处是节约内存，坏处是速度比较慢。多用于移动设备的开发。
<3>没有特殊要求的情况下，应该使用ApplicationContext完成。因为BeanFactory能完成的事情，ApplicationContext都能完成，并且提供了更多接近现在开发的功能。



------

## 														 **Spring IOC** **的实现机制**

​																	Spring 中的 IOC 的实现原理就是**工厂模式加反射机制**









## 										Spring 的 AOP 是怎么实现的 

本质是通过动态代理来实现的，主要有以下几个步骤。

1、获取增强器，例如被 Aspect 注解修饰的类。

2、在创建每一个 bean 时，会检查是否有增强器能应用于这个 bean，简单理解就是该 bean 是否在该增强器指定的 execution 表达式中。如果是，则将增强器作为拦截器参数，使用动态代理创建 bean 的代理对象实例。

3、当我们调用被增强过的 bean 时，就会走到代理类中，从而可以触发增强器，本质跟拦截器类似。

------

## 								Spring 的 AOP 有哪几种创建代理的方式 

Spring 中的 AOP 目前支持 JDK 动态代理和 Cglib 代理。

通常来说：如果被代理对象实现了接口，则使用 JDK 动态代理，否则使用 Cglib 代理。另外，也可以通过指定 proxyTargetClass=true 来实现强制走 Cglib 代理。

 

------

## 										JDK 动态代理和 Cglib 代理的区别 

1、JDK 动态代理本质上是实现了被代理对象的接口，而 Cglib 本质上是继承了被代理对象，覆盖其中的方法。

2、JDK 动态代理只能对实现了接口的类生成代理，Cglib 则没有这个限制。但是 Cglib 因为使用继承实现，所以 Cglib 无法代理被 final 修饰的方法或类。

3、在调用代理方法上，JDK 是通过反射机制调用，Cglib是通过FastClass 机制直接调用。FastClass 简单的理解，就是使用 index 作为入参，可以直接定位到要调用的方法直接进行调用。

4、在性能上，JDK1.7 之前，由于使用了 FastClass 机制，Cglib 在执行效率上比 JDK 快，但是随着 JDK 动态代理的不断优化，从 JDK 1.7 开始，JDK 动态代理已经明显比 Cglib 更快了。

### JDK 动态代理为什么只能对实现了接口的类生成代理

根本原因是通过 JDK 动态代理生成的类已经继承了 Proxy 类，所以无法再使用继承的方式去对类实现代理。

------



### 											Spring 的事务传播行为有哪些

Spring事务的传播行为在Propagation枚举类中定义了如下几种选择:

1、REQUIRED：Spring 默认的事务传播级别，如果上下文中已经存在事务，那么就加入到事务中执行，如果当前上下文中不存在事务，则新建事务执行。

2）REQUIRES_NEW：每次都会新建一个事务，如果上下文中有事务，则将上下文的事务挂起，当新建事务执行完成以后，上下文事务再恢复执行。

3）SUPPORTS：如果上下文存在事务，则加入到事务执行，如果没有事务，则使用非事务的方式执行。

4）MANDATORY：上下文中必须要存在事务，否则就会抛出异常。

5）NOT_SUPPORTED ：如果上下文中存在事务，则挂起事务，执行当前逻辑，结束后恢复上下文的事务。

6）NEVER：上下文中不能存在事务，否则就会抛出异常。

7）NESTED：嵌套事务。如果上下文中存在事务，则嵌套事务执行，如果不存在事务，则新建事务。

 



 

------



### 															Spring 事务的实现原理

AOP（动态代理）

动态代理：基本所有要进行逻辑增强的地方都会用到动态代理，AOP 底层也是通过动态代理实现。



Spring事务支持两种方式，**编程式事务**和**声明式事务**

**@Transactional注解应用到public方法，才能进行事务管理**



### Spring事务的隔离级别

spring事务隔离级别就是数据库的隔离级别:外加一个默认级别

- read uncommitted（未提交读）
- read committed（提交读，不可重复读）
- repeatable read（可重复读）
- serializable（可串行划）

------



## 										@Resource 和 @Autowire 的区别 

1、@Resource 和 @Autowired 都可以用来装配 bean

2、@Autowired 默认按类型装配，默认情况下必须要求依赖对象必须存在，如果要允许null值，可以设置它的required属性为false。

3、@Resource 如果指定了 name 或 type，则按指定的进行装配；如果都不指定，则优先按名称装配，当找不到与名称匹配的 bean 时才按照类型进行装配。

------



### 							使用 Mybatis 时，调用 DAO接口时是怎么调用到 SQL 的

1、DAO接口会被加载到 Spring 容器中，通过动态代理来创建

2、XML中的SQL会被解析并保存到本地缓存中，key是SQL 的 namespace + id，value 是SQL的封装

3、当我们调用DAO接口时，会走到代理类中，通过接口的全路径名，从步骤2的缓存中找到对应的SQL，然后执行并返回结果

 

------

## 											 **Spring MVC  流程** 

工作原理：

1、 用户发送请求至前端控制器DispatcherServlet。 

2、 DispatcherServlet收到请求调用HandlerMapping处理器映射器。

3、 处理器映射器找到具体的处理器(可以根据xml配置、注解进行查找)，生成处理器对象及处理器拦截

器(如果有则生成)一并返回给DispatcherServlet。 

4、 DispatcherServlet调用HandlerAdapter处理器适配器。

5、 HandlerAdapter经过适配调用具体的处理器(Controller，也叫后端控制器)。 

6、 Controller执行完成返回ModelAndView。 

7、 HandlerAdapter将controller执行结果ModelAndView返回给DispatcherServlet。 

8、 DispatcherServlet将ModelAndView传给ViewReslover视图解析器。

9、 ViewReslover解析后返回具体View。

10、DispatcherServlet根据View进行渲染视图（即将模型数据填充至视图中）。11、 DispatcherServlet响应用户。

**组件说明：**

以下组件通常使用框架提供实现：

DispatcherServlet：作为前端控制器，整个流程控制的中心，控制其它组件执行，统一调度，降低组件

之间的耦合性，提高每个组件的扩展性。

HandlerMapping：通过扩展处理器映射器实现不同的映射方式，例如：配置文件方式，实现接口方

式，注解方式等。

HandlAdapter：通过扩展处理器适配器，支持更多类型的处理器。

ViewResolver：通过扩展视图解析器，支持更多类型的视图解析，例如：jsp、freemarker、pdf、 

excel等。

**组件：**

**1****、前端控制器****DispatcherServlet****（不需要工程师开发）****,****由框架提供**

作用：接收请求，响应结果，相当于转发器，中央处理器。有了dispatcherServlet减少了其它组件之间

的耦合度。

用户请求到达前端控制器，它就相当于mvc模式中的c，dispatcherServlet是整个流程控制的中心，由

它调用其它组件处理用户的请求，dispatcherServlet的存在降低了组件之间的耦合性。

**2****、处理器映射器****HandlerMapping(****不需要工程师开发****),****由框架提供**

作用：根据请求的url查找Handler

HandlerMapping负责根据用户请求找到Handler即处理器，springmvc提供了不同的映射器实现不同

的映射方式，例如：配置文件方式，实现接口方式，注解方式等。

**3****、处理器适配器****HandlerAdapter**

作用：按照特定规则（HandlerAdapter要求的规则）去执行Handler

通过HandlerAdapter对处理器进行执行，这是适配器模式的应用，通过扩展适配器可以对更多类型的

处理器进行执行。

**4****、处理器****Handler(****需要工程师开发****)**

**注意：编写****Handler****时按照****HandlerAdapter****的要求去做，这样适配器才可以去正确执行****Handler**

Handler 是继DispatcherServlet前端控制器的后端控制器，在DispatcherServlet的控制下Handler对具

体的用户请求进行处理。

由于Handler涉及到具体的用户业务请求，所以一般情况需要工程师根据业务需求开发Handler。 

**5****、视图解析器****View resolver(****不需要工程师开发****),****由框架提供**

作用：进行视图解析，根据逻辑视图名解析成真正的视图（view）

View Resolver负责将处理结果生成View视图，View Resolver首先根据逻辑视图名解析成物理视图名即

具体的页面地址，再生成View视图对象，最后对View进行渲染将处理结果通过页面展示给用户。

springmvc框架提供了很多的View视图类型，包括：jstlView、freemarkerView、pdfView等。

一般情况下需要通过页面标签或页面模版技术将模型数据通过页面展示给用户，需要由工程师根据业务

需求开发具体的页面。

**6****、视图****View(****需要工程师开发****jsp...)**

View是一个接口，实现类支持不同的View类型（jsp、freemarker、pdf...）

**核心架构的具体流程步骤如下：**

1、首先用户发送请求——>DispatcherServlet，前端控制器收到请求后自己不进行处理，而是委托给

其他的解析器进行处理，作为统一访问点，进行全局的流程控制；

2、DispatcherServlet——>HandlerMapping， HandlerMapping 将会把请求映射为

HandlerExecutionChain 对象（包含一个Handler 处理器（页面控制器）对象、多个

HandlerInterceptor 拦截器）对象，通过这种策略模式，很容易添加新的映射策略；3、DispatcherServlet——>HandlerAdapter，HandlerAdapter 将会把处理器包装为适配器，从而支

持多种类型的处理器，即适配器设计模式的应用，从而很容易支持很多类型的处理器；

4、HandlerAdapter——>处理器功能处理方法的调用，HandlerAdapter 将会根据适配的结果调用真

正的处理器的功能处理方法，完成功能处理；并返回一个ModelAndView 对象（包含模型数据、逻辑视

图名）；

5、ModelAndView的逻辑视图名——> ViewResolver， ViewResolver 将把逻辑视图名解析为具体的

View，通过这种策略模式，很容易更换其他视图技术；

6、View——>渲染，View会根据传进来的Model模型数据进行渲染，此处的Model实际是一个Map数

据结构，因此很容易支持其他视图技术；

7、返回控制权给DispatcherServlet，由DispatcherServlet返回响应给用户，到此一个流程结束。

下边两个组件通常情况下需要开发：

Handler：处理器，即后端控制器用controller表示。

View：视图，即展示给用户的界面，视图中通常需要标签语言展示模型数据。



------











