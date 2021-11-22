



# 											JAVA 集合



# 前文--知识体系结构：![集合类架构图](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\java_collections_overview.png)





在Java中，**容器**只能**存放对象**，对于基本类型(**byte,boolean,int,short,float,double,long,char**八大基本数据类型) 需要将之转换成 包装类(相当于对象)(包装类如：Boolean,Byte,Integer,Short,Long,Float,Double,Character) 才能存入容器中，如果不通过转换成包装类直接存 基本数据类型的话，虽然不会出现bug，但会有额外的性能开销（这里的**额外开销**是由于 **JVM虚拟机会调用 包装类中的 valueOf方法，将基本数据类型转换成包装类**，详见下图），但简化了设计和编程(个人觉得还减少了一定可能性的bug)

![字节码中jvm对基本数据类型的操作示意图](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\字节码中jvm对基本数据类型的操作示意图.png)





# Collection

```
 容器主要包括 Collection 和 Map 两种，Collection 存储着对象的集合，而 Map 存储着键值对(两个对象)的映射表。
```

 

​	这里的Collection，可以根据下图了解到，涉及的是List、Set、Queue ( 在这里，涉及的均是直接将元素存入集合中，而Map则是根据键值对存取 )

![Collection涉及的集合类型](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\Collection涉及的集合类型.png)





## Set

###  	1.TreeSet

简介：(学习地址：https://www.cnblogs.com/skywang12345/p/3311268.html)

TreeSet 是一个**有序**的**集合**，它的作用是提供有序的Set集合。它继承于**AbstractSet抽象类**，实现了**NavigableSet<E>, Cloneable, java.io.Serializable接口**。
TreeSet 继承于**AbstractSet**，所以它是一个**Set集合**，具有Set的属性和方法。
TreeSet 实现了NavigableSet接口，意味着它支持一系列的导航方法。比如查找与指定目标最匹配项。
TreeSet 实现了**Cloneable**接口，意味着它**能被克隆**。
TreeSet 实现了java.io.**Serializable**接口，意味着它**支持序列化**。

TreeSet是**基于TreeMap实现**的。TreeSet中的元素支持2种排序方式：**自然排序 或者 根据创建TreeSet 时提供的 Comparator 进行排序**。这取决于使用的构造方法。

​		1) 由下面代码可以看出，**TreeSet的实现实际上依赖于 TreeMap**

​		2）**TreeSet**是 **非线程安全**类。( 没看到使用**synchronized关键字或Lock或CAS**等操作)

​		3) 查找耗费的时间复杂度为 **O(log n)** ，这是基于**红黑树**实现查找(**二分**)。

```java
public class TreeSet<E> extends AbstractSet<E>
    implements NavigableSet<E>, Cloneable, java.io.Serializable
{
    /**
     * NavigableMap对象
     */
    private transient NavigableMap<E,Object> m;

    // TreeSet是通过TreeMap实现的，
 	// PRESENT是键-值对中的值
    private static final Object PRESENT = new Object();

    /**
     * 将TreeMap对象赋值给NavigableMap的对象实例m
     */
    TreeSet(NavigableMap<E,Object> m) {
        this.m = m;
    }
    
    //创建一个空的TreeMap对象	
    public TreeSet() {
        this(new TreeMap<E,Object>());
    }
    
    //带比较器的构造函数
    public TreeSet(Comparator<? super E> comparator) {
        this(new TreeMap<>(comparator));
    }

    
    // 返回Map的长度
    public int size() {
        return m.size();
    }
    
    // 判断是否为空
    public boolean isEmpty() {
        return m.isEmpty();
    }
```



#### 如何遍历：

​	1) Iterator 遍历

```java
for(Iterator iter = set.iterator(); iter.hasNext(); ) { 
    iter.next();
}   

或
   
// 假设set是TreeSet对象
for(Iterator iter = set.descendingIterator(); iter.hasNext(); ) { 
    iter.next();
}
```



2) foreach 遍历

```java
for(  Object o: os){
}
```



#### TreeSet 基于红黑树 实现 查找 时间复杂度为O(log n) 的代码：

这里TreeSet依赖于 TreeMap，所以查找使用的方法 **contains() 会被转换成TreeMap的containsKey()方法**，如图( m代表 着 TreeMap，不理解回头看仔细)

![](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\TreeSet的查找方法(1).png)



这里再去查看 TreeMap中的 containsKey()方法，如下：

```java
 public boolean containsKey(Object key) {
        return getEntry(key) != null;
    }
```

根据方法中所提供的，再去查看 getEntry() 方法，如下：

​	这里可以看到，在查找的时候是 使用了  **红黑树**的数据结构，所以查找的时间复杂度为**O(log n)**

![](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\TreeSet的查找方法(2).png)

