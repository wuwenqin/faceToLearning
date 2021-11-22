# 												JVM学习

1.请你谈谈你对JVM的理解？ java8虚拟机和之前的变化更新？

2.什么是OOM，什么是栈溢出StackOverFlowError? 怎么分析?

3.JVM的常用调用参数有哪些

4.内存快照如何抓取？怎么分析Dump文件

5.谈谈JVM中，类加载器 你的认识?



## 1.JVM的位置

![image-20210722091757995](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722091757995.png)



## 2.JVM的体系结构

![image-20210722094345982](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722094345982.png)



## 3.类加载器

![image-20210722095527783](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722095527783.png)



作用：加载并初始化class字节码文件

![image-20210722101544571](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722101544571.png)

​		(1.虚拟机自带的加载器

​		(2.启动类(根) 加载器

​		(3.扩展类加载器     //ExtClassLoader     

​		(4.应用程序加载器

![image-20210722104414700](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722104414700.png)









## 4.双亲委派机制 (请求从下往上委派，加载是从上往下)

​	(1) APP -->EXC-->BOOT(最终执行，全名叫bootstrap class loader)

​	类加载器收到类加载的请求Application，将这个请求向上委托给父类加载器去完成，一直向上委托，直到启动类加载器Boot

​	启动类加载器检查是否能够加载当前这个类，能加载就结束，使用当前的加载器，否则，抛出异常，通知子加载器进行加载。

​	Class Not Found~

​	null:java 调用不到 C、C++

​	百度：双亲委派机制



## 5.沙箱安全机制

![image-20210722111536514](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722111536514.png)



![image-20210722114035680](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722114035680.png)

![image-20210722114301094](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722114301094.png)





## 6.Native

​    凡是带了native关键字，说明java的作用范围达不到了，回去调用底层C语言的库。

它在内存区域中专门开辟了一块标记区域：Native Method Stack，登记Native方法

​	JNI：会进入本地方法栈，然后调用通过 **JNI **来调用本地方法接口。

​	JNI作用：扩展JAVA的使用，融合不同的编程语言为Java所用，最初是:C、C++







## 7.PC寄存器



程序计数器：Program Counter Register

​	每个线程都有一个程序计数器，是线程私有的，就是一个指针，指向方法区中的方法字节码（用来存储指向一条指令的地址，也即将要执行的指令代码），在执行引擎读取下一条指令，是一个非常小的内存空间，几乎可以忽略不计









## 8.方法区：static,final,Class，常量池



Method Area，方法区

​		方法区是被所有线程共享，所有字段和方法字节码，以及一些特殊方法，如构造函数，接口代码也在此定义，简单说， 所有定义的方法的信息都保存在该区域，此区域属于共享区间。

​		静态变量、常量、类信息(构造方法，接口定义)、运行时的常量池存在方法区中，但是实例变量存在堆内存中，和方法区无关。   

​		p.s:注意jdk1.7和1.8中，在1.8版本中字符串常量池在堆里，运行时常量池在方法区。





 	

## 9.栈

​	栈内存，主管程序的运行，生命周期和线程同步，;线程结束，栈内存也就释放，对于栈来说，不存在 **垃圾回收**问题。

一旦线程结束，栈就Over.

![image-20210722144331730](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722144331730.png)







## 10.三种JVM

​	   (1. Sun公司        	**Java HotSpot(TM) 64-Bit Server VM (build 25.261-b12, mixed mode)**

​		(2.) BEA    **JRockit**

​		(3.) IBM  **J9 VM**



​		学习的都是： HotSpot







## 11.堆

 		Heap,一个JVM只有一个堆内存，堆内存的大小是可以调节的。

​		类加载器读取了类文件后，一般会把什么东西放到堆中？   类、方法、常量、变量，保存我们所有引用类型的真实对象。

​		堆内存中还要细分为三个区域：

​			(1) 新生代   New/Young

​			(2) 老年代   Old
​			(3) 永久区   Perm

![image-20210722151506992](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722151506992.png)

GC垃圾回收，主要是在伊甸园区和养老区(老年代)

​		假设内存满了OutOfMemory(OOM)，堆内存不够  java.lang.OutOfMemoryError:java heap space

​		在JDK8以后，永久存储区改了名，称为**元空间。**







## 12.新生区、老年区

​		![image-20210722154826439](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722154826439.png)

## 13.永久区

![image-20210722155052590](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722155052590.png)

![image-20210722155546080](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722155546080.png)



![image-20210722161446574](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722161446574.png)

 元空间：  逻辑上存在，物理上不存在。

​		

![image-20210722162943356](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722162943356.png)

​		默认情况下：分配的总内存 是电脑内存的 1/4，而初始化的内存是: 1/64

![image-20210722170011944](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722170011944.png)

![image-20210722170059736](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210722170059736.png)



## 14.堆内存调优

​	在一个项目中，突然出现OOM故障，那么该如何排除？研究为什么出错

​		(1) 能够看到代码第几行出错：内存快照分析工具，MAT，Jprofiler

​		(2) Debug：一行行分析代码

​	MAT、Jprofiler 作用：

​		(1) 分析Dump内存文件,快速定位内存泄漏

​		(2) 获得堆中的数据

​		(3) 获得大的对象



-Xms8m -Xmx8m -XX:+HeapDumpOnOutOfMemoryError

解析： -Xms  设置初始化内存分配大小   1/64

​			-Xmx 设置最大分配内存  默认 1/4

​			-XX:+PrintGCDetails    //打印GC垃圾回收信息

​			-XX:+HeapDumpOnOutOfMemoryError     //OOM DUMP

99%(大多数)的垃圾在堆里，需要在堆里进行垃圾回收。

## ![image-20210723110823499](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723110823499.png)

## ![image-20210723111020920](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723111020920.png)

## 15.GC

![image-20210723111006070](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723111006070.png)

### 	（1）常用算法

​					JVM在进行GC时，并不是对着三个区域统一回收，大部分时候，回收的都是新生代

​					1) 新生代

​					2) 幸存区  (from,to)

​					3)老年区

​			GC 两种类：轻 GC （普通的GC :minor GC） ， 重GC (全局GC   :full GC)

​			

题目：



(1) JVM的内存模型和分区，详细到每个分区放什么

​		

(2)堆里面的分区有哪些?    

​		: Eden，from，to，老年区。说说他们的特点。

​		

(3)GC的算法有哪些？	 
标记清除法、标记压缩、复制算法、引用计数法。

如何使用？

 

引用计数法：

![image-20210723112018880](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723112018880.png)

当它计数为0时 将被GC清除





​	复制算法：

![image-20210723133453444](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723133453444.png)



![image-20210723134228418](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723134228418.png)



​	好处： 没有内存碎片

​	坏处：浪费了内存空间 : 多了一半空间永远是 **空 to**，假设对象 100% 存活(极端情况)



复制算法最佳使用场景：对象存活度较低的时候：新生区

 



标记清除法：    

![image-20210723152236471](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723152236471.png)

优点：不需要额外的空间。

缺点：两次扫描，严重浪费时间，会产生内存碎片。



标记压缩算法：   防止内存碎片产生，再次扫描，向一段移动存活的对象，多了一个移动成本



标记清除压缩：

总的来说：    标记  ----- 清除-------压缩

![image-20210723152809295](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723152809295.png)







## 16.JMM (Java Memory Model)

#### Java内存模型——JMM:

 JMM定义了Java 虚拟机(JVM)在计算机内存(RAM)中的工作方式。JVM是整个计算机虚拟模型，所以JMM是隶属于JVM的。从抽象的角度来看，JMM定义了线程和主内存之间的抽象关系：线程之间的共享变量存储在主内存（Main Memory）中，每个线程都有一个私有的本地内存（Local Memory），本地内存中存储了该线程以读/写共享变量的副本。本地内存是JMM的一个抽象概念，并不真实存在。它涵盖了缓存、写缓冲区、寄存器以及其他的硬件和编译器优化。

![img](https://upload-images.jianshu.io/upload_images/4222138-96ca2a788ec29dc2.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)



1.什么是JMM？ 

​	JMM: Java Memory Model 的缩写。



2.它是干嘛的?

​		作用：缓存一致性协议，用于定义数据读写的规则。(遵守，找到这个规则)

JMM定义了线程工作内存和主内存之间的抽象关系：线程之间的共享变量存储在主内存（Main Memory）中，每个线程都有一个私有的本地内存（Local Memory），本地内存中存储了该线程以读/写共享变量的副本。

![image-20210723162837003](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723162837003.png)



解决共享对象可见性的问题：  volatile (不保证原子性,保证可见性，禁止指令重排)



3.它该如何学习：

​		JMM: 抽象的概念、理论

​		JMM对这八种指令的使用，制定了如下规则:

![image-20210723163408392](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723163408392.png)



​	![image-20210723163235215](C:\Users\吴文钦\AppData\Roaming\Typora\typora-user-images\image-20210723163235215.png)





## 17.总结

内存效率：复制算法 > 标记清除算法 > 标记压缩算法 （时间复杂度）

内存整齐度:  复制算法 =标记压缩算法 > 标记清除算法

内存利用率：标记压缩算法=标记清除算法>复制算法



没有最好的算法，只有最合适的算法   GC：分代收集算法



年轻代：

​	（1） 存活率低

​		(2) 复制算法



老年代：

​		(1) 区域大：存活率
​		（2）标记清除（内存碎片不是太多) +标记压缩混合 实现





学习新的东西：

​	(1) netty

​	(2) SpringCloud









































