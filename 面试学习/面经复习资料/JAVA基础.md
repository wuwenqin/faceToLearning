## ==JAVA基础==

### JAVA基本特性

#### 抽象

​	现实生活中的事物被抽象成对象，把具有相同属性和行为的对象被抽象成类，再从具有相同属性和行为的类中抽象出父类。

#### 继承

​	子类和父类之间的继承关系，子类可以获取到父类的属性和方法。

#### 封装

​	隐藏对象的属性和实现细节，仅仅对外公开接口。

#### 多态

​	java语言允许某个类型的引用变量引用子类的实例，而且可以对这个引用变量进行类型转换。同时还有重写，子类可以对父类的方法进行重写，需要保证返回值一致和对应的方法名一致，同时参数不一致。（泛型也算是多态的一种）

#### 跨平台原理

1、首先javac会将对应的.java源文件编译成对应的.class字节码文件。

2、之后，不同的jvm会将对应的.class字节码文件转换成对应操作系统下的机器码，并交给操作系统执行。

<img src="https://img-blog.csdnimg.cn/20200302141617467.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzIzODY0Njk3,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:50%;" />

#### 重写

​	@override，重写是子类对父类的允许访问的方法的实现过程进行重新编写, **形参都不能改变，返回值只能是其派生类**。即外壳不变，核心重写！也就是说子类能够根据需要实现父类的方法。

**重写规则**： 

- 参数列表与被重写方法的参数列表必须完全相同。
- 返回类型与被重写方法的**返回类型可以不相同**，但是必须是父类返回值的派生类（java5 及更早版本返回类型要一样，java7 及更高版本可以不同）。
- 访问权限不能比父类中被重写的方法的访问权限更低。例如：如果父类的一个方法被声明为 public，那么在子类中重写该方法就不能声明为 protected。
- 父类的成员方法只能被它的子类重写。
- 声明为 final 的方法不能被重写。声明为 static 的方法不能被重写，但是能够被再次声明。
- 子类和父类在同一个包中，那么子类可以重写父类所有方法，除了声明为 private 和 final 的方法。子类和父类不在同一个包中，那么子类只能够重写父类的声明为 public 和 protected 的非 final 方法。
- 重写的方法能够抛出任何非强制异常，无论被重写的方法是否抛出异常。但是，重写的方法不能抛出新的强制性异常，或者比被重写方法声明的更广泛的强制性异常，反之则可以。
- 构造方法不能被重写。
- 如果不能继承一个类，则不能重写该类的方法。

#### 重载

​	@overload，重载是在一个类里面，**方法名字相同，而参数不同**。返回类型可以相同也可以不同。**每个重载的方法（或者构造函数）都必须有一个独一无二的参数类型列表**。最常用的地方就是构造器的重载。

- 被重载的方法必须改变参数列表(参数个数或类型不一样)；
- 被重载的方法可以改变返回类型；
- 被重载的方法可以改变访问修饰符；
- 被重载的方法可以声明新的或更广的检查异常；
- 方法能够在同一个类中或者在一个子类中被重载。
- 无法以返回值类型作为重载函数的区分标准。



**java创建对象的方法：**

1、采用new方法，直接创建。

2、采用反射：

- Object ----> getClass();

- 任何数据类型（包括基本数据类型）都有一个“静态”的class属性

- 通过Class类的静态方法：forName（String className）(常用)

  ```
  	//第一种方式获取Class对象  
  		Student stu1 = new Student();//这一new 产生一个Student对象，一个Class对象。
  		Class stuClass = stu1.getClass();//获取Class对象
  	
  	//第二种方式获取Class对象。
  	Student stu2 = new Student();//这一new 产生一个Student对象，一个Class对象。
    Student.class.getName();//采用对应的.class属性获取对象。
  	
  	//第三种方式获取Class对象。
  	String className = "equals.Student";
  	Class stuClass3 = Class.forName(className);
  ```


3、采用反序列化，借助于ObjectOutputStream将对象保存到文件中。

4、采用.clone（）复制实现，





### JDK/JRE/JVM

<img src="https://img-blog.csdn.net/20170314192719335?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvc2luZ2l0/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="img" style="zoom:50%;" />

#### JDK

java development kit 的缩写，意思是JAVA开发工具，其主要包含三部分，

第一部分就是Java运行时环境，**JRE**。

第二部分就是Java的**基础类库**，这个类库的数量还是非常可观的。

第三部分就是**Java的开发工具**，它们都是辅助你更好的使用Java的利器。

#### JRE

​	其中包含了**JAVA虚拟机**（JVM），**运行时类库**（runtime class libraries）和**JAVA应用加载器**（Java application launcher），这些是运行Java程序的必要组件。

#### JVM

​	它是整个java实现跨平台的最核心的部分，所有的java程序会首先被编译为.class的类文件，这种类文件可以在虚拟机上执行，是实现一次编译多处运行的关键。







### 异常/错误：

#### Exception

​	其指的是异常，其是指**当程序出现错误**后，程序如何处理。具体来说，异常机制提供了程序退出的安全通道。当出现错误后，程序执行的流程发生改变，程序的控制权转移到异常处理器。Exception下主要分为两个大类：**RuntimeException（运行时异常）**和**NonRuntimeException（非运行时异常）**。对于异常，一般采用**try{...}catch{...}finally{...}**进行处理。

**RuntimeException(运行时异常)**包括NullPointerException，ClassCastException(类型转换异常)，IndexOutOfBoundsException(越界异常)， IllegalArgumentException(非法参数异常)，ArrayStoreException(数组存储异常)，AruthmeticException(算术异常)，BufferOverflowException(缓冲区溢出异常)等；

<img src="https://img-blog.csdnimg.cn/2019101117003396.jpg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzI5MjI5NTY3,size_16,color_FFFFFF,t_70" alt="img" style="zoom:50%;" />

#### Error

​	其是错误，对于所有的编译时期的错误以及系统错误都是通过Error抛出的。这些错误表示故障发生于虚拟机自身、或者发生在虚拟机试图执行应用时，如**Java虚拟机运行错误（Virtual MachineError）**、**类定义错误（NoClassDefFoundError）**，**内存溢出（OutOfMemoryError）**等。



### JAVA泛型

泛型是在JDK1.5中引入的，泛型使类型（类和接口）在定义类、接口和方法时成为参数，好处在于：

- **强化类型安全**，由于泛型在编译期进行类型检查，从而保证类型安全，减少运行期的类型转换异常。拒绝类似用Object进行继承从而造成运行时错误的情况。
- **提高代码复用**，泛型能减少重复逻辑，编写更简洁的代码。
- **类型依赖关系更加明确**，接口定义更加优好，增强了代码和文档的易读性。

#### 类型擦除：

类型擦除指的是通过类型参数合并，将泛型类型实例关联到同一份字节码上。编译器只为泛型类型生成一份字节码，并将其实例关联到这份字节码上。类型擦除的关键在于从泛型类型中清除类型参数的相关信息，并且再必要的时候添加类型检查和类型转换的方法。 **类型擦除可以简单的理解为将泛型java代码转换为普通java代码，只不过编译器更直接点，将泛型java代码直接转换成普通java字节码**

 类型擦除的**主要过程**如下：**类型检查**----**类型擦除**----**强制类型转换**
   1、将所有的泛型参数用其最左边界（最顶级的父类型）类型替换。（**在泛型类被类型擦除的时候，之前泛型类中的类型参数如果没有指定上限，如\<T>则会被转成普通的Object类型，如果指定了上限如\<T extends String>，则类型参数就会被替换成类型上限，即String。**)
   2、移除所有的类型参数。



三、**类型上下界**：

**<? extends T>**它通过确保类型必须是T的子类来设定类型的上界，

**<? super T>**它通过确保类型必须是T的父类来设定类型的下界



### JAVA基本数据类型

**byte，short，Int，boolean，float，double，long，char**共八种。其与对应的包装类**Byte、Short、Integer、Boolean、Float、Double、Long、Character**的转换被称作**拆箱**和**装箱**。

ps: 0.1在java的表示中用二进制是无法整除的，因此会出现1.0-0.9！=0.1的情况。

#### String：

​	jdk1.8中底层实现是一个Final char[]数组，而且长度固定，在java中有一个方法区保存着一个常量池用来维护对应的String对象。在jdk1.9中，换成了final byte[]数组的形式，同时新加了一个coder的变量，用以判断对应的编码的方式。

#### StringBuffer：

​	**多线程**下的char数组，采用**Synchronized**进行了互斥访问，保证了多线程下的并发安全。

#### StringBuilder：

​	**单线程**下的char数组，可以插入新的字符，但其非线程安全的。

