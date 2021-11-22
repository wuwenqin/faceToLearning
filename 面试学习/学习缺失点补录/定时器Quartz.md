# 											定时器学习



学习定时器之前需要有 一定的**理论基础**： **小顶堆 和 时间轮算法**

​		那么，**什么是小顶堆呢**？—— 首先，堆的定义是：堆是**一颗完全二叉树**，且堆中某个节点的值总是**不大于(或不小于)其父节点的值**。对此，根节点最大的堆叫做大顶堆，**根节点最小的堆叫做小顶堆。**

​		从上面小顶堆的定义需要知道，**什么是完全二叉树**？——它的定义是**除了最后一层外其他层都达到了最大节点数，且最后一层节点都靠左排列。**

​		那么，堆是**如何存储的**呢？—— 堆是一颗完全二叉树，但二叉树在Java中是逻辑结构，在Java中要么使用**数组**进行存储，要么使用**链表**进行存储。( 这里需要知道一个注意点，虽然Java中有实现了**树相关的类**，但通过源代码可以看到，**它们的数据结构均是封装了数组或链表**) 。

​		那么，**以数组为底的数据结构，如何进行查询父节点？**—— 创建 **一个 下标为0不进行数据存储的数组**，那么只要**将 当前元素的下标/2 即可得到父节点的下标**。

而以链表为底的数据结构，则**直接访问当前元素的父节点**即可。



既然上述的概念均以了解，那么接下来将**进行元素的插入、堆顶元素的删除，这该如何实现呢**？——

​		①进行**元素的插入**，首先必然需要继续满足堆的两个特性(完全二叉树以及小(大)顶堆)。如何实现这两个条件呢？可以通过将元素**尾插**到数组中( 尾插之前有**数组的扩容和拷贝的判定** )，再**判断是否上浮（判断该节点和父节点的值大小比较）**。简而言之就是**插入元素进行堆化(也被称为自下而上的堆化)**。

​		②进行 **堆顶元素的删除**，和插入同理，需要满足堆的两个特性。这里的实现是：**移除堆顶元素后，将数组尾部(最大元素) 放到堆顶，然后下沉。（下沉的思路是：若为小顶堆，则下沉时当与子节点较小的元素进行交换）**



通过上述定义，接下来需要知道**定时器和 小顶堆有什么联系呢**？——通过定义可知，小顶堆的元素可用**数组**进行存储，那么最小的根节点则会放在数组的首发之中，当堆需要推出一个元素(删除首元素)，那么它必定是**当前数组中的最小值**，这个**最小值可以认为**是任务将在什么时候(该元素的值)进行。也就是**最近将要执行的任务**。



上述的为小顶堆的定义。接下来将进行 **时间轮算法**的学习。



那么， **时间轮的含义**？—— 时间轮是**一种调度模型**，为高效解决调度任务而产生。

既然了解了含义，那么其**实现方式有哪些**呢？—— 

​	① **链表或数组实现时间轮**：while-true-sleep。遍历数组，每个下标放置一个链表，链表节点放置任务，遍历到了就取出执行。

​	② round型时间轮：任务上记录一个round，遍历到了就将round减一，为0时取出执行。但这样的缺点是——需要遍历所有任务，效率低下。

​	③ 分层时间轮：使用不同时间维度的轮——天轮（记录几点执行），月轮（记录几号执行）。月轮遍历到了，将任务取出放到天轮里面，即可实现几号几点执行。



------



## 1.JDK 定时器 ：Timer 使用及原理分析

​		① timer使用：

​		注意点：预设的执行时间 nextExecutTime 12:00:00  12:00:02 12:00:04 ...

​						schedule 真正的执行时间，取决上一个任务的结束时间， ExecutTime  03 05 08 ...   可能会出现 **丢任务(少执行了)**

​						scheduleAtFixedRate:严格按照预设时间， 12:00:00   12:00:02 ...(**执行时间会乱**)

```java

import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class TimerTest {

    public static void main(String[] args) {
        Timer t=new Timer();
        for (int i=0;i<2;i++){
            TimerTask task=new FooTimerTask("foo"+i);
            t.schedule(task,new Date(),2000);
        }
    }

}

 
class FooTimerTask extends TimerTask{

    private String name;

    public FooTimerTask(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public void run() {
        try {
            System.out.println("name="+name+",startTime="+new Date());
            Thread.sleep(3000);
            System.out.println("name="+name+",endTime="+new Date());

        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}

```



​		② timer 的数据结构和原理分析：