```java
final Entry<K,V> getEntry(Object key) {
        // Offload comparator-based version for sake of performance
        if (comparator != null)  //根据已有的比较器进行比较
            return getEntryUsingComparator(key);  //看下面
        if (key == null)	//传入的key为空值，则报错 NullPointerException
            throw new NullPointerException();
        @SuppressWarnings("unchecked")
            Comparable<? super K> k = (Comparable<? super K>) key;
        Entry<K,V> p = root;
        while (p != null) {
            int cmp = k.compareTo(p.key);
            if (cmp < 0)
                p = p.left;
            else if (cmp > 0)
                p = p.right;
            else
                return p;
        }
        return null;
    }
```

```
 final Entry<K,V> getEntryUsingComparator(Object key) {
        @SuppressWarnings("unchecked")
            K k = (K) key;
        Comparator<? super K> cpr = comparator;
        if (cpr != null) {
            Entry<K,V> p = root;
            while (p != null) {
                int cmp = cpr.compare(k, p.key);
                if (cmp < 0)
                    p = p.left;
                else if (cmp > 0)
                    p = p.right;
                else
                    return p;
            }
        }
        return null;
    }
```





### 2.HashSet

基于哈希表( HashMap )实现，支持快速查找（时间复杂度为O(1) ），但不支持有序性操作。并且失去了元素的插入顺序信息，也就是说使用 Iterator 遍历 HashSet 得到的结果是不确定的。

​		

可以根据下列代码总结：

​	1)HashSet  **依赖于 HashMap实现**。所有方法实现的均需要 通过**HashMap**中的对应方法实现。

​	2) **不是线程安全**的

```
public class HashSet<E>
    extends AbstractSet<E>
    implements Set<E>, Cloneable, java.io.Serializable
{
    static final long serialVersionUID = -5024744406713321676L;

//HashMap实例
    private transient HashMap<E,Object> map;

//map中的键值对对应的值Object
    // Dummy value to associate with an Object in the backing Map
    private static final Object PRESENT = new Object();

    /**
     * 初始化
     */
    public HashSet() {
        map = new HashMap<>();
    }

//初始化HashMap实例
 public HashSet(int initialCapacity, float loadFactor) {
        map = new HashMap<>(initialCapacity, loadFactor);
    }
    
    
    //通过HashMap中的containsKey()方法获取对应的key值
    public boolean contains(Object o) {
        return map.containsKey(o);
    }

    
```



这里**只需知道HashSet依赖于HashMap实现，然后了解HashMap的底层原理即可**。(因为HashMap在**jdk1.7和1.8出现了一些变化**，1.8改用了数组+链表+红黑树的数据结构实现的HashMap，而jdk1.7版本的HashMap基于数组+链表实现，有些复杂，在这不细讲)



### 3.LinkedHashSet

具有 **HashSet 的查找效率**，且内部使用**双向链表维护元素的插入顺序**。 这里可以简单的理解为拥有 **链表和 Set的双重特性**

如下，可以看出，**LinkedHashSet 继承了 HashSet** 类。

```
public class LinkedHashSet<E>
    extends HashSet<E>
    implements Set<E>, Cloneable, java.io.Serializable {

    private static final long serialVersionUID = -2851667679971038690L;
	
	
	//super() : 向父类中查找对应方法。这里是找HashSet的有参构造器方法。
    public LinkedHashSet(int initialCapacity, float loadFactor) {
        super(initialCapacity, loadFactor, true);
    }

	//super() : 向父类中查找对应方法。这里是找HashSet的有参构造器方法。
    public LinkedHashSet(int initialCapacity) {
        super(initialCapacity, .75f, true);
    }
    
	//super() : 向父类中查找对应方法。这里是找HashSet的有参构造器方法。
    public LinkedHashSet() {
        super(16, .75f, true);
    }


    public LinkedHashSet(Collection<? extends E> c) {
        super(Math.max(2*c.size(), 11), .75f, true);
        addAll(c);
    }

```



在HashSet中也有体现：

```
HashSet(int initialCapacity, float loadFactor, boolean dummy) {
        map = new LinkedHashMap<>(initialCapacity, loadFactor);
    }
```



相对应的，在 **LinkedHashMap**中，可以看到，LinkedHashMap继承了 HashMap 类

```
public class LinkedHashMap<K,V>
    extends HashMap<K,V>
    implements Map<K,V>
{

```









## List