**Object类基本方法**：(https://fangjian0423.github.io/2016/03/12/java-Object-method/)

1、**wait()/notify()/notifyAll()**，主要用于线程通信阻塞和唤醒。；

2、**toString（）**，该方法在打印对象时被调用，将对象信息变为字符串返回，默认输出对象地址。

3、**equals（）**，比较两个对象的地址。

4、**hashCode（）**，该方法会返回对象的内存地址(但在java中不是这么实现的)，常会和equals方法同时重写，确保相等的两个对象拥有相等的哈希值。**hashcode在String类中被重写过：以“abc”为例子，hashcode的计算方式为a\*31^2^+b\*31^1^+c*31^0^，这里的a，b，c代表对应字母的Ascii码。采用31为幂的原因主要在于，31可以被编译器优化成左移5位后减1，有较高的性能**![image-20210407203706788](/Users/XYJ/Desktop/面经复习文件/image-20210407203706788.png)

**ps**：如果重写equals（）那么必须对应的重写hashCode（）代码，原因在于Object中的hashCode方法，是直接返回对应对象的虚拟地址，由此会产生两个对象所存储的类数据都相同即采用equals的时候结果相同，但是却得不出一样的hashcode（），就会导致差异性。

### 引用类型

#### 1、强引用

​	是使用最普遍的引用。如果一个对象具有强引用，那**垃圾回收器**绝不会回收它

#### 2、软引用

​	如果一个对象只具有**软引用**，则**内存空间充足**时，**垃圾回收器**就**不会**回收它；如果**内存空间不足**了，就会**回收**这些对象的内存，**软引用**可以和一个**引用队列**(`ReferenceQueue`)联合使用。如果**软引用**所引用对象被**垃圾回收**，`JAVA`虚拟机就会把这个**软引用**加入到与之关联的**引用队列**中。

```java
 // 软引用
    String str = new String("abc");
    SoftReference<String> softReference = new SoftReference<String>(str);
```

#### 3、弱引用

与**软引用**的区别在于：只具有**弱引用**的对象拥有**更短暂**的**生命周期**。

    String str = new String("abc");
    WeakReference<String> weakReference = new WeakReference<>(str);
    str = null;

#### 4、虚引用

​	顾名思义，就是**形同虚设**。与其他几种引用都不同，**虚引用**并**不会**决定对象的**生命周期**。如果一个对象**仅持有虚引用**，那么它就和**没有任何引用**一样，在任何时候都可能被垃圾回收器回收。；

#### 对象引用：

主要的实现方式有两种，分别是**句柄引用**和**直接指针**。

<img src="https://images2015.cnblogs.com/blog/592743/201603/592743-20160319235555303-769658219.jpg" alt="img" style="zoom:75%;" />

### 拷贝

#### 浅拷贝

浅拷贝是按位拷贝对象，它会创建一个新对象，这个对象有着原始对象属性值的一份精确拷贝。如果属性是基本类型，拷贝的就是基本类型的值；如果属性是内存地址（引用类型），拷贝的就是内存地址 ，因此如果其中一个对象改变了这个地址，就会影响到另一个对象。

(1) 对于基本数据类型的成员对象，是直接将属性值赋值给新的对象。基础类型的拷贝，其中一个对象修改该值，不会影响另外一个。
 (2) 对于引用类型，比如数组或者类对象，浅拷贝只是把内存地址赋值给了成员变量，它们指向了同一内存空间。改变其中一个，会对另外一个也产生影响。

#### 深拷贝

​	在拷贝引用类型成员变量时，为引用类型的数据成员另辟了一个独立的内存空间，实现真正内容上的拷贝。

(1) 对于基本数据类型的成员对象，所以是直接将属性值赋值给新的对象。基础类型的拷贝，其中一个对象修改该值，不会影响另外一个（和浅拷贝一样）。
 (2) 对于引用类型，比如数组或者类对象，深拷贝会新建一个对象空间，然后拷贝里面的内容，所以它们指向了不同的内存空间。改变其中一个，不会对另外一个也产生影响。
 (3) 对于有多层对象的，每个对象都需要实现 `Cloneable` 并重写 `clone()` 方法，进而实现了对象的串行层层拷贝。
 (4) 深拷贝相比于浅拷贝速度较慢并且花销较大。

#### 对象拷贝

​	是直接将某个对象的内存地址赋值到另一个对象中，从而实现对象的拷贝。

### [JAVA三大集合类](https://blog.csdn.net/weixin_39549899/article/details/114223293)

#### List集合

##### ArrayList

​	其采用数组实现，检索元素的速度较快。扩容是扩大约原本容量的1.5倍。

```java
int newCapacity = oldCapacity + (oldCapacity >> 1);
```

在扩容后会采用Arrays.copyOf()方法将原数组中的数组复制过来。

- remove方法
  该方法将被删除位置后的元素**向前复制**，底层调用的也是System.arrayCopy()方法，复制完成后，将数组元素的最后一个设置为null（因为向前复制一个位置，所以最后位置的元素是重复的），这样就解决了复制重复元素的问题

##### LinkedList

​	采用双向链表实现，每个节点为Node有pre和next属性，插入删除的速度较快。

##### Vector

​	其是ArrayList的改进版本，其采用Synchronized加锁的方式保证了线程安全。

#### Map集合

##### hashmap

​	hashmap采用**Node数组+链表**的结构（1.7引入了红黑树加快了检索的速度），以key-value的形式存储数据，解决冲突的方式主要是链表法。由于采用了**头插法**，会产生死循环和数据覆盖等不安全的情况。（在jdk1.8中采用了尾插法，避免了死循环的出现）。**get()方法**流程大致为: 首先判断当前的key是否为空，如果为空则对应的key=0，否则采用rehash的方式计算对应的index值。再判断当前的数据结构是链表还是红黑树，然后依次采用.equals()比较并得到最后的结果。

```java
   	transient Node<K,V>[] table; //Node数组,Node实现了Entry接口，本质上也是Entry.
		transient Set<Map.Entry<K,V>> entrySet;//Entry对象,
		public V get(Object key) {//获取数组对象
        Node<K,V> e;
        return (e = getNode(hash(key), key)) == null ? null : e.value;
    }
		final Node<K,V> getNode(int hash, Object key) {//get方法的源代码
        Node<K,V>[] tab; Node<K,V> first, e; int n; K k;
        if ((tab = table) != null && (n = tab.length) > 0 &&
            (first = tab[(n - 1) & hash]) != null) { //这行计算
            if (first.hash == hash && // always check first node
                ((k = first.key) == key || (key != null && key.equals(k))))
                return first;
            if ((e = first.next) != null) {
                if (first instanceof TreeNode)
                    return ((TreeNode<K,V>)first).getTreeNode(hash, key);
                do {
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        return e;
                } while ((e = e.next) != null);
            }
        }
        return null;
}
```



​	**put()方法**流程则为：先采用hashCode()计算对应的hashcode值**（通过获取内存的值）**，再通过**（hashcode & length-1）**得到对应的index值，再按照红黑树或链表的方式加入到对应的index下标的元素中。并在添加后判断是否转换成红黑树以及是否需要扩容，如果需要则进行转换或扩容操作。

```java
    public V put(K key, V value) {
        return putVal(hash(key), key, value, false, true);
    }
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {//putval的主体内容
        Node<K,V>[] tab; Node<K,V> p; int n, i;
        if ((tab = table) == null || (n = tab.length) == 0)
          //如果为空或者长度为0，进行resize（）因此可以猜想到resize()是类似构建表的操作。
            n = (tab = resize()).length;
        if ((p = tab[i = (n - 1) & hash]) == null)//i=(n-1) & hash 哈希计算，找到对应的Node节点
            tab[i] = newNode(hash, key, value, null);
        else {
            Node<K,V> e; K k;
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))//如果第一个就是对应节点
                e = p;
            else if (p instanceof TreeNode)//如果是红黑树
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            else {
                for (int binCount = 0; ; ++binCount) {
                    if ((e = p.next) == null) {//如果发现当前的节点是空则尾部插入
                        p.next = newNode(hash, key, value, null);
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                      //否则修改对应的值,细节是能够==负责比较基础数据类型，equals负责比较引用对象类型。
                        break;
                    p = e;
                }
            }
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)//在插入后还会去判断是否可以扩容
            resize();
        afterNodeInsertion(evict);
        return null;
    }	
```

**注意点**：每次扩容的大小是**2倍**，`(newCap = oldCap << 1)`，一是因为位运算较快，二是因为在rehash的过程中，哈希函数依赖于数组长度为2的倍数来分散对应的节点位置，进而减少冲突。比如当前的数组长度为4，二进制为100，要插入一个2的hashcode的话，index= 010 & 100 = 0；对hashcode=3的情况 ，index= 011&100 = 0，两个index都为0，就发生了冲突。而如果采用length-1作为哈希过程，结果就会是 index2 = 010 & 011 = 010=2。index3 = 011 & 011=011 = 3，就很好的解决了冲突的问题。(但在jdk1.7中直接采用hashcode进行计算。) 具体的resize的代码如下：

```java
  final Node<K,V>[] resize() {
        Node<K,V>[] oldTab = table;
        int oldCap = (oldTab == null) ? 0 : oldTab.length;
        int oldThr = threshold;
        int newCap, newThr = 0;
        if (oldCap > 0) {
            if (oldCap >= MAXIMUM_CAPACITY) {//如果旧大小已经达到最大则返回
                threshold = Integer.MAX_VALUE;
                return oldTab;
            }
            else if ((newCap = oldCap << 1) < MAXIMUM_CAPACITY &&
                     oldCap >= DEFAULT_INITIAL_CAPACITY)
              //如果新长度小于最大长度，同时旧长度大于默认长度,则修改对应的阈值
                newThr = oldThr << 1; 
        }
        else if (oldThr > 0) 
            newCap = oldThr;
        else {               // 如果是初始创建的resize()
            newCap = DEFAULT_INITIAL_CAPACITY;
            newThr = (int)(DEFAULT_LOAD_FACTOR * DEFAULT_INITIAL_CAPACITY);
        }
        if (newThr == 0) {//设置新的阈值,默认max(Integer.MAX_VALUE,容量*负载因子);
            float ft = (float)newCap * loadFactor;
            newThr = (newCap < MAXIMUM_CAPACITY && ft < (float)MAXIMUM_CAPACITY ?
                      (int)ft : Integer.MAX_VALUE);
        }
        threshold = newThr;
        @SuppressWarnings({"rawtypes","unchecked"})
        Node<K,V>[] newTab = (Node<K,V>[])new Node[newCap];
        table = newTab;
        if (oldTab != null) {
            for (int j = 0; j < oldCap; ++j) {
                Node<K,V> e;
                if ((e = oldTab[j]) != null) {
                    oldTab[j] = null;
                  //重新哈希的过程
                    if (e.next == null)
                        newTab[e.hash & (newCap - 1)] = e;
                    else if (e instanceof TreeNode)
                      //树节点情况下的重新扩容
                        ((TreeNode<K,V>)e).split(this, newTab, j, oldCap);
                    else { 
                      //链表情况下的重新扩容
                        Node<K,V> loHead = null, loTail = null;
                        Node<K,V> hiHead = null, hiTail = null;
                        Node<K,V> next;
                        do {
                            next = e.next;
                            if ((e.hash & oldCap) == 0) {//十分巧妙的一步
                              //如果为0则此时不需要移动该元素，因为hash后的位置一致.
                                if (loTail == null)
                                    loHead = e;
                                else
                                    loTail.next = e;
                                loTail = e;
                            }
                            else {
                              //否则会是当前的位置的元素移动一定的距离.
                                if (hiTail == null)
                                    hiHead = e;
                                else
                                    hiTail.next = e;
                                hiTail = e;
                            }
                        } while ((e = next) != null);
                        if (loTail != null) { 
                            loTail.next = null;
                            newTab[j] = loHead;
                        }
                        if (hiTail != null) {
                          //对应于上面的结论.
                            hiTail.next = null;
                            newTab[j + oldCap] = hiHead;
                        }
                    }
                }
            }
        }
        return newTab;
    }
```

遍历hashmap的两种方式。

```java
//第一种直接获取对应的entry对象 
Iterator<Map.Entry<String, Integer>> entryIterator = map.entrySet().iterator();
     while (entryIterator.hasNext()) {
       Map.Entry<String, Integer> next = entryIterator.next();
       System.out.println("key=" + next.getKey() + " value=" + next.getValue());
     }

//第二种获取key，再通过key去访问对应的对象。iterator采用了快速失败的机制。
 Iterator<String> iterator = map.keySet().iterator();
     while (iterator.hasNext()){
      String key = iterator.next();
      System.out.println("key=" + key + " value=" + map.get(key));
    }
```

hashmap的一些关键参数：

```
DEFAULT_INITIAL_CAPICITY = 1<<4; 默认大小为16
MAXIMUM_CAPACITY = 1<< 30; 最大容量
DEFAULT_LOAD_FACTOR = 0.75f; 默认负载因子
TREEIFY_THRESHOLD = 8; 
UNTREEIFY_THRESHOLD = 6; 树化和退化为链表的阈值，不采用7的原因是避免频繁的转换
MIN_TREEIFY_CAPACITY = 64; 链表转化为红黑树时需要的数组大小
threshold 表示扩用的阈值，大小为 数组大小*负载因子
```

##### hashtable

hashtable是hashmap的线程安全版本，采用**Synchronized**的方式进行上锁，性能不如Concurrenthashmap。需要注意⚠️，hashtable和ConcurrentHashmap都不允许插入空键和值，而hashmap则允许插入，因为在java中hashtable和Concurrenthashmap**不能使用contains的方式判断当前是否包含这个键值，从而无法判断当前的key是空还是不存在。**其判断两个元素是否相同的方式是：

1. 判断两个对象先按照hashCode()计算出来的哈希值是否相同；
2. 再采用equals（）来判断对应的元素是否相同。

```java
public synchronized V put(K key, V value) {//采用Synchronized进行同步
        if (value == null) {//不允许值为空
            throw new NullPointerException();
        }

        Entry<?,?> tab[] = table;
        int hash = key.hashCode();
        int index = (hash & 0x7FFFFFFF) % tab.length;
        @SuppressWarnings("unchecked")
        Entry<K,V> entry = (Entry<K,V>)tab[index];
        for(; entry != null ; entry = entry.next) {
            if ((entry.hash == hash) && entry.key.equals(key)) {//判断相同的方式
                V old = entry.value;
                entry.value = value;
                return old;
            }
        }
        addEntry(hash, key, value, index);
        return null;
    }
```

##### concurrenthashmap

​	其基本的架构同hashmap类似，不同的是在线程安全上，concurrenthashmap采用分段锁的机制。jdk1.7以前，基本结构为**Segment+HashEntry+链表**的形式，通过对每个Segment进行上锁来保证高并发。

<img src="https://ss.csdn.net/p?https://mmbiz.qpic.cn/mmbiz_png/QCu849YTaIPf1sDCN5zcDdGsibZwyzy9rmnTSzibQ6VEBXUhicBWHFae47ShkNzCRB7SZibuUN6gDmGkfeB5saAMQQ/640?wx_fmt=png" alt="640?wx_fmt=png" style="zoom:80%;" />

​	而在jdk1.8中采用Node数组+链表的形式，用**Node节点**代替了原有的segment结构，简化了结构。在putVal方法中采用**CAS+Synchronized**来进行上锁的操作，在Node为空或者是第一个的情况下，采用CAS进行修改，而在进入链表后就需要采用Synchronized进行Node加锁的操作。这样做的理由也很简单，因为不安全的情况出现在第一个节点后的链表中，因此在不进入链表的时候采用轻量锁就可以了。Node的定义如下：

```java
static class Node<K,V> implements Map.Entry<K,V> {
        final int hash;
        final K key;
        volatile V val;
        volatile Node<K,V> next;
        Node(int hash, K key, V val) {
            this.hash = hash;
            this.key = key;
            this.val = val;
        }
        Node(int hash, K key, V val, Node<K,V> next) {
            this(hash, key, val);
            this.next = next;
        }
        public final K getKey()     { return key; }
        public final V getValue()   { return val; }
        public final int hashCode() { return key.hashCode() ^ val.hashCode(); }
        public final String toString() {
            return Helpers.mapEntryToString(key, val);
        }
        public final V setValue(V value) {
            throw new UnsupportedOperationException();
        }
        public final boolean equals(Object o) {//重写了Node的equals,因此必须要重写hashcode
            Object k, v, u; Map.Entry<?,?> e;
            return ((o instanceof Map.Entry) &&
                    (k = (e = (Map.Entry<?,?>)o).getKey()) != null &&
                    (v = e.getValue()) != null &&
                    (k == key || k.equals(key)) &&
                    (v == (u = val) || v.equals(u)));
        }
        Node<K,V> find(int h, Object k) {
            Node<K,V> e = this;
            if (k != null) {
                do {
                    K ek;
                    if (e.hash == h &&
                        ((ek = e.key) == k || (ek != null && k.equals(ek))))
                        return e;
                } while ((e = e.next) != null);
            }
            return null;
        }
    }
```

重要参数：

```java
    private static final int MAXIMUM_CAPACITY = 1 << 30; //最大容量是2^31
    private static final int DEFAULT_CAPACITY = 16;//初始长度为16
```





##### Treemap

​	其底层基于**哈希数组+红黑树**的结构进行实现，TreeMap的特点在于，你得到的结果是经过排序的。TreeMap是唯一的带有subMap()方法的Map，它可以返回一个子树。hash数组的默认大小是**11**,当hash数组的容量超过初始容量**0.75**时,增加的方式是**old*2+1**。

##### LinkedHashMap

​	其通过维护一个额外的**双向链表**保证了迭代顺序。特别地，该迭代顺序可以是插入顺序，也可以是访问顺序。因此，根据链表中元素的顺序可以将LinkedHashMap分为：保持插入顺序的LinkedHashMap 和 保持访问顺序的LinkedHashMap，其中LinkedHashMap的默认实现是按插入顺序排序的。

#### Set集合

##### hashset

​	其属于无序集合其hashset底层与hashmap类似，其保持唯一性的方式是先通过hashCode（）比较对应的哈希值是否相同，接着采用equal（）方法比较两个对象是否一致。初始容量16，负载因子为0.75，

##### TreeSet

​	属于有序集合，其底层与TreeMap一致，采用红黑树进行实现。

##### LinkedHashSet

​	按放入顺序有序不重复。



#### 快速失败机制（fail-fast）：

在用迭代器遍历一个集合对象时，如果遍历过程中对集合对象的内容进行了修改（增加、删除、修改），则会抛出 Concurrent Modification Exception。

**原理：**迭代器在遍历时直接访问集合中的内容，并且在遍历过程中使用一个 modCount 变量。集合在被遍历期间如果内容发生变化，就会改变 modCount 的值。每当迭代器使用 hashNext()/next() 遍历下一个元素之前，都会检测 modCount 变量是否为 expectedmodCount 值，是的话就返回遍历；否则抛出异常，终止遍历。

**注意：**这里异常的抛出条件是检测到 **modCount != expectedmodCount** 这个条件。如果集合发生变化时修改 modCount 值刚好又设置为了 expectedmodCount 值，则异常不会抛出。因此，不能依赖于这个异常是否抛出而进行并发操作的编程，这个异常只建议用于检测并发修改的 bug。

**场景：**java.util 包下的集合类都是快速失败的，不能在多线程下发生并发修改（迭代过程中被修改）。

#### 安全失败机制（fail—safe）

采用安全失败机制的集合容器，在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在拷贝的集合上进行遍历。

**原理：**由于迭代时是对原集合的拷贝进行遍历，所以在遍历过程中对原集合所作的修改并不能被迭代器检测到，所以不会触发 Concurrent Modification Exception。

**缺点**：基于拷贝内容的优点是避免了 Concurrent Modification Exception，但同样地，迭代器并不能访问到修改后的内容，即：迭代器遍历的是开始遍历那一刻拿到的集合拷贝，在遍历期间原集合发生的修改迭代器是不知道的。

**场景：**java.util.concurrent 包下的容器都是安全失败，可以在多线程下并发使用，并发修改。



### [类加载](https://blog.csdn.net/weixin_40236948/article/details/88072698)

​	我们编写的java文件都是保存着业务逻辑代码。java编译器将 .java 文件编译成扩展名为 .class 的文件。.class 文件中保存着.java文件转换后，虚拟机将要执行的指令。当需要某个类的时候，java虚拟机会加载 .class 文件，并创建对应的class对象，将class文件加载到虚拟机的内存，这个过程被称为类的加载，主要流程如下所示。

<img src="https://img-blog.csdnimg.cn/20190302102035338.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDIzNjk0OA==,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:50%;" />

##### 加载

​	在加载阶段，**ClassLoader通过一个类的完全限定名查找此类字节码文件，并将这个字节码文件的静态数据结构转换成对应的运行时数据结构，并利用字节码文件创建一个class对象**。加载的时机主要如下：

- 遇到**new、getstatic、putstatic或invokestatic**这四个字节码的时候，会进行类的加载。
- 使用**反射方式**创建某个类或者接口对象的Class对象，会进行加载。
- 初始化某个类的子类，如果父类没有加载，则进行加载（双亲委派机制）。
- 虚拟机启动时，需要指定一个执行的主类进行加载。
- 使用JDK1.7的新加入的动态语言支持的时候，如果一个MethodHandle实例的最后解析结果为：REF_getStatic、REF_putStatic、REF_invokeStatic、REF_newInvokeSpecial

实现自定义类加载器主要有两步。

1、继承ClassLoader
2、重写findClass，在findClass里获取类的字节码，并调用ClassLoader中的defineClass方法来加载类，获取class对象。代码如下：

```java
public static class MyClassLoader  extends  ClassLoader{
        @Override
        protected Class<?> findClass(String name) throws ClassNotFoundException {
            byte[] data=null;
            try {
                 data= loadByte(name);
            } catch (IOException e) {
                e.printStackTrace();
            }
            return this.defineClass(data,0,data.length);
        }
        private byte[] loadByte(String name) throws IOException {
            File file = new File("/Users/admin/test/"+name);
            FileInputStream fi = new FileInputStream(file);
            int len = fi.available();
            byte[] b = new byte[len];
            fi.read(b);
            return b;
        }
    }

//待加载的类
public class Demo{
	public void say(){
		System.out.println("hello");
	}
}
MyClassLoader classLoader = new MyClassLoader();
Class clazz = classLoader.loadClass("Demo.class");
Object o = clazz.newInstance();
Method method = clazz.getMethod("say");	//反射
method.invoke(o);
```

###### 双亲委派

​	双亲委派模型**要求除了顶层的启动类加载器之外，其余的类加载器都应该有自己的父类加载器，但是在双亲委派模式中父子关系采取的并不是继承的关系，而是采用组合关系来复用父类加载器的相关代码**。双亲委派模式的好处是：

1、Java类随着它的类加载器一起具备一种带有优先级的层次关系，通过这种层级关系可以**避免类的重复加载**，当父亲已经加载了该类的时候，就没有必要子类加载器（ClassLoader）再加载一次。

2、是考虑到安全因素，Java核心API中定义类型不会被随意替换。

###### 线程上下文类加载器

​	在Java应用中存在着很多服务提供者接口，这些接口允许第三方为它们提供实现，如常见的 SPI 有 JDBC、JNDI等，这些 SPI 的接口属于 Java 核心库，一般存在rt.jar包中，由Bootstrap类加载器加载，而 SPI 的第三方实现代码则是作为Java应用所依赖的 jar 包被存放在classpath路径下，由于SPI接口中的代码经常需要加载具体的第三方实现类并调用其相关方法，但SPI的核心接口类是由引导类加载器来加载的，而Bootstrap类加载器无法直接加载SPI的实现类，同时由于双亲委派模式的存在，Bootstrap类加载器也无法反向委托AppClassLoader加载器SPI的实现类。在这种情况下，我们就需要一种特殊的类加载器来加载第三方的类库，而**线程上下文类加载器**就是很好的选择。

<img src="https://img-blog.csdn.net/20170625231013755?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvamF2YXplamlhbg==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="img" style="zoom:67%;" />

##### 验证

​	验证的原因在于，字节码是可以伪造的。因此验证目的在于确保class文件的字节信息中包含信息符合当前虚拟机要求，不会危害虚拟机自身的安全，主要包括四种验证：

​	**文件格式验证**：主要负责校验当前的.class文件是否符合对应的字节码规范。

​	**元数据校验**：主要对字节码中的数据进行语义分析，以确保符合Java的规定。

​	**字节码校验**：这个阶段是最复杂的一个阶段，该阶段通过数据流分析和控制流分析，以确保程序的语义符合逻辑。但即使程序经过了字节码校验，也不能保证这个程序就一定是不存在bug的。

​	**符号引用校验**：这个阶段发生在将符号引用转换为直接引用的时候发生的。主要校验的内容有通过全限定名是否能找到对应的类，可访问性是否可以访问（private、public等）。

##### 准备

​	为类中定义的static变量**分配内存并且设置该类变量的初始值**，该类变量通常会分配在方法区中，这里不包含final修饰的static ，因为final在编译的时候就已经分配了。**在jdk1.8后，类变量就会随着Class对象一起存放到JAVA堆中了。**这里不会为实例变量分配初始化，类变量会分配在方法区中，实例变量会随着对象分配到Java堆中。（需要注意的是，除了final修饰的变量，其余在这个阶段的静态变量的值是0，而不是对应的初始值。）

##### 解析

​	这里主要的任务是把**常量池中的符号引用替换成直接引用。**符号引用指的是以一组符号来描述对应的目标，而直接引用则是指直接指向目标的指针。如果此时对应的引用还没有生成，则也需要进行加载。

##### 初始化

​	这里是类加载的最后阶段，如果该类具有父类就进行对父类进行初始化，执行其静态初始化器（静态代码块）和静态初始化成员变量。（前面已经对static 初始化了默认值，这里我们对它进行赋值，成员变量也将被初始化）



### JAVA多线程

**线程安全**：代码会通过同步机制保证各个线程都可以正常且正确的执行，不会出现数据污染等意外情况。

线程的实现方式主要有三种：1、**内核线程实现**(1:1)；2、**使用用户线程实现**(1:N)；3、**用户线程+轻量级进程实现**(N:M)

线程创建的方法有四种：

#### 1、**继承Thread类**。

（java只允许单类继承，因此一般采用实现的接口的方式会更好。）

```java
class mythread extends Thread{
  @override
  public void run(){...}
}
```

#### 2、实现Runnable接口

```java
class mythread implements Runnable{
  @override
  public void run(){...}
}
```

#### 3、实现Callable接口

​	相较于Runnable接口，**Callable接口可以返回值，且可以抛出异常。**

```java
class myThread1 implements Callable {
  @Override
  public Object call() throws Exception {...}
}
```

#### 4、采用线程池进行创建

​	Java通过Executors（jdk1.5的concurrent包中）提供四种线程池，核心创建代码如下。

```java
//1、创建一个长度不限的线程池，如果线程池存在时间超过设定，则可灵活回收空闲线程。
ExecutorService newExecutorService = Executors.newCachedThreadPool();

//2、创建一个固定数量线程池,可控制线程最大并发数，超出的线程会在队列中等待。
ExecutorService newExecutorService = Executors.newFixedThreadPool(3);

//3、创建一个定时长线程池，支持定时及周期性任务执行。
ScheduledExecutorService newScheduledThreadPool = Executors.newScheduledThreadPool(5);

//4、创建一个单线程化的线程池，它只会用唯一的工作线程来执行任务，保证所有任务按照指定顺序(FIFO, LIFO, 优先级)执行。
ExecutorService newSingleThreadExecutor = Executors.newSingleThreadExecutor();

//线程池执行代码。当然也可以不采用匿名类的方法，而是采用之前 继承Thread类/实现Runnable接口的线程。
newExecutorService.execute(new Runnable() {
  @Override
  public void run() {...}
});
```

#### 线程生命周期

<img src="https://img-blog.csdnimg.cn/2020123013280490.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3RhbzQ0MTAzMzYxOA==,size_16,color_FFFFFF,t_70" alt="线程状态转换" style="zoom:90%;" />

线程的生命周期主要是**创建(new )、就绪（采用start的时候处于就绪状态）、运行(.run处于运行状态)、等待(.wait进入阻塞状态)、计时等待、死亡**，六个状态。



#### 线程同步：==?待补充==

实现线程同步的方法：

1、volatile关键字。

2、lock关键字。

3、synchronized关键字。

4、ThreadLocal关键字，总的来说是为每个线程创建一个变量，从而避免冲突。

5、BlockQueue，阻塞队列。

6、AtomicInteger，原子整型类。



### 线程池

**三大优点：**

1、**降低资源消耗**：通过重复利用现有的线程来执行任务，避免多次创建和销毁线程。

2、**提高响应速度**：因为省去了创建线程这个步骤，所以在拿到任务时，可以立刻开始执行。

3、**提供附加功能**：线程池的可拓展性使得我们可以自己加入新的功能，比如说定时、延时来执行某些线程。

<img src="https://s4.51cto.com/wyfs02/M01/9B/4A/wKioL1lg5nGjTm-5AAtWWU6jVhw052.png-wh_500x0-wm_3-wmp_4-s_2683155803.png" alt="wKioL1lg5nGjTm-5AAtWWU6jVhw052.png-wh_50" style="zoom:150%;" />

#### 线程池七大核心参数：

##### 1、**核心线程数**

​	指的是线程池核心线程的数目，核心线程不同于普通线程，其完成任务后不会被回收而是等待下一次执行任务。

##### 2、**最大线程数**

​	顾名思义，指的是线程池最多允许产生的线程数目。

##### 3、**线程存活时间**

​	线程允许存活的时间，通常是个数字。

##### 4、**线程存活时间单位**

​	定义线程的存活时间单位是毫秒、秒、分、小时等。

##### 5、**阻塞队列**

​	主要分为三大类，**无界队列、有界队列、同步移交队列**。

- 无界队列/有界队列：

  （1）**DelayQueue**, （延期阻塞队列，实现了BlockingQueue接口） 这个队列是无界的，并且没有指定长度的构造方法 

  （2）**ArrayBlockingQueue**, （基于数组的并发阻塞队列） 必须设置长度，遵循先进先出的原则。

  （3）**LinkedBlockingQueue**, （基于链表的FIFO阻塞队列） 没有指定长度就是有界的反之是有界的，使用该队列做为阻塞队列时要尤其当心，当任务耗时较长时可能会导致大量新任务在队列中堆积最终导致**OOM**

  （4）**LinkedBlockingDeque**, （基于链表的FIFO双端阻塞队列） 没有指定长度就是有界的反之是有界的 

  （5）**PriorityBlockingQueue**, （带优先级的无界阻塞队列） 这个只能传入Comperable接口的类型，不是有界的 ，可以自定义优先级。

- 同步移交队列：

  （1）**SynchronousQueue** ，（并发同步阻塞队列）不能指定长度，只能传入一个值，有界。不是一个真正的队列，而是一种线程之间移交的机制。

  （2）**ArrayDeque**, （数组双端队列） 

  （3）**PriorityQueue**, （优先级队列） 

  （4）**ConcurrentLinkedQueue**, （基于链表的并发队列） 

##### 6、线程工厂

​	采用了工厂的设计模式，可以使得线程具有相同的特性，方便我们创建对应的线程，以及监视线程的状态等；

##### 7、拒绝策略

主要用于在阻塞队列已满，同时线程数达到最大线程数的时候，对任务的处理方式，共四种拒绝策略：

​	（1）**ThreadPoolExecutor.AbortPolicy:**丢弃任务并抛出RejectedExecutionException异常。 主要用于关键的功能模块。

​	（2）**ThreadPoolExecutor.DiscardPolicy**：丢弃任务，但是不抛出异常。可以用于一些非关键的功能模块。

​	（3）**ThreadPoolExecutor.DiscardOldestPolicy**：丢弃队列最前面的任务，然后重新提交被拒绝的任务 。在一些对时间有要求的任务上可以采用。

​	（4）**ThreadPoolExecutor.CallerRunsPolicy**：由调用线程（提交任务的线程）处理该任务

**核心线程设置原则：**

**IO密集型任务**，对于该类任务，线程数是越多越好，但过多的线程会过度损耗CPU的资源，因此通常采用2*CPU核心数的线程数目。

**CPU密集型任务**（计算密集型任务），对于该类任务，只需要让CPU的各个核心都能被利用即可，同时要多出一个线程用于IO操作，因此线程数为：CPU核心数+1。

**线程池的优点：**1）降低资源消耗，减少了频繁创建线程的消耗；2）提高响应速度，直接将线程进行分配，不必再等待创建；3）提高线程的可管理性，会对被使用完成的线程进行回收，用于下次使用。

**线程方法**：

- **wait()/notify()/notifyall()**：属于object基类下的一个方法，主要用于线程的通信，唤醒对应的线程，在调用的时候会释放对应的锁。
- **sleep()**：其属于Thread类下的一个静态方法，在调用的时候需要传入对应的参数，线程会根据传入的参数沉睡相应的秒数，不会释放对应的锁。
- **join()**：join() 定义在Thread.java中。其让当前占用CPU资源的“主线程”等待“子线程”结束之后才能继续运行。主要作用是**同步**，它可以使得线程之间的**并行执行变为串行执行**。在A线程中调用了B线程的join()方法时，表示只有当B线程执行完毕时，A线程才能继续执行。本质上也是采用wait方法，让主线程等待子线程完成。(ps: **join()方法必须在线程start()方法调用之后调用才有意义**)

主要代码：

```java
  public final synchronized void join(long millis)
    throws InterruptedException {
        // 在循环中不断检测当前线程（B线程）是否活着
        while (isAlive()) {
            // 如果或者，调用者就在当前线程（B线程）对象上等待
            wait(0);
        }
    }
```



- **Start()：**启动一个线程使其进入就绪状态，真正实现了多线程运行，这时主线程无需等待run方法体代码执行完毕而直接继续执行下面的代码。
- **Run()：**线程的执行体，run（）方法可以当作普通方法的方式调用，程序还是要顺序执行，还是要等待run方法体执行完毕后才可继续执行下面的代码，因此本质上直接调用Run方法没有使用到多线程。



### ThreadLocal

​	ThreadLocal中填充的变量属于**当前**线程，该变量对其他线程而言是隔离的。ThreadLocal为变量在每个线程中都创建了一个副本，那么每个线程可以访问自己内部的副本变量。

**原理**：其主要通过维护一个Map，以Thread作为Key，而对应的值作为Value，从而对每个线程维护了一个唯一的副本，从而使得线程间的访问不会出现问题。需要注意的是ThreadLocal是一个**弱引用**，会在被设置为null或空间不足的时候被回收。早期**jdk1.5中的设计**如下，这么做有一个弊端：**当线程回收时，该线程绑定的变量不能被自动的回收，因为变量存储在 ThreadLocal 里，必须显式的去回收。**

<img src="https://img-blog.csdnimg.cn/img_convert/e44d0f40ad4957c08410b883cb5d1180.png" alt="e44d0f40ad4957c08410b883cb5d1180.png" style="zoom:80%;" />



**JDK 1.8 的设计**，每个 Thread 维护一个 ThreadLocalMap，这 map 的 key 是 **ThreadLocal** 实例本身，value 才是真正要存储的变量值。不同的**ThreadLocal**对应线程不同的变量副本。

<img src="https://img-blog.csdnimg.cn/img_convert/63b044745bd6fb475069c2a216c0c864.png" alt="63b044745bd6fb475069c2a216c0c864.png" style="zoom:80%;" />

hashmap与ThreadLocalMap十分类似，但在解决冲突上，HashMap 使用的拉链法，而 ThreadLocalMap 使用的**线性探测法**。对于父子线程如何共享变量的问题，主要使用 **InheritableThreadLocal** 来解决。

**应用场景：**

1、在进行对象跨层传递的时候，使用ThreadLocal可以避免多次传递，打破层次间的约束。

2、线程间数据隔离

3、进行事务操作，用于存储线程事务信息。

4、数据库连接，Session会话管理。

**问题**：存在**内存泄漏**的可能性，如果突然我们ThreadLocal被设置为null了，也就是要被垃圾回收器回收了，但是此时我们的ThreadLocalMap生命周期和Thread的一样，它不会回收，这时候就出现了一个现象。那就是ThreadLocalMap的key没了，但是value还在，这就造成了**内存泄漏**。**解决办法**是使用完ThreadLocal后，显式执行remove操作，删除对应的ThreadLocal键和对应的变量副本，避免出现内存泄漏情况。

<img src="https://pics3.baidu.com/feed/91ef76c6a7efce1b563edc5501a900dbb58f6512.jpeg?token=a6acac56e087a9c1581a7acfc867015d&s=A642F210061F6DCA0AF341C5030030BB" alt="img" style="zoom: 67%;" />



### JAVA的锁分类

**（1）悲观锁**（lock和Synchronized ）/**乐观锁**（CAS锁）

**（2）自旋锁**（CAS） /**非自旋锁**（Synchronized）

自旋锁可以不断的尝试获取锁，整体锁的效率更高；而非自旋锁则会进行阻塞，从而减少CPU的损耗。

**（3）锁升级**===>无锁/偏向锁/轻量级锁/重量级锁（Synchronized在jdk6引入的）

**（4）公平锁/非公平锁；**

非公平锁由于不需要判断当前阻塞队列是否有元素，因此其能更好的利用CPU时间碎片。而公平锁可以给系统带来更高的可操控性。

**（5）可重入锁（ReentrantLock和synchronized）/非可重入锁；**

可重入锁是指在同一个线程在外层方法获取锁的时候，再进入该线程的内层方法会自动获取锁（前提锁对象得是同一个对象或者class），不会因为之前已经获取过还没释放而阻塞。在一定程度上避免了死锁的情况。

**（6）共享锁/非共享锁：**

**共享锁**（S锁）：如果事务T对数据A加上共享锁后，则其他事务只能对A再加共享锁，不能加排他锁。获准共享锁的事务只能读数据，不能修改数据。
**排他锁**（X锁）：如果事务T对数据A加上排他锁后，则其他事务不能再对A加任任何类型的封锁。获准排他锁的事务既能读数据，又能修改数据。

<img src="https://img-blog.csdnimg.cn/20181122101753671.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2F4aWFvYm9nZQ==,size_16,color_FFFFFF,t_70" alt="img" style="zoom:50%;" />



### ReentrantLock/lock:

**一、ReentrantLock底层实现：**ReentrantLock主要采用**CAS+AQS队列**来实现。它支持公平锁和非公平锁，两者的实现类似。其中	**AbstractQueuedSynchronizer简称AQS**，是一个用于构建锁和同步容器的框架。AQS使用一个FIFO的队列表示排队等待锁的线程，队列头节点称作“哨兵节点”或者“哑节点”，它不与任何线程关联。其他的节点与等待线程关联，每个节点维护一个**等待状态waitStatus**。同时，ReentrantLock也属于**重入锁**。

​	ReentrantLock的基本实现概括为：

1、先通过CAS尝试获取锁。

2、如果此时已经有线程占据了锁，那就加入AQS队列并且被挂起。

3、当锁被释放之后，排在CLH队列队首的线程会被唤醒，然后CAS再次尝试获取锁。

​	基于公平锁和非公平锁又有些许的差别，在**非公平锁**下，如果同时还有另一个线程进来尝试获取，那么有可能会让这个线程抢先获取；而在**公平锁**下，如果同时还有另一个线程进来尝试获取，当它发现自己不是在队首的话，就会排到队尾，由队首的线程获取到锁。

<img src="https://img-blog.csdnimg.cn/20181104201101705.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2Z1eXV3ZWkyMDE1,size_16,color_FFFFFF,t_70" alt="img" style="zoom:50%;" />

​	在ReetrantLock的**tryLock(long timeout, TimeUnit unit)** 提供了超时获取锁的功能。它的语义是在指定的时间内如果获取到锁就返回true，获取不到则返回false。这种机制避免了线程无限期的等待锁释放。另外，ReentrantLock既可以是公平锁也可以是非公平锁，在new对象的时候传入true参数可以构成公平锁。

```java
Lock lock = new ReentrantLock(true); // 公平锁，
Lock lock = new ReentrantLock(false); //	非公平锁,默认为非公平锁。
```

### AQS

AQS（AbstractQueuedSynchronizer，抽象队列同步器）是将每一条请求共享资源的线程封装成一个CLH锁队列的一个结点（Node），源代码如下：

```java
	static final class Node {
        static final Node SHARED = new Node();
        static final Node EXCLUSIVE = null;
        static final int CANCELLED =  1;
        static final int SIGNAL    = -1;
        static final int CONDITION = -2;
        static final int PROPAGATE = -3;
        volatile int waitStatus; //线程的等待状态
        volatile Node prev,next;		// 双向链表的结构 
        volatile Thread thread;//Node对象用来包装线程
        Node nextWaiter;		// 用来表明当前node的线程是想要获取共享锁还是独占锁
        final boolean isShared() {
            return nextWaiter == SHARED;
        }
    }
--------------------------------------------------------------------------------------------
private transient volatile Node head;// 头指针，固定是一个dummy node，因为它的thread成员固定为null
private transient volatile Node tail;// 尾节点，请求锁失败的线程，会包装成node，放到队尾
```

同时采用volatile修饰共享变量**state**，所以当state为0时，代表没有线程持有锁。当state为1时，代表有线程持有锁。当state>1时，代表有线程持有该锁，并且重入过该锁。所以state是否为0，可以作为判断是否有线程持有该独占锁的标准。。

```java
private volatile int state;	//用于互斥访问使用。
```

由于本文分析的是独占锁，所以当state为0时，代表没有线程持有锁。当state为1时，代表有线程持有锁。当state>1时，代表有线程持有该锁，并且重入过该锁。**所以state是否为0，可以作为判断是否有线程持有该独占锁的标准。**线程通过CAS去改变state，成功则获取锁成功，失败则进入等待队列，等待被唤醒。

```java
private transient Thread exclusiveOwnerThread;	//用于记录当前的线程使用者
```

<img src="https://img-blog.csdnimg.cn/20181128142923147.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L211bGluc2VuNzc=,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:80%;" />

​	如图示，AQS维护了一个volatile int state和一个FIFO线程等待队列(双向队列)，多线程争用资源被阻塞的时候就会进入这个队列。state就是共享资源，其访问方式有如下三种：getState()；setState()；compareAndSetState()；

AQS 定义了两种资源共享方式：
1、**Exclusive**：独占，只有一个线程能执行，如ReentrantLock。
2、**Share**：共享，多个线程可以同时执行，如Semaphore、CountDownLatch、ReadWriteLock，CyclicBarrier

线程进入AQS的基本流程如下：

![img](https://images2015.cnblogs.com/blog/721070/201511/721070-20151102145743461-623794326.png)

**二、[条件变量（Condition）](https://www.jianshu.com/p/4358b1466ec9)：**

​	条件变量很大一个程度上是为了解决Object.wait/notify/notifyAll难以使用的问题。创建一个condition对象是通过`lock.newCondition()`创建。其底层原理为，内部维护了一个单向**等待队列**，所有调用condition.await方法的线程会加入到等待队列中，并且线程状态转换为等待状态。

1. Synchronized中，所有的线程都在同一个object的条件队列上等待。而ReentrantLock中，每个condition都维护了一个条件队列。
2. 每一个**Lock**可以有任意数量的**Condition**对象，**Condition**是与**Lock**绑定的，所以就有**Lock**的公平性特性：如果是公平锁，线程为按照FIFO的顺序从*Condition.await*中释放，如果是非公平锁，那么后续的锁竞争就不保证FIFO顺序了。
3. Condition接口定义的方法，**await**对应于**Object.wait**，**signal**对应于**Object.notify**，**signalAll**对应于**Object.notifyAll**。特别说明的是Condition的接口改变名称就是为了避免与Object中的*wait/notify/notifyAll*的语义和使用上混淆。

### JAVA对象头

​	对象头含有三部分：**Mark Word**（存储对象自身运行时数据）、**Class Metadata Address**（存储类元数据的指针）、**Array length**（数组长度，只有数组类型才有）。重点在Mark Word部分，Mark Word数据结构被设计成非固定的动态数据，会随着对象的不同状态而变化，如下所示。

<img src="https://img-blog.csdn.net/20151217151455512?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQv/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center" alt="img" style="zoom:50%;" />

对象的生命周期：

1、创建，如果当前没有进行过加载，则进行对应的类加载。

2、内存分配，默认从Eden区域中取内存空间分配给对象，如果空间不足进行minorGC，再不足进行



### Synchronized

​	Synchronized底层主要是依靠对应的**monitorenter**和**monitorexit**指令分别对应synchronized同步块的进入和退出，有两个monitorexit指令的原因是：为了保证抛异常的情况下也能释放锁，所以javac为同步代码块添加了一个隐式的try-finally，在finally中会调用monitorexit命令释放锁。

#### 锁升级

（**锁降级：**JVM 进入安全点（SafePoint）的时候，会检查是否有闲置的 Monitor，然后试图进行降级)

##### 1、无锁状态

​	即对资源进行访问不需要先获取锁。

##### 2、偏向锁

​	当线程1访问代码块并获取锁对象时，会在java对象头(**MarkWord**）和栈帧中**记录偏向的锁的threadID**，因为偏向锁不会主动释放锁，**因此以后线程1再次获取锁的时候，需要比较当前线程的threadID和Java对象头中的threadID是否一致，如果一致（还是线程1获取锁对象），则无需使用CAS来加锁、解锁**；如果不一致，则需要进行以下的判断来进行锁升级：

```java
	例如线程2要竞争锁对象，而偏向锁不会主动释放，因此还是存储的线程1的threadID，需要查看Java对象头中记录的线程1是否存活，如果没有存活，那么锁对象被重置为无锁状态，线程2可以竞争将其设置为偏向锁；如果存活，那么立刻查找该线程1的栈帧信息，如果还是需要继续持有这个锁对象，那么暂停线程1，撤销偏向锁，升级为轻量级锁，如果线程1不再使用该锁对象，那么将锁对象状态设为无锁状态，重新偏向新的线程。
```

##### 3、**轻量级锁**

​	轻量级锁考虑的是竞争锁对象的线程不多，而且线程持有锁的时间也不长的情景。线程1获取轻量级锁时会先把锁对象的**对象头MarkWord复制一份到线程1的栈帧中用于存储锁记录的空间**（称为DisplacedMarkWord），然后**使用CAS把对象头中的内容替换为线程1存储的锁记录（**DisplacedMarkWord**）的地址**；如果在线程1复制对象头的同时（在线程1CAS之前），线程2也准备获取锁，复制了对象头到线程2的锁记录空间中，但是在线程2进行CAS时，发现线程1已经把对象头换了，**线程2的CAS失败，那么线程2就尝试使用自旋锁来等待线程1释放锁**。CAS在等待时间较小的情况下，可以有效避免线程的上下文切换。

​	但是如果自旋的时间太长也不行，因为自旋是要消耗CPU的，因此自旋的次数是有限制的，比如10次或者100次，如果自旋次数到了线程1还没有释放锁，或者线程1还在执行，线程2还在自旋等待，这时又有一个线程3过来竞争这个锁对象，那么这个时候**轻量级锁就会膨胀为重量级锁**。

同时在自选这块，JDK中引入了自适应自选，即每次自选会根据上一次的自选选择合适的时间，从而避免无用的CPU资源消耗。

##### 4、重量级锁

​	采用monitor实现，在编译的时候会加上**monitorentry**和**monitorexit**，从而限制线程的进入。会自动的阻塞线程，不会占用CPU的内存，但同时锁的响应时间会较长。

```java
Monitor可以理解为一种同步工具，也可理解为一种同步机制，常常被描述为一个Java对象。
	(1) 互斥：一个Monitor在一个时刻只能被一个线程持有，即Monitor中的所有方法都是互斥的。
	(2) signal机制：如果条件变量不满足，允许一个正在持有Monitor的线程暂时释放持有权，当条件变量满足时，当前线程可以唤醒正在等待该条件变量的线程，然后重新获取Monitor的持有权。所有的Java对象是天生的Monitor，每一个Java对象都有成为Monitor的潜质，因为在Java的设计中 ，每一个Java对象自打娘胎里出来就带了一把看不见的锁，它叫做内部锁或者Monitor锁。
	Monitor的本质是依赖于底层操作系统的管程实现，操作系统实现线程之间的切换需要从用户态到内核态的转换，成本非常高。
```

- **锁粗化：**锁粗化就是将多个连续的加锁、解锁操作连接在一起，扩展成一个范围更大的锁，避免频繁的加锁解锁操作。

- **锁消除**：Java虚拟机在JIT编译时(可以简单理解为当某段代码即将第一次被执行时进行编译，又称即时编译)，通过对运行上下文的扫描，经过**逃逸分析**，去除不可能存在共享资源竞争的锁，通过这种方式消除没有必要的锁，可以节省毫无意义的请求锁时间



#### Lock/Synchronized 区别

##### 1、底层实现

​	synchronized 是**JVM**层面的锁，是**Java关键字**，依靠对应的monitorenter和monitorexiut对对应的代码块进行加锁的操作。而ReentrantLock则是基于**CAS和AQS**的实现，是API层面的实现。

##### 2、绑定条件

​	一个ReentrantLock可以绑定多个**Condition对象**，仅需多次调用new Condition()即可；而在synchronized中锁锁对象的wait()、notify()/notifyAll()可以**实现一个隐含的条件**，如果要和多余的条件关联，就不得不额外的增加一个锁。

##### 3、是否需要手动释放

​	synchronized发生异常时，**会自动释放线程占用的锁**，故不会发生死锁现象。Lock发生异常，若没有主动释放，极有可能造成死锁，**故需要在finally中调用unLock方法释放锁**；

##### 4、是否可中断

​	Synchronized不可以响应中断，但是lock可以通过lockInterruptibly()方法响应中断。

##### 5、是否公平的角度

​	Synchronized是**非公平**的锁，而lock、reentrantlock则是可以设置为**公平锁**。是否公平要判断是否会出现饥饿的现象。

##### 6、从锁的对象来说

​	synchronzied锁的是**对象**，锁是保存在对象头里面的，根据对象头数据来标识是否有线程获得锁/争抢锁；ReentrantLock锁的是**线程**，根据进入的线程和int类型的state标识锁的获得/争抢。

**两者的选择**：在一些内置锁无法满足需求的情况下，ReentrantLock可以作为一种高级工具。当需要一些高级功能时才应该使用ReentrantLock，这些功能包括：可定时的，可轮询的与**可中断**的锁获取操作，公平队列，以及非块结构的锁。否则，还是应该优先使用Synchronized



### [JVM线程内存模型](https://blog.csdn.net/zhaomengszu/article/details/80270696)

​	**Java内存模型**(Java Memory Model，JMM)主要是为了规定了线程和内存之间的一些关系。根据JMM的设计，系统存在一个主内存(Main Memory)，Java中所有变量都储存在主存中，对于所有线程都是共享的。每条线程都有自己的工作内存(Working Memory)，工作内存中保存的是主存中某些变量的拷贝，线程对所有变量的操作都是在工作内存中进行，线程之间无法相互直接访问，变量传递均需要通过主存完成。

![img](https://img-blog.csdn.net/20170513140412095?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvTFpONTE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

在[JVM](https://www.jianshu.com/p/8a58d8335270)内部，Java内存模型把内存分成了两部分：线程栈区和堆区， JVM中运行的每个线程都拥有自己的线程栈，线程栈包含了当前线程执行的方法调用相关信息，我们也把它称作调用栈。随着代码的不断执行，调用栈会不断变化。

​	特别需要注意的是，主内存和工作内存与JVM内存结构中的Java堆、栈、方法区等并不是同一个层次的内存划分，无法直接类比。《深入理解Java虚拟机》中认为，如果一定要勉强对应起来的话，从变量、主内存、工作内存的定义来看，**主内存主要对应于Java堆中的对象实例数据部分。工作内存则对应于虚拟机栈中的部分区域。**



#### 内存间的交互操作:

**Lock**：作用于主内存的变量，把一个变量标示为线程独占的状态。

**unlock**：作用于主内存的变量，它把一个处于锁定状态的变量释放出来，释放后的变量才能被其余线程使用。

**read**：作用于主内存的变量，把变量的值传输到线程工作内存中。

**Load**：作用于工作内存的变量，将工作内存的变量传输到工作内存的副本中。

**Use**：作用于工作内存的变量，把工作内存的变量值传递给执行引擎。当虚拟机遇到一个需要使用变量的字节码指令的时候，会执行这个操作。

**Assign**：把执行引擎接受的值传递给工作内存中的变量，虚拟机遇到变量赋值的字节码的时候采用这个命令。

**Store**：作用于工作内存的变量，把工作内存的值传递到主内存。

**Write**：作用于主内存的变量，把Store操作从工作内存中得到的变量放入到主内存变量中。

<img src="https://img-blog.csdn.net/20160507135725155" alt="虚拟机内存交互关系" style="zoom:75%;" />

#### 原子性：

​	在Java中，为了保证原子性，提供了两个高级的字节码指令**monitorenter**和**monitorexit**。在[synchronized的实现原理](http://www.hollischuang.com/archives/1883)文章中，介绍过这两个字节码，在Java中对应的关键字就是`synchronized`。因此，在Java中可以使用`synchronized`来保证方法和代码块内的操作是原子性的。而Volatile关键字在不满足下述两个条件的时候，需要采用Synchronized来进行同步。

- 运算结果不依赖变量的当前值，或能够确保只有单一的线程修改变量的值。
- 变量不需要与其他状态变量共同参与不变约束。

#### 可见性:

​	Java内存模型是通过在变量修改后将新值同步回主内存，在变量读取前从主内存刷新变量值的这种依赖主内存作为传递媒介的方式来实现的。Java中的**volatile**关键字提供了一个功能，那就是被其修饰的变量在被修改后可以立即同步到主内存，被其修饰的变量在每次是用之前都从主内存刷新。因此，可以使用**volatile**来保证多线程操作时变量的可见性，Java中的synchronized和final两个关键字也可以实现可见性。

- **Volatile的可见性原理：**

  ​	第一，**Volatile给指令加上了对应的内存屏障，从而阻止对应的指令进行重排序达到可见性的目的**。第二，volatile保证了修饰的共享变量在转换为汇编语言时，会加上一个以lock为前缀的指令(内存屏障)。当CPU发现一个变量被volatile修饰时，其会遵循下面的规则来确保可见性：

  1. 每次使用变量，都必须从主内存刷新最新的值，确保看到别人的改动。
  2. 每次修改变量，都必须重新刷新到主内存中，以确保其他线程看到线程对变量V的修改。
  3. 同时要求JVM不可以对volatile修饰的变量进行指令重排序，确保执行顺序相同。

  **重排序**，主要分为三种：

  ​	1、**编译器优化**，编译器（包括 JVM、JIT 编译器等）出于优化的目的，例如当前有了数据 a，把对 a 的操作放到一起效率会更高，避免读取 b 后又返回来重新读取 a 的时间开销，此时在编译的过程中会进行一定程度的重排

  ​	2、**CPU重排序**，CPU 同样会有优化行为，这里的优化和编译器优化类似，都是通过乱序执行的技术来提高整体的执行效率。

  ​	3、**内存的“重排序”**，内存系统内不存在真正的重排序，但是内存会带来看上去和重排序一样的效果。由于内存有缓存的存在，在 JMM 里表现为主存和本地内存，而主存和本地内存的内容可能不一致，所以这也会导致程序表现出乱序的行为。在JAVA中，指令重排序遵循**happens-before**的原则，即两个线程的重排序结果不会影响原有程序执行的效果。

- **Synchronized的可见性原理**：

  ​	Synchronized的可见性是由**“对一个变量执行unlock操作之前，必须先把此变量同步回主内存“**这条规则获得的。

- **Final可见性原理:**

  ​	**被final修饰的字段在构造器中一旦初始化，且构造器没有把“this”的引用传递出去**那么其他线程就能看见final字段的值。



#### 有序性:

​	在Java中，可以使用**synchronized**和**volatile**来保证多线程之间操作的有序性。实现方式有所区别：**volatile**关键字会禁止指令重排，synchronized关键字保证同一时刻只允许一条线程操作。读者可能发现了，好像synchronized关键字是万能的，他可以同时满足以上三种特性，这其实也是很多人滥用`synchronized`的原因。但是`synchronized`是比较影响性能的，虽然编译器提供了很多锁优化技术，但是也不建议过度使用。



#### 先行发生原则：

1、**程序次序规则**。在一个线程内，书写在前面的代码先行发生于后面的。确切地说应该是，按照程序的控制流顺序，因为存在一些分支结构。

2、**Volatile变量规则**。对一个volatile修饰的变量，对他的写操作先行发生于读操作。

3、**线程启动规则**。Thread对象的start()方法先行发生于此线程的每一个动作。

4、**线程终止规则**。线程的所有操作都先行发生于对此线程的终止检测。

5、**线程中断规则**。对线程interrupt()方法的调用先行发生于被中断线程的代码所检测到的中断事件。

6、**对象终止规则**。一个对象的初始化完成（构造函数之行结束）先行发生于发的finilize()方法的开始。

7、**传递性**。A先行发生B，B先行发生C，那么，A先行发生C。

8、**管程锁定规则**。一个unlock操作先行发生于后面对同一个锁的lock操作。



#### [共享变量的线程安全](https://blog.csdn.net/weixin_39891166/article/details/86293484)：

​	当10个客户端同时请求同一个接口，这样就产生了10个线程，当这10个线程需要共享一个**变量**时，就可能出现脏读等线程安全问题。解决的方案主要有：

一、**ThreadLocal**

ThreadLocal会把每一个线程变量的值存储到本地，线程之间不共用数据，从而杜绝数据脏读等问题

二、**InheritableThreadLocal**

ThreadLocal确实从一定程度上解决了线程安全的问题，但也有缺点，那就是父子线程之间不能进行值传递。我们先了解一下父子线程，其是指一个接口请求另一个接口，第二个接口的线程是由第一个接口的线程引发的，第一个接口的线程则为第二个接口线程的父线程。

三、**TransmittableThreadLocal**



### [JVM内存模型](https://zhuanlan.zhihu.com/p/101495810)

JMM是java的内存模型，大体上其分为三个部分，主要构造如下图：

<img src="https://pic1.zhimg.com/80/v2-354d31865d1fb3362f5a1ca938f9a770_1440w.jpg" alt="img" style="zoom:50%;" />

1、**类加载器**，主要负责类加载模块，将对应的字节码加载到内存区中。

2、**运行时数据区**，其又可以划分成五大部分：

（1）**堆**，属于线程共享的部分，其是OOM故障最主要的发源地，它存储着几乎所有的**实例对象**，由垃圾收集器负责管理回收，堆区由各子线程共享使用；堆的内存空间既可以固定大小，也可运行时动态地调整，通过参数-Xms设定初始值、-Xmx设定最大值。

（2）**方法区**，线程共享，用来存储已被虚拟机加载的**类信息、常量、静态变量、JIT**（just in time,即时编译技术）编译后的代码等数据。**运行时常量池**是方法区的一部分，用于存放编译期间生成的各种字面常量和符号引用。

- 在1.7版本中方法区迎来了一些改动，永久代中的**静态变量**和运行时常量池中的**字符串常量池**转移到了堆中，
  也就是说全局变量和其他常量(非字符串常量)还遗留在永久代中

- 在JDK1.8中，方法区转换变成了元空间，主要原因是：

  1、**字符串存在永久代中，容易出现性能问题和内存溢出**，类及方法的信息等比较难确定其大小，因此对于永久代的大小指定比较困难，太小 容易出现永久代溢出，太大则容易导致老年代溢出
  2、**永久代会为 GC 带来不必要的复杂度，并且回收效率偏低**
  3、**将 HotSpot 与 JRockit 合二为一**

（3）**虚拟机栈**，线程私有，它描述的是java方法执行的内存模型，每个方法执行的同时都会创建一个**栈帧**（Stack Frame）用于存储**局部变量表、操作数栈、动态链接、方法出口**等信息。每个方法从调用直至完成的过程，都对应着一个栈帧从入栈到出栈的过程。

（4）**本地方法栈**，线程私有，本地方法栈和虚拟机栈所发挥的作用是很相似的，它们之间的区别不过是虚拟机栈为虚拟机执行Java方法（字节码）服务，而本地方法栈则为虚拟机使用到的**Native方法**服务。(Native方法主要指的是一个java调用非java代码的接口。一个Native Method是这样一个java的方法：该方法的实现由非java语言实现，比如C。)

（5）**程序计数器**，是一块较小的内存空间，它可以看作是当前线程所执行的字节码的行号指示器。字节码解释器工作时就是通过改变这个计数器的值来选取下一条需要执行的字节码指令：分支、跳转、循环、异常处理、线程恢复等基础操作都会依赖这个计数器来完成。

3、**执行引擎**，通过类装载器装载的，被分配到JVM的运行时数据区的字节码会被执行引擎执行。执行引擎以指令为单位读取Java字节码。它就像一个CPU一样，一条一条地执行机器指令。



### 内存泄漏：

内存泄漏的根本原因，在于对象存在一条引用链，致使对应的GC不能对对象进行回收，从而造成内存不能再分配的情况。常见的内存泄漏有如下的情况：

1. **静态集合类**，如HashMap、LinkedList等，如果这些容器为静态的，那么它们的生命周期与程序一致，则容器中的对象在程序结束之前将不能被释放，从而造成内存泄漏。
2. **各种连接，如数据库连接、网络连接和IO连接等**。在对数据库进行操作的过程中，首先需要建立与数据库的连接，当不再使用时，需要调用close方法来释放与数据库的连接。只有连接被关闭后，垃圾回收器才会回收对应的对象。
3. **变量不合理的作用域**。一般而言，一个变量的定义的作用范围大于其使用范围，很有可能会造成内存泄漏。另一方面，如果没有及时地把对象设置为null，很有可能导致内存泄漏的发生。**如下面伪代码**，通过readFromNet方法把接受的消息保存在变量msg中，然后调用saveDB方法把msg的内容保存到数据库中，此时msg已经就没用了，由于msg的生命周期与对象的生命周期相同，此时msg还不能回收，因此造成了内存泄漏。

```java
public class UsingRandom {
		private String msg;
		public void receiveMsg(){
		readFromNet();// 从网络中接受数据保存到msg中
		saveDB();// 把msg保存到数据库中
		}
}
```

4、**内部类持有外部类**，如果一个外部类的实例对象的方法返回了一个内部类的实例对象，这个内部类对象被长期引用了，即使那个外部类实例对象不再被使用，但由于内部类持有外部类的实例对象，这个外部类对象将不会被垃圾回收，这也会造成内存泄露。

5、**改变哈希值**，当一个对象被存储进HashSet集合中以后，就不能修改这个对象中的那些参与计算哈希值的字段了，否则，对象修改后的哈希值与最初存储进HashSet集合中时的哈希值就不同了，在这种情况下，即使在contains方法使用该对象的当前引用作为的参数去HashSet集合中检索对象，也将返回找不到对象的结果，这也会导致无法从HashSet集合中单独删除当前对象，造成内存泄露。

6、**内存泄漏的另一个常见来源是缓存**，一旦你把对象引用放入到缓存中，他就很容易遗忘，对于这个问题，可以使用WeakHashMap代表缓存，此种Map的特点是，当除了自身有对key的引用外，此key没有其他引用那么此map会自动丢弃此值

7、**监听器和回调**，内存泄漏第三个常见来源是监听器和其他回调，如果客户端在你实现的API中注册回调，却没有显示的取消，那么就会积聚。需要确保回调立即被当作垃圾回收的最佳方法是只保存他的若引用，例如将他们保存成为WeakHashMap中的键。

### 对象的生命周期:

对象的整个生命周期大致可以分为7个阶段：

1、**创建阶段**（Creation）

在对象创建阶段，系统要通过下面的步骤，完成对象的创建过程：

（1）为对象分配存储空间。

（2）开始构造对象。

（3）递归调用其超类的构造方法。

（4）进行对象实例初始化与变量初始化。

（5）执行构造方法体。

2、**应用阶段**（Using）

3、**不可视阶段**（Invisible）

4、**不可到达阶段**（Unreachable）

5、**可收集阶段**（Collected）

6、**终结阶段**（Finalized）

7、**释放阶段**（Free）



### [垃圾回收（GC）](https://blog.csdn.net/laomo_bible/article/details/83112622)

​	垃圾回收，我们的内存垃圾回收主要集中于 java 堆和方法区中，在程序运行期间，这部分内存的分配和使用都是动态的，因此需要对这部分内容进行合理的回收。程序运行时，内存空间是有限的，那么如何及时的把不再使用的对象清除将内存释放出来，这就是GC要做的事。总体概述图如下：

<img src="https://img-blog.csdn.net/20171121144712406?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDIyOTIxNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast" alt="清理对象" style="zoom:67%;" />

#### GC对象判定：

​	需要进行回收的对象就是已经没有存活的对象，判断一个对象是否存活常用的有两种办法：**引用计数**和**可达分析**。

##### 引用计数：

​	每个对象有一个引用计数属性，新增一个引用时计数加1，引用释放时计数减1，计数为0时可以回收。此方法简单，**无法解决对象相互循环引用的问题**。

##### **可达性分析**：

​	从GC Roots开始向下搜索，搜索所走过的路径称为引用链。当一个对象到GC Roots没有任何引用链相连时，则证明此对象是不可用的，即不可达对象。**ps:当标记为不可达的对象时，该对象是不可以再被引用的。**

```java
在Java语言中，GC Roots包括：
1、虚拟机栈（局部变量表）中引用的对象。
2、方法区中类静态属性实体引用的对象（采用static修饰的对象）。
3、方法区中常量引用的对象（final修饰的对象）。
4、本地方法栈中JNI引用的对象（使用native修饰的方法）。
```

#### GC清理常用算法：

##### 标记清除法：

​	为每个对象存储一个标记位，记录对象的状态（活着或是死亡）。分为两个阶段，一个是标记阶段，这个阶段内，为每个对象更新标记位，检查对象是否死亡；第二个阶段是清除阶段，该阶段对死亡的对象进行清除，执行 GC 操作。

##### 标记整理法：

​	与标记清除类似，该算法也将所有对象标记为存活和死亡两种状态；不同的是，在第二个阶段，该算法并没有直接对死亡的对象进行清理，而是将所有存活的对象整理一下，放到另一处空间，然后把剩下的所有对象全部清除。这样可以避免**内存碎片**的产生

##### 复制算法：

​	该算法将内存平均分成两部分，然后每次只使用其中的一部分，当这部分内存满的时候，将内存中所有存活的对象复制到另一个内存中，然后将之前的内存清空，只使用这部分内存，循环下去。优点是不产生内存碎片，缺点是只能使用一半内存空间。

##### 分代回收算法：

​	它根据对象的生存周期，将堆分为**新生代(Young)和老年代(Tenure)**，默认比例大小为1:2。在新生代中，由于对象生存期短，每次回收都会有大量对象死去，那么这时就采用复制算法。老年代里的对象存活率较高，没有额外的空间进行分配担保，所以可以使用**标记-整理 或者 标记-清除**。

#### GC触发的时机

```java
GC又分为 minor GC 和 Full GC(也称为 Major GC )
Minor GC触发条件：
  当Eden区满时，触发Minor GC。

Full GC触发条件：
  a.调用System.gc时，系统建议执行Full GC，但是不必然执行
  b.老年代空间不足（关键）
  c.方法区空间不足（关键）
  d.通过Minor GC后进入老年代的平均大小大于老年代的可用内存
  e.由Eden区、From Space区向To Space区复制时，对象大小大于To Space可用内存，则把该对象转存到老年代，且老年代的可用内存小于该对象大小
```

新生代转换为老年代具体有四种情况，如下。

1. **Eden区满时，进行Minor GC**，当Eden和一个Survivor区中依然存活的对象无法放入到Survivor中，则通过**分配担保机制**提前转移到老年代中。**分配担保机制**是指，将当前新生代Eden区中的对象拷贝到老年代中，从而清理出新生代的空间用于存储新的大对象。
2. **对象体积太大，新生代无法容纳**，**XX:PretenureSizeThreshold**即对象的大小大于此值, 就会绕过新生代, 直接在老年代分配, 此参数只对Serial及ParNew两款收集器有效。
3. **长期存活的对象将进入老年代**，虚拟机对每个对象定义了一个对象年龄（Age）计数器。当年龄增加到一定的临界值时，就会晋升到老年代中，该临界值由参数：**-XX:MaxTenuringThreshold**来设置。如果对象在Eden出生并在第一次发生MinorGC时仍然存活，并且能够被Survivor中所容纳的话，则该对象会被移动到Survivor中，并且设Age=1；以后每经历一次Minor GC，该对象还存活的话Age=Age+1。
4. **动态对象年龄判定**，虚拟机并不总是要求对象的年龄必须达到MaxTenuringThreshold才能晋升到老年代，如果在Survivor区中相同年龄（设年龄为age）的**对象的所有大小之和超过Survivor空间的一半**，年龄大于或等于该年龄（age）的对象就可以直接进入老年代，无需等到MaxTenuringThreshold中要求的年龄。

**跨代引用**是指新生代中存在对老年代对象的引用，或者老年代中存在对新生代的引用，

​	更细致的，新生代还可以划分成Eden区，From Surivior区和To Survivor区三个部分，比例为8:1:1。

```java
之所以使用两个Surivior区域，是为了避免对象从Eden区域复制到Surivior区域时，由于之前的数据还保存在Surivior中可能会导致内存碎片的出现，采用两个Surivior区，就可以始终保持其中一个Surivior区域是空的。等到一些对象经历了15次GC后，会从Surivior区域转移到老年代中。
```

如下是分代垃圾收集的过程，始终会保持一个Surivior中为全空状态。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQ4OTY2OS8yMDE4MTAvMTQ4OTY2OS0yMDE4MTAxNjE5NDEzNjA5Ny05MzYzNTg2NTcucG5n?x-oss-process=image/format,png" alt="img" style="zoom:50%;" />

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQ4OTY2OS8yMDE4MTAvMTQ4OTY2OS0yMDE4MTAxNjE5NDIwNzYwNi0yOTg1Nzc2ODIucG5n?x-oss-process=image/format,png" alt="img" style="zoom:50%;" />

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQ4OTY2OS8yMDE4MTAvMTQ4OTY2OS0yMDE4MTAxNjE5NDIzNjAwNy0xNDI4NDA4MzUyLnBuZw?x-oss-process=image/format,png" alt="img" style="zoom:50%;" />

等达到GC的阈值之后，就一并移动到老年代中。

<img src="https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTQ4OTY2OS8yMDE4MTAvMTQ4OTY2OS0yMDE4MTAxNjE5NDMwMjk3NC0xODQ0NzM0MzMxLnBuZw?x-oss-process=image/format,png" alt="img" style="zoom:50%;" />

**跨代引用**：跨代引用是指新生代中存在对老年代对象的引用，或者老年代中存在对新生代的引用。minor GC时，为了找到年轻代中的存活对象，不得不遍历整个老年代；反之亦然。这种方案存在极大的性能浪费。

**解决方案**：**记忆集**，是用来记录跨代引用的表，通过引入记忆集避免遍历老年代。以minor GC为例说明，要回收年轻代，只需要引用年轻代对象的GC ROOT+记忆集，就可以判断出Young区对象是否存活，不必再遍历老年代。缺点是具有“滞后性”，浪费一定的空间，因为如果没有进行Full GC，一些老年代中的引用难以被清除。

#### 垃圾收集器：

<img src="https://img-blog.csdnimg.cn/20190222222328910.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l2YV9icm90aGVy,size_16,color_FFFFFF,t_70" alt="img" style="zoom:77%;" />

##### 1、Serial 垃圾回收器 

##### 2、Serial Old垃圾回收器

​	Serial垃圾回收器采用**复制算法**，SerialOld垃圾回收器采用**标记整理算法**，两种都是采用串型单线程的方式进行垃圾回收。

<img src="https://img-blog.csdnimg.cn/20190222222433393.jpeg" alt="img" style="zoom: 67%;" />

##### 3、ParNew垃圾收集器

​	其是Serial收集器的多线程版本，用于**新生代**收集，常采用**复制算法**，目前只有它能与CMS收集器配合工作。

<img src="https://img-blog.csdnimg.cn/20190222222515855.jpeg?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2l2YV9icm90aGVy,size_16,color_FFFFFF,t_70" alt="img" style="zoom:67%;" />

##### 4、Parallel Scavenge

其属于**新生代**垃圾收集器，采用**复制**算法，关注吞吐量,吞吐量优先，吞吐量=代码运行时间/(代码运行时间+垃圾收集时间)，也就是高效率利用cpu时间，Parallel Scavenge收集器使用两个参数控制吞吐量：

- XX:MaxGCPauseMillis 控制最大的垃圾收集停顿时间
- XX:GCRatio 直接设置吞吐量的大小。

除此之外，Parallel Scavenge收集器还可以设置参数-XX:+UseAdaptiveSizePocily来动态调整停顿时间或者最大的吞吐量，这种方式称为**GC自适应调节策略**，这个是ParNew没有的。

##### 5、Parallel Old

ParallelScavenge的老年版本，用于**老年代**收集，常采用**标记整理算法**。

<img src="https://img-blog.csdn.net/20160505192422531" alt="Parallel Scavenge and Parrallel Old收集器组合" style="zoom: 50%;" />

##### 6、CMS收集器

CMS收集器（Concurrent Mark Sweep）的目标就是**获取最短回收停顿时间**。在注重服务器的响应速度，希望停顿时间最短，则CMS收集器是比较好的选择。整个执行过程分为以下4个步骤：

1. **初始标记**
2. **并发标记**
3. **重新标记**
4. **并发清除**，（与用户并发，因此产生了浮动垃圾。）

初始标记和重新标记这两个步骤仍然需要暂停Java执行线程，**初始标记**只是标记GC Roots能够关联到的对象，**并发标记**就是执行GC Roots Tracing的过程，而**重新标记**就是为了修正并发标记期间因用户程序执行而导致标记发生变动使得标记错误的记录。其执行过程如下：

<img src="https://img-blog.csdn.net/20160505193622716" alt="CMS收集器" style="zoom:50%;" />

CMS的**主要缺点**在于：

- CMS收集器无法处理**浮动垃圾**。所谓的“浮动垃圾”，就是在**并发清除**阶段，由于用户程序在运行，那么自然就会有新的垃圾产生，CMS无法在当次集中处理它们，只好在下一次GC的时候处理。这部分未处理的垃圾就称为**“浮动垃圾”**
- **对CPU资源太敏感**，这点可以这么理解，虽然在并发标记阶段用户线程没有暂停，但是由于收集器占用了一部分CPU资源，导致程序的响应速度变慢。
- 由于CMS收集器是基于**“标记-清除”**算法的，前面说过这个算法会导致大量的空间碎片的产生，一旦空间碎片过多，大对象就没办法给其分配内存,那么即使内存还有剩余空间容纳这个大对象，但是却没有连续的足够大的空间放下这个对象，所以虚拟机就会触发一次Full GC（这个后面还会提到）这个问题的解决是通过控制参数-XX:+UseCMSCompactAtFullCollection，用于在CMS垃圾收集器顶不住要进行FullGC的时候开启空间碎片的合并整理过程。

##### 7、G1收集器

G1（Garbage-First）收集器是现今收集器技术的最新成果之一，之前一直处于实验阶段，直到jdk7u4之后，才正式作为商用的收集器。与前几个收集器相比，G1收集器有以下特点：

- 并行与并发
- 分代收集（仍然保留了分代的概念）
- 空间整合（整体上属于“标记-整理”算法，不会导致空间碎片）
- 可预测的停顿（比CMS更先进的地方在于能让使用者明确指定一个长度为M毫秒的时间片段内，消耗在垃圾收集上的时间不得超过N毫秒）

​	此外，G1收集器将Java堆划分为多个大小相等的Region（独立区域），新生代与老年代都是一部分Region的集合，G1的收集范围则是这一个个Region（化整为零）。

G1的工作过程如下：

1. **初始标记**（Initial Marking）
2. **并发标记**（Concurrent Marking）
3. **最终标记**（Final Marking）
4. **筛选回收**（Live Data Counting and Evacuation），采用STW来避免出现浮动垃圾。                                 

​	**初始标记**阶段仅仅只是标记一下GC Roots能够直接关联的对象，并且修改TAMS（Next Top at Mark Start）的值，让下一阶段的用户程序并发运行的时候，能在正确可用的Region中创建对象，这个阶段需要暂停线程。**并发标记**阶段从GC Roots进行可达性分析，找出存活的对象，这个阶段与用户线程并发执行的。**最终标记阶段则是修正在并发标记阶段因为用户程序的并发执行而导致标记产生变动的那一部分记录**，这部分记录被保存在**Remembered Set Logs**中，最终标记阶段再把Logs中的记录合并到Remembered Set中。最后在筛选阶段首先对各个Region的回收价值和成本进行排序，根据用户所期望的GC停顿时间制定回收计划，同时采用STW的方式进行回收，从而避免了浮动垃圾的产生。整个执行过程如下：

<img src="https://img-blog.csdn.net/20160505194916580" alt="G1收集器" style="zoom: 50%;" />





### [JVM调优](https://blog.csdn.net/weixin_42447959/article/details/81637909)

**JVM调优目标**：使用较小的内存占用来获得较高的吞吐量或者较低的延迟。调优有几个比较重要的指标：

- 内存占用：程序正常运行需要的内存大小。
- 延迟：由于垃圾收集而引起的程序停顿时间。
- 吞吐量：用户程序运行时间占用户程序和垃圾收集占用总时间的比值。

**JVM调优工具：**

**（1）调优数据：**

​	可以依赖、参考的数据有**系统运行日志、堆栈错误信息、GC日志、线程快照、堆转储快照**等。

​	①**系统运行日志**：系统运行日志就是在程序代码中打印出的日志，描述了代码级别的系统运行轨迹（执行的方法、入参、返回值等），一般系统出现问题，系统运行日志是首先要查看的日志。

​	②**堆栈错误信息**：当系统出现异常后，可以根据堆栈信息初步定位问题所在，比如根据“java.lang.OutOfMemoryError: Java heap space”可以判断是堆内存溢出；根据“java.lang.StackOverflowError”可以判断是栈溢出；根据“java.lang.OutOfMemoryError: PermGen space”可以判断是方法区溢出等。

​	③**GC日志**：程序启动时用 -XX:+PrintGCDetails 和 -Xloggc:/data/jvm/gc.log 可以在程序运行时把gc的详细过程记录下来，或者直接配置“-verbose:gc”参数把gc日志打印到控制台，通过记录的gc日志可以分析每块内存区域gc的频率、时间等，从而发现问题，进行有针对性的优化。 

​	④**[线程快照](http://www.cnblogs.com/kongzhongqijing/articles/3630264.html)**：顾名思义，根据线程快照可以看到线程在某一时刻的状态，当系统中可能存在请求超时、死循环、死锁等情况是，可以根据线程快照来进一步确定问题。通过执行虚拟机自带的“jstack pid”命令，可以dump出当前进程中线程的快照信息，

​	⑤**堆转储快照**：程序启动时可以使用 “-XX:+HeapDumpOnOutOfMemory” 和 “-XX:HeapDumpPath=/data/jvm/dumpfile.hprof”，当程序发生内存溢出时，把当时的内存快照以文件形式进行转储（也可以直接用jmap命令转储程序运行时任意时刻的内存快照），事后对当时的内存使用情况进行分析。

**（2）JVM调优工具:**

​	①用jps（JVM process Status）可以查看虚拟机启动的所有进程、执行主类的全名、JVM启动参数，

​	②用jstat（JVM Statistics Monitoring Tool）监视虚拟机信息 jstat -gc pid 500 10 ：每500毫秒打印一次Java堆状况（各个区的容量、使用容量、gc时间等信息），打印10次。

​	③用jmap（Memory Map for Java）查看堆内存信息，执行jmap -histo pid可以打印出当前堆中所有每个类的实例数量和内存占用。

​	④利用jconsole、jvisualvm分析内存信息(各个区如Eden、Survivor、Old等内存变化情况).

​	⑤分析堆转储快照，前面说到配置了 “-XX:+HeapDumpOnOutOfMemory” 参数可以在程序发生内存溢出时dump出当前的内存快照，也可以用jmap命令随时dump出当时内存状态的快照信息，dump的内存快照一般是以.hprof为后缀的二进制格式文件。 

**（3）常用的JVM调优参数：**

| 参数                    | 说明                                                         | 实例                     |
| :---------------------- | :----------------------------------------------------------- | :----------------------- |
| -Xms                    | 初始堆大小，默认物理内存的1/64                               | -Xms512M                 |
| -Xmx                    | 最大堆大小，默认物理内存的1/4                                | -Xms2G                   |
| -Xmn                    | 新生代内存大小，官方推荐为整个堆的3/8                        | -Xmn512M                 |
| -Xss                    | 线程堆栈大小，jdk1.5及之后默认1M，之前默认256k               | -Xss512k                 |
| -XX:NewRatio=n          | 设置新生代和年老代的比值。如:为3，表示年轻代与年老代比值为1：3，年轻代占整个年轻代年老代和的1/4 | -XX:NewRatio=3           |
| -XX:SurvivorRatio=n     | 年轻代中Eden区与两个Survivor区的比值。注意Survivor区有两个。如:8，表示Eden：Survivor=8:1:1，一个Survivor区占整个年轻代的1/8 | -XX:SurvivorRatio=8      |
| -XX:PermSize=n          | 永久代初始值，默认为物理内存的1/64                           | -XX:PermSize=128M        |
| -XX:MaxPermSize=n       | 永久代最大值，默认为物理内存的1/4                            | -XX:MaxPermSize=256M     |
| -verbose:class          | 在控制台打印类加载信息                                       |                          |
| -verbose:gc             | 在控制台打印垃圾回收日志                                     |                          |
| -XX:+PrintGC            | 打印GC日志，内容简单                                         |                          |
| -XX:+PrintGCDetails     | 打印GC日志，内容详细                                         |                          |
| -XX:+PrintGCDateStamps  | 在GC日志中添加时间戳                                         |                          |
| -Xloggc:filename        | 指定gc日志路径                                               | -Xloggc:/data/jvm/gc.log |
| -XX:+UseSerialGC        | 年轻代设置串行收集器Serial                                   |                          |
| -XX:+UseParallelGC      | 年轻代设置并行收集器Parallel Scavenge                        |                          |
| -XX:ParallelGCThreads=n | 设置Parallel Scavenge收集时使用的CPU数。并行收集线程数。     | -XX:ParallelGCThreads=4  |
| -XX:MaxGCPauseMillis=n  | 设置Parallel Scavenge回收的最大时间(毫秒)                    | -XX:MaxGCPauseMillis=100 |
| -XX:GCTimeRatio=n       | 设置Parallel Scavenge垃圾回收时间占程序运行时间的百分比。公式为1/(1+n) | -XX:GCTimeRatio=19       |
| -XX:+UseParallelOldGC   | 设置老年代为并行收集器ParallelOld收集器                      |                          |
| -XX:+UseConcMarkSweepGC | 设置老年代并发收集器CMS                                      |                          |
| -XX:+CMSIncrementalMode | 设置CMS收集器为增量模式，适用于单CPU情况。                   |                          |



### 序列化