​		由下列源代码可看出，Timer类的数据结构主要是**以数组为存储结构的一个小顶堆**，逻辑结构上可以理解为一颗完全二叉树。

​		

```java
public class Timer {
   
    /**
    *定时器任务队列。 该数据结构与定时器线程共享。 定时器通过其各种调度调用产生任务，定时器线程消耗，适当地执行定时器任务，并在它们过时时将它们从队列中移除
    */
    private final TaskQueue queue = new TaskQueue();

    /**
     * The timer thread.
     */
    private final TimerThread thread = new TimerThread(queue);

    //调用schedule方法即可实现定时
    public void schedule(TimerTask task, long delay, long period) {
        if (delay < 0)
            throw new IllegalArgumentException("Negative delay.");
        if (period <= 0)
            throw new IllegalArgumentException("Non-positive period.");
        sched(task, System.currentTimeMillis()+delay, -period);
    }
    
    //调用schedule方法后被内部调用
    private void sched(TimerTask task, long time, long period) {
        if (time < 0)
            throw new IllegalArgumentException("Illegal execution time.");

        // Constrain value of period sufficiently to prevent numeric
        // overflow while still being effectively infinitely large.
        if (Math.abs(period) > (Long.MAX_VALUE >> 1))
            period >>= 1;

        //进行了双重检验
        synchronized(queue) {
            if (!thread.newTasksMayBeScheduled)
                throw new IllegalStateException("Timer already cancelled.");

            synchronized(task.lock) {
                if (task.state != TimerTask.VIRGIN)
                    throw new IllegalStateException(
                        "Task already scheduled or cancelled");
                task.nextExecutionTime = time;
                task.period = period;
                task.state = TimerTask.SCHEDULED;
            }

            queue.add(task);
            if (queue.getMin() == task)  //小顶堆的顶部元素
                queue.notify();  //唤醒
        }
    }

    //运行线程
    public void run() {
        try {
            mainLoop();
        } finally {
            // Someone killed this Thread, behave as if Timer cancelled
            synchronized(queue) {
                newTasksMayBeScheduled = false;
                queue.clear();  // Eliminate obsolete references
            }
        }
    }
    
    //run方法调用的mainLoop()
    private void mainLoop() {
        while (true) {
            try {
                TimerTask task;
                boolean taskFired;
                synchronized(queue) {
                    // Wait for queue to become non-empty
                    while (queue.isEmpty() && newTasksMayBeScheduled)
                        queue.wait();
                    if (queue.isEmpty())
                        break; // Queue is empty and will forever remain; die

                    // Queue nonempty; look at first evt and do the right thing
                    long currentTime, executionTime;
                    task = queue.getMin();
                    synchronized(task.lock) {
                        if (task.state == TimerTask.CANCELLED) {
                            queue.removeMin();
                            continue;  // No action required, poll queue again
                        }
                        currentTime = System.currentTimeMillis();
                        executionTime = task.nextExecutionTime;
                        if (taskFired = (executionTime<=currentTime)) {
                            if (task.period == 0) { // Non-repeating, remove
                                queue.removeMin();
                                task.state = TimerTask.EXECUTED;
                            } else { // Repeating task, reschedule
                                queue.rescheduleMin(
                                  task.period<0 ? currentTime   - task.period
                                                : executionTime + task.period);
                            }
                        }
                    }
                    if (!taskFired) // Task hasn't yet fired; wait
                        queue.wait(executionTime - currentTime);
                }
                if (taskFired)  // Task fired; run it, holding no locks
                    task.run();
            } catch(InterruptedException e) {
            }
        }
    }
}
    
    
    ...
}


//TimerThread是继承了Thread的线程类
class TimerThread extends Thread {
 ...   
}
    
//这里的TaskQueue基于上述中所讲的小顶堆思想
class TaskQueue {
    /**
    *优先级队列表示为一个平衡的二叉堆：queue[n] 的两个孩子是 queue[2*n] 和 queue[2*n+1]。 优先级队列在 nextExecutionTime 字段上排序：具有最低 nextExecutionTime 的 TimerTask 在 queue[1] 中（假设队列非空）。 对于堆中的每个节点 n，以及 n、d、n.nextExecutionTime <= d.nextExecutionTime 的每个后代。
    */
    private TimerTask[] queue = new TimerTask[128];
    
```

​		③ timer 中存在的问题：① 少执行(丢任务)   ② 执行时间紊乱

​		那么，这是**什么原因导致的**呢？—— 这是因为Timer是单线程的，但任务会进入队列中一个一个被顺序运行，会出现任务阻塞，从而出现任务超时。