学习地址： (https://pdai.tech/md/java/collection/java-collection-ArrayList.html)

### 	

### 	1.ArrayList 



​		基于**动态数组**实现（ensureCapacity（）方法），支持随机访问。

​		

​		可以看出，ArrayList 实现了 **List 接口**，这代表着 ArrayList 是一个 **有序(顺序)集合。**也就是**集合元素的数据与它 放入集合中的顺序相同**。

​							ArrayList 实现了**Cloneable**接口，意味着它**能被克隆**。

​							ArrayList 实现了java.io.**Serializable**接口，意味着它**支持序列化**。

​		但，ArrayList 并**不是一个 线程安全**的集合。

```java

public class ArrayList<E> extends AbstractList<E>
        implements List<E>, RandomAccess, Cloneable, java.io.Serializable
{
    private static final long serialVersionUID = 8683452581122892189L;
	
    //初始长度
    private static final int DEFAULT_CAPACITY = 10;

    
    /**
    ArrayList 的元素存储在其中的数组缓冲区。 ArrayList 的容量就是这个数组缓冲区的长度。 添加第一个元素时，任何带有 elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA 的空 ArrayList 都将扩展为 DEFAULT_CAPACITY。
    **/
    transient Object[] elementData;
    
    //初始化一个具有指定容量的空列表list
     public ArrayList(int initialCapacity) {
        if (initialCapacity > 0) {
            this.elementData = new Object[initialCapacity];
        } else if (initialCapacity == 0) {
            this.elementData = EMPTY_ELEMENTDATA;
        } else {
            throw new IllegalArgumentException("Illegal Capacity: "+
                                               initialCapacity);
        }
    }
    
    
    //构造一个初始容量为 10 的空列表。
     public ArrayList() {
        this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;
    }
    
    //动态数组实现，扩容
    public void ensureCapacity(int minCapacity) {
        int minExpand = (elementData != DEFAULTCAPACITY_EMPTY_ELEMENTDATA)
            // any size if not default element table
            ? 0
            // larger than default for default empty table. It's already
            // supposed to be at default size.
            : DEFAULT_CAPACITY;

        if (minCapacity > minExpand) {
            ensureExplicitCapacity(minCapacity);
        }
    }
    //扩展
    private void ensureExplicitCapacity(int minCapacity) {
        modCount++;

        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
    }
    
    /**
    * grow() 才是真正实现动态数组的方法
    *增加容量以确保它至少可以容纳由最小容量参数指定的元素数量。
    **/
    private void grow(int minCapacity) {
        // overflow-conscious code
        int oldCapacity = elementData.length;
        int newCapacity = oldCapacity + (oldCapacity >> 1);
        if (newCapacity - minCapacity < 0)
            newCapacity = minCapacity;
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        // minCapacity is usually close to size, so this is a win:
        elementData = Arrays.copyOf(elementData, newCapacity);
    }
```



在List**添加元素**进去时，会**根据现长度判断是否需要扩容(增大容量)，然后再进行数据存储**。

```java
public boolean add(E e) {
    	//	进行判断
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }

private void ensureCapacityInternal(int minCapacity) {
        ensureExplicitCapacity(calculateCapacity(elementData, minCapacity));
    }
	
	//计算当前数组默认长度 与 列表元素的个数+1 
    private static int calculateCapacity(Object[] elementData, int minCapacity) {
        if (elementData == DEFAULTCAPACITY_EMPTY_ELEMENTDATA) {
            return Math.max(DEFAULT_CAPACITY, minCapacity);
        }
        return minCapacity;
    }
```



**size(), isEmpty(), get(), set()方法均能在常数时间内(O(1) )完成**，**add()方法的时间开销跟插入位置有关**，addAll()方法的时间开销跟添加元素的个数成正比。其余方法大都是线性时间。

```java
//直接获取size
public int size() {
        return size;
    }

// 判断 size是否为空即可
public boolean isEmpty() {
        return size == 0;
    }

// 检查给定的索引是否在范围内，若在范围内则返回 数组对应下标的值，唯一要注意的是由于底层数组是Object[]，得到元素后需要进行类型转换。
public E get(int index) {
        rangeCheck(index);
        return elementData(index);
    }


	//add()方法的时间开销跟插入位置有关，这里的add()方法则默认在数组尾部添加元素
	public boolean add(E e) {
        ensureCapacityInternal(size + 1);  // Increments modCount!!
        elementData[size++] = e;
        return true;
    }
	
	//在某一下标开始添加元素
	public void add(int index, E element) {
        rangeCheckForAdd(index);   //检查给定的索引是否在范围内

        ensureCapacityInternal(size + 1);  // 判断是否需要扩展数组容量
        System.arraycopy(elementData, index, elementData, index + 1,
                         size - index);   //这里类似于 将对应的下标往后推一位，再将元素添加到index位置中
        elementData[index] = element;
        size++;
    }

```



为追求效率，ArrayList**没有实现同步(synchronized)**，如果需要多个线程并发访问，用户可以手动同步，也可使用Vector替代。



set()方法： 给数组的特定位置赋值

```java
public E set(int index, E element) {
    rangeCheck(index);//下标越界检查
    E oldValue = elementData(index);
    elementData[index] = element;//赋值到指定位置，复制的仅仅是引用
    return oldValue;
}

```



 

**Fail-Fast机制:**ArrayList也采用了快速失败的机制，通过记录modCount参数来实现。在面对并发的修改时，迭代器很快就会完全失败，而不是冒着在将来某个不确定时间发生任意不确定行为的风险

注：modcount 在 ArrayList所 继承(extends) 的AbstractList 中创建。

```
private void fastRemove(int index) {
        modCount++;
        int numMoved = size - index - 1;
        if (numMoved > 0)
            System.arraycopy(elementData, index+1, elementData, index,
                             numMoved);
        elementData[--size] = null; // clear to let GC do its work
    }
```



### 2.Vector(子类Stack)

和 ArrayList 类似，但它是线程安全( 使用了synchronized关键字  )的。

​							Vector实现了 **List 接口**，这代表着 Vector是一个 **有序(顺序)集合。**也就是**集合元素的数据与它 放入集合中的顺序相同**。

​							Vector实现了**Cloneable**接口，意味着它**能被克隆**。

​							Vector实现了java.io.**Serializable**接口，意味着它**支持序列化**。

在 **Vector线程安全类** 中，**Stack类**继承了Vector。

```java
public class Stack<E> extends Vector<E> {
    public Stack() {
    }
    
    //入栈，addElement() 是父类方法
    public E push(E item) {
        addElement(item);

        return item;
    }
    
    //出栈，removeElementAt() 是父类方法
    public synchronized E pop() {
        E       obj;
        int     len = size();

        obj = peek();
        removeElementAt(len - 1);

        return obj;
    }
    
    //获取栈顶(不弹出),elementAt()是父类方法
    public synchronized E peek() {
        int     len = size();

        if (len == 0)
            throw new EmptyStackException();
        return elementAt(len - 1);
    }
    
    //查看栈是否为空
    public boolean empty() {
        return size() == 0;
    }
    
    //查找栈中某个元素,lastIndexOf()是父类方法
    public synchronized int search(Object o) {
        int i = lastIndexOf(o);

        if (i >= 0) {
            return size() - i;
        }
        return -1;
    }
```

父类**Vector**中，相关的方法：

```java
public class Vector<E>
    extends AbstractList<E>
    implements List<E>, RandomAccess, Cloneable, java.io.Serializable
{
//存储向量组件的数组缓冲区。 向量的容量是这个数组缓冲区的长度，并且至少足够包含向量的所有元素。
    protected Object[] elementData;

	//添加元素的安全方法
	public synchronized void addElement(E obj) {
        modCount++;
        ensureCapacityHelper(elementCount + 1);
        elementData[elementCount++] = obj;
    }
    //判断是否需要扩容
    private void ensureCapacityHelper(int minCapacity) {
        // overflow-conscious code
        if (minCapacity - elementData.length > 0)
            grow(minCapacity);
    }

	// 移除指定位置的元素
	public synchronized void removeElementAt(int index) {
        modCount++;
        if (index >= elementCount) {
            throw new ArrayIndexOutOfBoundsException(index + " >= " +
                                                     elementCount);
        }
        else if (index < 0) {
            throw new ArrayIndexOutOfBoundsException(index);
        }
        int j = elementCount - index - 1;
        if (j > 0) {
            System.arraycopy(elementData, index + 1, elementData, index, j);
        }
        elementCount--;
        elementData[elementCount] = null; /* to let gc do its work */
    }
    
    //获取特定位置的元素
    public synchronized E elementAt(int index) {
        if (index >= elementCount) {
            throw new ArrayIndexOutOfBoundsException(index + " >= " + elementCount);
        }

        return elementData(index);
    }
    
    //返回此向量中指定元素最后一次出现的索引，如果此向量不包含该元素，则返回 -1。 更正式地，返回最高索引i使得(o==null ? get(i)==null : o.equals(get(i))) ，如果没有这样的索引，则返回 -1 
    public synchronized int lastIndexOf(Object o) {
        return lastIndexOf(o, elementCount-1);
    }
    
    //返回此向量中指定元素最后一次出现的index ，从index向后搜索，如果未找到该元素，则返回 -1
    public synchronized int lastIndexOf(Object o, int index) {
        if (index >= elementCount)
            throw new IndexOutOfBoundsException(index + " >= "+ elementCount);

        if (o == null) {
            for (int i = index; i >= 0; i--)
                if (elementData[i]==null)
                    return i;
        } else {
            for (int i = index; i >= 0; i--)
                if (o.equals(elementData[i]))
                    return i;
        }
        return -1;
    }

```



JAVA官方已不再建议使用栈，而是改用另外的声明方式 **ArrayDeque** 来实现栈的性质( Deque<E>  stack=new ArrayDequeue<>() )。







### 3.LinkedList

基于**双向链表**实现，只能**顺序访问**，但是可以**快速地在链表中间插入和删除元素**。不仅如此，LinkedList 还可以用作**栈、队列和双向队列**



​		可以看出，LinkedList 实现了 **List 接口**，这代表着 ArrayList 是一个 **有序(顺序)集合。**也就是**集合元素的数据与它 放入集合中的顺序相同**。

​							LinkedList 实现了 **Deque接口**，这意味着 可以 将LinkedList作为一个 **队列**(先进先出)、或是一个 **栈**(后进先出) 使用。

​							LinkedList 实现了**Cloneable**接口，意味着它**能被克隆**。

​							LinkedList 实现了java.io.**Serializable**接口，意味着它**支持序列化**。



虽然现在仍可以使用   **Stack<Object>  stack =new  Stack<Object>();**       注意： Object对应包装类 

但在 Stack类中的官方解释中  已经声明了**不建议使用这样的方式来创建一个 Stack栈实例**。

而是改用了    **Deque<Object> stack = new ArrayDeque<Object>();**  来实现 栈。   注意: Deque是一个接口，不能使用接口来创建对象实例，所以首选的是 **ArrayDeque**



*LinkedList*的实现方式决定了所有跟下标相关的操作都是线性时间，而在首段或者末尾删除元素只需要常数时间。为追求效率*LinkedList***没有实现同步(synchronized)**，如果需要多个线程并发访问，可以先**采用`Collections.synchronizedList()`方法对其进行包装**。

```java
public class LinkedList<E>
    extends AbstractSequentialList<E>
    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
{
    transient int size = 0;

    //头节点
 	transient Node<E> first;
	//尾节点
    transient Node<E> last;

	//这是 双向链表的实现内部类Node
	private static class Node<E> {
        E item;
        Node<E> next;
        Node<E> prev;

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }

	//获取头节点的值 ，直接查找first
	public E getFirst() {
        final Node<E> f = first;
        if (f == null)
            throw new NoSuchElementException();
        return f.item;
    }

	//获取尾节点的值，直接查找last
    public E getLast() {
        final Node<E> l = last;
        if (l == null)
            throw new NoSuchElementException();
        return l.item;
    }
    
    
    
```



对应的LinkedList类中实现Queue的方法：

```java
   
    /**
     * Retrieves, but does not remove, the head (first element) of this list.
     *
     * @return the head of this list, or {@code null} if this list is empty
     * @since 1.5
     */
    public E peek() {
        final Node<E> f = first;
        return (f == null) ? null : f.item;
    }

    /**
     * Retrieves, but does not remove, the head (first element) of this list.
     *
     * @return the head of this list
     * @throws NoSuchElementException if this list is empty
     * @since 1.5
     */
    public E element() {
        return getFirst();
    }

    /**
     * Retrieves and removes the head (first element) of this list.
     *
     * @return the head of this list, or {@code null} if this list is empty
     * @since 1.5
     */
    public E poll() {
        final Node<E> f = first;
        return (f == null) ? null : unlinkFirst(f);
    }

    /**
     * Retrieves and removes the head (first element) of this list.
     *
     * @return the head of this list
     * @throws NoSuchElementException if this list is empty
     * @since 1.5
     */
    public E remove() {
        return removeFirst();
    }

    /**
     * Adds the specified element as the tail (last element) of this list.
     *
     * @param e the element to add
     * @return {@code true} (as specified by {@link Queue#offer})
     * @since 1.5
     */
    public boolean offer(E e) {
        return add(e);
    }

```











 

## Queue

​	Queue是一个接口类，所以在声明时不能使用Queue来声明，而是使用LinkedList 或PriorityQueue等方式来声明一个队列。

*Queue*接口**继承自 Collection接口**，除了最基本的Collection的方法之外，它还支持额外的***insertion*, *extraction*和*inspection***操作。这里有两组格式，共6个方法，**一组是抛出异常的实现；另外一组是返回值的实现(没有则返回null)**。

|         | Throws exception | Returns special value |
| ------- | ---------------- | --------------------- |
| Insert  | add(e)           | offer(e)              |
| Remove  | remove()         | poll()                |
| Examine | element()        | peek()                |

## 

Queue接口内的代码：

```java
public interface Queue<E> extends Collection<E> {
	
    boolean add(E e);
    boolean offer(E e);
    E remove();
    E poll();
    E element();
    E peek();
    
}
```





Deque： 双端队列，继承Queue接口，但Deque本身也是一个接口，所以无法实现队列的创建。

​				因为继承 Queue接口，所以支持Queue的方法，并在此基础上还支持  `insert`, `remove`和`examine`操作，且Deque可以在对队列的头部和尾部进行操作，支持两种方式：一种是抛出异常的实现；另外一组是返回值的实现(没有则返回null) 

 

|         | First Element - Head |               | Last Element - Tail |               |
| ------- | -------------------- | ------------- | ------------------- | ------------- |
|         | Throws exception     | Special value | Throws exception    | Special value |
| Insert  | addFirst(e)          | offerFirst(e) | addLast(e)          | offerLast(e)  |
| Remove  | removeFirst()        | pollFirst()   | removeLast()        | pollLast()    |
| Examine | getFirst()           | peekFirst()   | getLast()           | peekLast()    |

 

把Deque当作是 FIFO(先进先出)的Queue队列来使用，需要明白，Queue队列中元素是从尾部放入，头部出列(删除)，所以对应的方法：

 

| Queue Method | Equivalent Deque Method |
| ------------ | ----------------------- |
| add(e)       | addLast(e)              |
| offer(e)     | offerLast(e)            |
| remove()     | removeFirst()           |
| poll()       | pollFirst()             |
| element()    | getFirst()              |
| peek()       | peekFirst()             |

 



### [¶](#linkedlist-2) 1.LinkedList

可以用它来实现双向队列。

### [¶](#priorityqueue) 2.PriorityQueue

基于**堆结构实现**，可以用它来实现**优先队列**。

PriorityQueue是非线程安全的，所以Java提供了PriorityBlockingQueue（实现[BlockingQueue接口](http://www.journaldev.com/1034/java-blockingqueue-example-implementing-producer-consumer-problem)）用于[Java多线程环境](http://www.journaldev.com/1079/java-thread-tutorial)。

那么，需要了解一下堆的结构实现。在这里优先队列的**本质上可以理解为一棵 完全二叉树的数组对象 来实现小根堆**(默认情况下)。具体优先级大小是通过实现了Comparable接口对象的compareTo方法或者自定义的Comparator比较器决定的。

什么是完全二叉树呢？ 例如有一完全二叉树的深度为n,那么在1~n-1层符合满二叉树的性质即 每层的节点数都达到最大个数(2n-1,n代表层数)。并且第n层中节点集中在最左边。



PriorityQueue:  使用 PriorityQueue 类的方式有： 

```java
PriorityQueue<Object> queue=new PriorityQueue<>();   //Object 指的是八大引用类型(Integer,Character等)以及自定义引用对象
```

由于PriorityQueue优先队列类中有多个构造器，根据需求使用。**无参构造器默认的是 升序排列**。

```java
    private static final int DEFAULT_INITIAL_CAPACITY = 11;     //默认数组大小，在没有指定初始化大小时使用
 

//无参构造器，没有指定初始化大小以及比较器时，默认创建一个长度为11的数组，若存放的数据量超过11，设计数组的扩容操作
public PriorityQueue() {
        this(DEFAULT_INITIAL_CAPACITY, null);
    }
//有参构造器，指定初始化大小
    public PriorityQueue(int initialCapacity) {
        this(initialCapacity, null);
    }

//有参构造器，指定比较器
    public PriorityQueue(Comparator<? super E> comparator) {
        this(DEFAULT_INITIAL_CAPACITY, comparator);
    }
//有参构造器，指定初始化大小以及比较器
    public PriorityQueue(int initialCapacity,
                         Comparator<? super E> comparator) {
        // Note: This restriction of at least one is not actually needed,
        // but continues for 1.5 compatibility
        if (initialCapacity < 1)
            throw new IllegalArgumentException();
        this.queue = new Object[initialCapacity];
        this.comparator = comparator;
    }

    
    @SuppressWarnings("unchecked")
    public PriorityQueue(Collection<? extends E> c) {
        if (c instanceof SortedSet<?>) {
            SortedSet<? extends E> ss = (SortedSet<? extends E>) c;
            this.comparator = (Comparator<? super E>) ss.comparator();
            initElementsFromCollection(ss);
        }
        else if (c instanceof PriorityQueue<?>) {
            PriorityQueue<? extends E> pq = (PriorityQueue<? extends E>) c;
            this.comparator = (Comparator<? super E>) pq.comparator();
            initFromPriorityQueue(pq);
        }
        else {
            this.comparator = null;
            initFromCollection(c);
        }
    }

    
    @SuppressWarnings("unchecked")
    public PriorityQueue(PriorityQueue<? extends E> c) {
        this.comparator = (Comparator<? super E>) c.comparator();
        initFromPriorityQueue(c);
    }

     
    @SuppressWarnings("unchecked")
    public PriorityQueue(SortedSet<? extends E> c) {
        this.comparator = (Comparator<? super E>) c.comparator();
        initElementsFromCollection(c);
    }
```



有关PriorityQueue中的数组扩容操作如下：

```java
// 根据当前数组的长度进行动态扩容

private void grow(int minCapacity) {
        int oldCapacity = queue.length;
        // Double size if small; else grow by 50%
        int newCapacity = oldCapacity + ((oldCapacity < 64) ?
                                         (oldCapacity + 2) :
                                         (oldCapacity >> 1));
        // overflow-conscious code
        if (newCapacity - MAX_ARRAY_SIZE > 0)
            newCapacity = hugeCapacity(minCapacity);
        queue = Arrays.copyOf(queue, newCapacity);
    }

    private static int hugeCapacity(int minCapacity) {
        if (minCapacity < 0) // overflow
            throw new OutOfMemoryError();
        return (minCapacity > MAX_ARRAY_SIZE) ?
            Integer.MAX_VALUE :
            MAX_ARRAY_SIZE;
    }
```



add()和offer()方法：新加入的元素`x`可能会破坏小顶堆的性质，因此需要进行调整。调整的过程为：**从`k`指定的位置开始，将`x`逐层与当前点的`parent`进行比较并交换，直到满足`x >= queue[parent]`为止**。注意这里的比较可以是元素的自然顺序，也可以是依靠比较器的顺序。

```java
//add(E e)和offer(E e)的语义相同，都是向优先队列中插入元素，只是Queue接口规定二者对插入失败时的处理不同，前者在插入失败时抛出异常，后则则会返回false。对于PriorityQueue这两个方法其实没什么差别。

//offer(E e),需要注意的是siftUp(int k, E x)方法，该方法用于插入元素x并维持堆的特性。
public boolean offer(E e) {
    if (e == null)//不允许放入null元素
        throw new NullPointerException();
    modCount++;
    int i = size;
    if (i >= queue.length)
        grow(i + 1);//自动扩容
    size = i + 1;
    if (i == 0)//队列原来为空，这是插入的第一个元素
        queue[0] = e;
    else
        siftUp(i, e);//调整
    return true;
}

//siftUp()
private void siftUp(int k, E x) {
    while (k > 0) {
        int parent = (k - 1) >>> 1;//parentNo = (nodeNo-1)/2
        Object e = queue[parent];
        if (comparator.compare(x, (E) e) >= 0)//调用比较器的比较方法
            break;
        queue[k] = e;
        k = parent;
    }
    queue[k] = x;
}
```





## Map

### [¶](#treemap) 1.TreeMap

基于红黑树实现。

### [¶](#hashmap) 2.HashMap

基于哈希表实现。



**HashSet 仅仅通过对 HashMap 作了一层包装(实质上还是HashMap**，只是显示上是HashSet)，所以只需理解HashMap即可。

在 JDK7 和JDK8中，HashMap出现了一些区别，在这里需要注意： 继承和实现没有变化。



区别： 

Java7 中使用 Entry 来代表每个 HashMap 中的数据节点，Java8 中使用 Node，基本没有区别，都是 key，value，hash 和 next 这四个属性，不过，Node 只能用于链表的情况，红黑树的情况需要使用 TreeNode。

我们根据数组元素中，第一个节点数据类型是 Node 还是 TreeNode 来判断该位置下是链表还是红黑树的。

### 

```java
public class HashMap<K,V> extends AbstractMap<K,V>
    implements Map<K,V>, Cloneable, Serializable {

```



**JDK7:**

*HashMap*实现了*Map*接口，即允许放入`key`为`null`的元素，也允许插入`value`为`null`的元素；除该类未实现同步外，其余跟`Hashtable`大致相同；跟*TreeMap*不同，该容器不保证元素顺序，根据需要该容器可能会对元素重新哈希，元素的顺序也会被重新打散，因此不同时间迭代同一个*HashMap*的顺序可能会不同。 根据对冲突的处理方式不同，哈希表有两种实现方式，一种开放地址方式(Open addressing)，另一种是冲突链表方式(Separate chaining with linked lists)。**Java7 \*HashMap\*采用的是冲突链表方式**。

HashMap中有对应的处理key位null的情况，它会先使用 hash方法，判断传进来的key是否为空，不为空则 进行哈希转换，为空则置为0。

jdk7中的hash方法 使用了4次异或的操作，而jdk8则简化了，只做了一次16位右移异或混合，进行了优化，原理仍然一样。

```java
//jdk7的hash方法
static int hash(int h) {
    // This function ensures that hashCodes that differ only by
    // constant multiples at each bit position have a bounded
    // number of collisions (approximately 8 at default load factor).

    h ^= (h >>> 20) ^ (h >>> 12);
    return h ^ (h >>> 7) ^ (h >>> 4);
}

//jdk8中的hash方法
static final int hash(Object key) {
        int h;
        return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
    }
```



jdk7:  jdk7采用的是 数组+链表的形式   

![](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\HashMap_base.png)

 

从上图容易看出，如果选择合适的哈希函数，`put()`和`get()`方法可以在常数时间内完成。但在对*HashMap*进行迭代时，需要遍历整个table以及后面跟的冲突链表。因此对于迭代比较频繁的场景，不宜将*HashMap*的初始大小设的过大。

有两个参数可以影响*HashMap*的性能: 初始容量(inital capacity)和负载系数(load factor)。初始容量指定了初始`table`的大小，负载系数用来指定自动扩容的临界值。当`entry`的数量超过`capacity*load_factor`时，容器将自动扩容并重新哈希。对于插入元素较多的场景，将初始容量设大可以减少重新哈希的次数。

将对象放入到*HashMap*或*HashSet*中时，有两个方法需要特别关心: `hashCode()`和`equals()`。**`hashCode()`方法决定了对象会被放到哪个`bucket`里，当多个对象的哈希值冲突时，`equals()`方法决定了这些对象是否是“同一个对象”**。所以，如果要将自定义的对象放入到`HashMap`或`HashSet`中，需要*@Override*`hashCode()`和`equals()`方法。



#### get()

 

`get(Object key)`方法根据指定的`key`值返回对应的`value`，该方法调用了`getEntry(Object key)`得到相应的`entry`，然后返回`entry.getValue()`。因此`getEntry()`是算法的核心。 算法思想是首先通过`hash()`函数得到对应`bucket`的下标，然后依次遍历冲突链表，通过`key.equals(k)`方法来判断是否是要找的那个`entry`。

![HashMap_getEntry](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\HashMap_getEntry.png)







------

​	**JDK8**:

jdk8中，采用了  数组+链表+红黑树 的形式，优化了jdk7中  数据量过大时链表查询慢  等弊端（查找的时候，根据 hash 值我们能够快速定位到数组的具体下标，但是之后的话，需要顺着链表一个个比较下去才能找到我们需要的，时间复杂度取决于链表的长度，为 O(n)  ）。  默认当链表元素达到8个就  将链表转换成红黑树。 这样在查询的时候可以降低时间复杂度为 O(log N)



p.s:这里还需知道，当数据量过大时，哈希表会进行自动扩容，而后在hash方法中获取的“桶”数组下标的范围将更大，所以一般不会出现很长的链表、红黑树的情况。

![](C:\Users\AWU\Desktop\面试学习\集合类\JAVA集合文档图片\java-collection-hashmap8.png)

```
/**
* 这是 jdk8版本的 HashMap
**/

public V get(Object key) {
        Node<K,V> e;
        return (e = getNode(hash(key), key)) == null ? null : e.value;
    }
    
    //Node内部类
    static class Node<K,V> implements Map.Entry<K,V> {
        final int hash;
        final K key;
        V value;
        Node<K,V> next;

        Node(int hash, K key, V value, Node<K,V> next) {
            this.hash = hash;
            this.key = key;
            this.value = value;
            this.next = next;
        }
        
        ...
        
       }
```



jdk8中的  put()方法分析：

```java
public V put(K key, V value) {
    return putVal(hash(key), key, value, false, true);
}

// 第四个参数 onlyIfAbsent 如果是 true，那么只有在不存在该 key 时才会进行 put 操作
// 第五个参数 evict 我们这里不关心
final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
               boolean evict) {
    Node<K,V>[] tab; Node<K,V> p; int n, i;
    // 第一次 put 值的时候，会触发下面的 resize()，类似 java7 的第一次 put 也要初始化数组长度
    // 第一次 resize 和后续的扩容有些不一样，因为这次是数组从 null 初始化到默认的 16 或自定义的初始容量
    if ((tab = table) == null || (n = tab.length) == 0)
        n = (tab = resize()).length;
    // 找到具体的数组下标，如果此位置没有值，那么直接初始化一下 Node 并放置在这个位置就可以了
    if ((p = tab[i = (n - 1) & hash]) == null)
        tab[i] = newNode(hash, key, value, null);

    else {// 数组该位置有数据
        Node<K,V> e; K k;
        // 首先，判断该位置的第一个数据和我们要插入的数据，key 是不是"相等"，如果是，取出这个节点
        if (p.hash == hash &&
            ((k = p.key) == key || (key != null && key.equals(k))))
            e = p;
        // 如果该节点是代表红黑树的节点，调用红黑树的插值方法，本文不展开说红黑树
        else if (p instanceof TreeNode)
            e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
        else {
            // 到这里，说明数组该位置上是一个链表
            for (int binCount = 0; ; ++binCount) {
                // 插入到链表的最后面(Java7 是插入到链表的最前面)
                if ((e = p.next) == null) {
                    p.next = newNode(hash, key, value, null);
                    // TREEIFY_THRESHOLD 为 8，所以，如果新插入的值是链表中的第 8 个
                    // 会触发下面的 treeifyBin，也就是将链表转换为红黑树
                    if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                        treeifyBin(tab, hash);
                    break;
                }
                // 如果在该链表中找到了"相等"的 key(== 或 equals)
                if (e.hash == hash &&
                    ((k = e.key) == key || (key != null && key.equals(k))))
                    // 此时 break，那么 e 为链表中[与要插入的新值的 key "相等"]的 node
                    break;
                p = e;
            }
        }
        // e!=null 说明存在旧值的key与要插入的key"相等"
        // 对于我们分析的put操作，下面这个 if 其实就是进行 "值覆盖"，然后返回旧值
        if (e != null) {
            V oldValue = e.value;
            if (!onlyIfAbsent || oldValue == null)
                e.value = value;
            afterNodeAccess(e);
            return oldValue;
        }
    }
    ++modCount;
    // 如果 HashMap 由于新插入这个值导致 size 已经超过了阈值，需要进行扩容
    if (++size > threshold)
        resize();
    afterNodeInsertion(evict);
    return null;
}

```



get()等方法均类似，这里不做叙述。









### [¶](#hashtable) 3.HashTable

和 HashMap 类似，但它是线程安全的，这意味着同一时刻多个线程可以同时写入 HashTable 并且不会导致数据不一致。它是遗留类，不应该去使用它。现在可以使用 ConcurrentHashMap 来支持线程安全，并且 ConcurrentHashMap 的效率会更高，因为 ConcurrentHashMap 引入了分段锁。

### [¶](#linkedhashmap) 4.LinkedHashMap

使用双向链表来维护元素的顺序，顺序为插入顺序或者最近最少使用(LRU)顺序

















