​		④ timer 的 应用场景分析：闹钟等。



## 2.定时任务线程池  (ScheduledThreadPoolExecutor )

​	① 使用简介：

（1）通过下列源代码可以看出，**ScheduledThreadPoolExecutor**继承了ThreadPoolExecutor类，为任务提供了延迟或周期执行的方法。

（2）自封内部类 ScheduledFutureTask 执行周期任务。也可以接收不需要时间调度的任务。

（3）使用DelayedWorkQueue存储任务。一种无界延迟队列。

（4）支持线程池关闭后执行，课选择线程池关闭后支持继续执行周期或延迟任务。



该类中有两个内部类：1.ScheduledFutureTask:可以延迟执行的异步运算任务

2.DelayedWorkQueue:存储周期或延迟任务的延迟队列	



```java
//创建方式
ScheduledExecutorService scheduledThreadPool = Executors.newScheduledThreadPool(5);

```

```java
/**
*这是Executors中的方法
*
*创建一个单线程执行器，它可以安排命令在给定的延迟后运行，或定期执行。 （但是请注意，如果这个单线程在关闭之前的执行过程中由于失败而终止，如果需要执行后续任务，一个新线程将取而代之。）任务保证按顺序执行，并且不会超过一个任务处于活动状态在任何给定的时间。 与其他等效的newScheduledThreadPool(1) ，返回的执行程序保证不可重新配置以使用其他线程。
*/
public class Executors {

public static ScheduledExecutorService newSingleThreadScheduledExecutor() {
        return new DelegatedScheduledExecutorService
            (new ScheduledThreadPoolExecutor(1));
    }


}



public class ScheduledThreadPoolExecutor
        extends ThreadPoolExecutor
        implements ScheduledExecutorService {

/**
*ScheduledThreadPoolExecutor 中的构造方法
**/
public ScheduledThreadPoolExecutor(int corePoolSize) {
        super(corePoolSize, Integer.MAX_VALUE, 0, NANOSECONDS,
              new DelayedWorkQueue());
    }
     
    //静态内部类
    static class DelayedWorkQueue extends AbstractQueue<Runnable>
        implements BlockingQueue<Runnable> {

    }
    
    //私有内部类
        private class ScheduledFutureTask<V>
            extends FutureTask<V> implements RunnableScheduledFuture<V> {

        }
    
}
```

​	② 单线程版和多线程版：使用**多线程执行任务，不会相互阻塞**。单线程版的适用于**需要单个后台线程执行周期任务**，同时需要**保证任务顺序执行**。

​	③ 数据结构和原理分析：主要是以ScheduledThreadPoolExecutor类为核心的数据结构。其内部封装了DelayedWorkQueue和ScheduledFutureTask 两个内部类。

​	④ 应用场景：适用于多个后台线程执行周期性任务。同时满足资源管理的需求而限制后台线程数量。

​	⑤ Leader-Follower 模式：

比如当前有一堆等待执行的任务（一般存储在一个队列中并排序），而所有的工作线程中只有一个会是leader线程，其他线程都是follower线程。且只有leader线程能执行任务，而剩下的follower 线程不会执行任务，只能处于休眠状态。

避免没必要的唤醒和阻塞的操作，这样能更加有效且节省资源。





## 3.定时任务框架 Quartz

​	① 使用简介：什么是Quartz？——

```java
Quartz是OpenSymphony开源组织在Job scheduling领域又一个开源项目，完全由Java开发，可以用来执行定时任务，类似于java.util.Timer。但是相较于Timer， Quartz增加了很多功能：

持久性作业 - 就是保持调度定时的状态;
作业管理 - 对调度作业进行有效的管理;
 
```

使用场景：如火车票购票，若待支付的业务超过某个限制的时间还未支付则会取消此次订单。当你支付完成之后，后台拿到支付回调后就会再插入一条待消费的task（job），Job触发日期为火车票上的出发日期，超过这个时间就会执行这个job，判断是否使用等。也适用于每日提醒的闹钟类。





​		

​	② 各组件介绍

​		（1）调度器：Scheduler

​		（2）任务：JobDetail

​		（3）触发器：Trigger，包括SimpleTrigger和CronTrigger



​	③ 组件关系架构分析



如何使用Quartz来实现定时任务：

​		（1）首先需要定义实现一个定时功能的接口( 实现Quartz框架中的Job类)，即自定义的类Job(Task)

如定时发送邮件的task（Job），重启机器的task（Job），优惠券到期发送短信提醒的task（Job）

![Quartz的Job](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz的Job.png)

​			（2）有了Task(Job)后，需要一个能够实现触发后任务执行的触发器(Quartz框架中已有封装)。触发器最基本的功能是指定Job的执行时间，执行间隔以及运行次数等。

![Quartz框架的Trigger](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz框架的Trigger.png)

​			（3）有了Job任务以及Trigger 触发器，这时需要一个定时器Schedule 来将两者结合起来，指定Trigger去执行指定的 Job。

![Quartz框架的Scheduler](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz框架的Scheduler.png)



​	④ 监听器及插件



​	⑤ 核心参数：

​		Quartz框架中的几个重要参数：

​		(1) Job和JobDetail：

​			Job是Quartz中的一个接口，接口中只有execute()方法，通过实现接口重写此方法中的业务逻辑。

```java
public interface Job {
    
 void execute(JobExecutionContext context)
        throws JobExecutionException;   
}
```

​			JobDetail用来绑定Job，为Job实例提供许多属性，它是一个继承了序列化接口以及克隆接口的一个接口类( 接口可以多继承接口的特性 )：每次Scheduler调度执行一个Job的时候，首先会拿到对应的Job，然后创建该Job实例，再去执行Job中的execute()的内容，任务执行结束后，关联的Job对象实例会被释放，且会被JVM GC清除。

```java
public interface JobDetail extends Serializable, Cloneable {
	public JobKey getKey();
    public String getDescription();
    public Class<? extends Job> getJobClass();
    public JobDataMap getJobDataMap();
    public boolean isDurable();
    public boolean isPersistJobDataAfterExecution();
    public boolean isConcurrentExectionDisallowed();
    public boolean requestsRecovery();
    public Object clone();
    public JobBuilder getJobBuilder();    
}
```

这里有一个问题，为什么不直接使用Job ，而是建议使用JobDetail+Job？——

​	JobDetail定义的是任务数据，而真正的执行逻辑是在Job中。这是因为任务是有可能并发执行，如果Scheduler直接使用Job，就会存在对同一个Job实例并发访问的问题。而JobDetail & Job 方式，Sheduler每次执行，都会根据JobDetail创建一个新的Job实例，这样就可以规避并发访问的问题。




​		(2) JobExecutionContext

​		JobExecutionContext中包含了Quartz运行时的环境以及Job本身的详细数据信息。当Schedule调度执行一个Job的时候，就会将JobExecutionContext传递给该Job的execute()中，Job就可以通过JobExecutionContext对象获取信息。
 ![Quartz的JobExecutionContext](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz的JobExecutionContext.png)



​		通过使用了CopyOnWriteArrayList类进行类的并发安全( 这个将在接下来的线程安全详细学习，在此不多叙述) ，且重写了 Job类的 execute( JobExecutionContext jobExecutionContext ) 方法 作为抽象Job类。( 这里主要是实现读写安全 )

![Quartz重写Job](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz重写Job.jpg)

如图，是定时任务的具体实现。

![Quartz的定时任务实现](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz的定时任务实现.png)

​		(3) JobDataMap

​	JobDataMap实现了JDK的Map接口（间接实现），可以以Key-Value的形式存储数据。
​	JobDetail、Trigger都可以使用JobDataMap来设置一些参数或信息，
​	Job执行execute()方法的时候，JobExecutionContext可以获取到JobExecutionContext中的信息：

 

```java
JobDetail jobDetail = JobBuilder.newJob(PrintWordsJob.class)                        .usingJobData("jobDetail1", "这个Job用来测试的")
                  .withIdentity("job1", "group1").build();

 Trigger trigger = TriggerBuilder.newTrigger().withIdentity("trigger1", "triggerGroup1")
      .usingJobData("trigger1", "这是jobDetail1的trigger")
      .startNow()//立即生效
      .withSchedule(SimpleScheduleBuilder.simpleSchedule()
      .withIntervalInSeconds(1)//每隔1s执行一次
      .repeatForever()).build();//一直执行

```

```java
	//部分代码：
public class JobDataMap extends StringKeyDirtyFlagMap implements Serializable {

    private static final long serialVersionUID = -6939901990106713909L;
  
        public JobDataMap() {
        super(15);
    }
   public JobDataMap(Map<?, ?> map) {
        this();
        @SuppressWarnings("unchecked") // casting to keep API compatible and avoid compiler errors/warnings.
        Map<String, Object> mapTyped = (Map<String, Object>)map;
        putAll(mapTyped);

        // When constructing a new data map from another existing map, we should NOT mark dirty flag as true
        // Use case: loading JobDataMap from DB
        clearDirtyFlag();
    }     
        
  
    //其他功能代码不在此叙述
}   
        
        
        
        
```

![Quartz的JobDataMap](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Quartz的JobDataMap.png)



​		(4) Trigger、SimpleTrigger、CronTrigger

​		Trigger是Quartz的触发器，会去通知Scheduler何时去执行对应Job

```java
new Trigger().startAt():表示触发器首次被触发的时间;
new Trigger().endAt():表示触发器结束触发的时间;
```

​		SimpleTrigger可以实现在一个指定时间段内执行一次作业任务或一个时间段内多次执行作业任务。
下面的程序就实现了程序运行5s后开始执行Job，执行Job 5s后结束执行：

```java
Date startDate = new Date();
startDate.setTime(startDate.getTime() + 5000);

 Date endDate = new Date();
 endDate.setTime(startDate.getTime() + 5000);

        Trigger trigger = TriggerBuilder.newTrigger().withIdentity("trigger1", "triggerGroup1")
                .usingJobData("trigger1", "这是jobDetail1的trigger")
                .startNow()//立即生效
                .startAt(startDate)
                .endAt(endDate)
                .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                .withIntervalInSeconds(1)//每隔1s执行一次
                .repeatForever()).build();//一直执行

```

​		CronTrigger功能非常强大，是基于日历的作业调度，而SimpleTrigger是精准指定间隔，所以相比SimpleTrigger，CroTrigger更加常用。CroTrigger是基于Cron表达式的，先了解下Cron表达式：

​		由7个子表达式组成字符串的，格式如下：

​		[秒] [分] [小时] [日] [月] [周] [年]

​		Cron表达式的语法比较复杂，
​		如：* 30 10 ? * 1/5 *
​		表示（从后往前看）
​		[指定年份] 的[ 周一到周五][指定月][不指定日][上午10时][30分][指定秒]

​		又如：00 00 00 ？ * 10,11,12 1#5 2018
​		表示2018年10、11、12月的第一周的星期五这一天的0时0分0秒去执行任务。


 		可通过在线生成Cron表达式的工具：http://cron.qqe2.com/ 来生成自己想要的表达式。

![Cron表达式学习](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Cron表达式学习.png)





​	⑥ springboot整合 Quartz

​	https://blog.csdn.net/chenmingxu438521/article/details/94485695



架构：

![Springboot整合Quartz(1)](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Springboot整合Quartz(1).png)

代码：

QuratzConfig.java类

```java

import com.blogspringboot.test.quartz.job.DateTimeJob;
import org.quartz.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class QuartzConfig {
    @Bean
    public JobDetail printTimeJobDetail(){
        return JobBuilder.newJob(DateTimeJob.class)//PrintTimeJob我们的业务类
                .withIdentity("DateTimeJob")//可以给该JobDetail起一个id
                //每个JobDetail内都有一个Map，包含了关联到这个Job的数据，在Job类中可以通过context获取
                .usingJobData("msg", "Hello Quartz")//关联键值对
                .storeDurably()//即使没有Trigger关联时，也不需要删除该JobDetail
                .build();
    }
    @Bean
    public Trigger printTimeJobTrigger() {
        CronScheduleBuilder cronScheduleBuilder = CronScheduleBuilder.cronSchedule("0/1 * * * * ?");
        return TriggerBuilder.newTrigger()
                .forJob(printTimeJobDetail())//关联上述的JobDetail
                .withIdentity("quartzTaskService")//给Trigger起个名字
                .withSchedule(cronScheduleBuilder)
                .build();
    }
}

```

```java
//DateTimeJob类，继承了QuartzJobBean，而QuartzJobBean实现了Job接口，相当于是间接实现了Job，Job接口里只有一个 void方法 execute()
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;
import org.springframework.scheduling.quartz.QuartzJobBean;

import java.text.SimpleDateFormat;
import java.util.Date;

public class DateTimeJob extends QuartzJobBean {

    @Override
    protected void executeInternal(JobExecutionContext jobExecutionContext) throws JobExecutionException {
        //获取JobDetail中关联的数据
        String msg = (String) jobExecutionContext.getJobDetail().getJobDataMap().get("msg");
        System.out.println("current time :"+new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date()) + "---" + msg);
    }
}
```

之后启动 @SpringbootApplication 注解所在的类即可实现。

![Springboot整合Quartz(2)](C:\Users\AWU\Desktop\面试学习\定时器学习图片存储池\Springboot整合Quartz(2).png)







