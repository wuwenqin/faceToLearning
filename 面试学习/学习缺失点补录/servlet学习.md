# 											servlet学习

### 一.Servlet基本认识

##### 	① Servlet 是Sun公司提供的一门用于开发动态web资源的技术。

##### 	② 什么是Servlet?  

​		 1.servlet 是**JavaEE规范之一**，规范就是接口。(如下源代码可见)

​		2.Servlet 是javaWeb的三大组件之一。三大组件分别是：**Servlet程序，Filter		过滤器，Listener监听器。**

​		3.Servlet是Java Servlet 的简称，称为小服务程序或服务连接器，用**java编写的服务端程序**，具有独立平台和协议的特性，主要功能在于交互式地浏览和生成数据，生成动态Web内容，它通常**通过HTTP超文本传输协议来接收客户端发送过来的请求，并作出响应返回数据给客户端**。



​	     有关 Servlet的**注意事项**：由于不能实例化接口，故若要实现此接口，可以编写**一个extends(扩展、继承) GenericServlet的一个Servlet类(自定)，或者编写一个extends(扩展、继承) HttpServlet 的Http  servlet类。**

![Servlet类结构图](C:\Users\AWU\Desktop\面试学习\Servlet学习图片存储池\Servlet类结构图.png)

```java
public abstract class GenericServlet 
    implements Servlet, ServletConfig, java.io.Serializable{
    ...
}

public abstract class HttpServlet extends GenericServlet
{
    
    private static final String METHOD_DELETE = "DELETE";
    private static final String METHOD_HEAD = "HEAD";
    private static final String METHOD_GET = "GET";
    private static final String METHOD_OPTIONS = "OPTIONS";
    private static final String METHOD_POST = "POST";
    private static final String METHOD_PUT = "PUT";
    private static final String METHOD_TRACE = "TRACE";

    private static final String HEADER_IFMODSINCE = "If-Modified-Since";
    private static final String HEADER_LASTMOD = "Last-Modified";
    
    private static final String LSTRING_FILE =
        "javax.servlet.http.LocalStrings";
    private static ResourceBundle lStrings =
        ResourceBundle.getBundle(LSTRING_FILE);
   
}
```



​	    Servlet接口定义了初始化servlet的方法，为请求提供服务的方法和从服务器移除servlet的方法。这些方法称为生命周期方法，它们是按以下顺序调用：

​	(1) 构造servlet，使用**init方法初始化。**

​	(2) 处理来自客户端的对**service方法的所有调用。**

​	(3) 从服务中取出servlet，使用**destroy方法销毁**，最后进行垃圾回收并终止它。



```java
public interface Servlet {
	/**servlet 容器在实例化 servlet 后只调用一次init方法。 在 		*servlet 可以接收任何请求之前， init方法必须成功完成。
	*如果init方法，servlet 容器不能将 servlet 置于服务中
	*抛出一个ServletException
	*在 Web 服务器定义的时间段内不返回
	**/
        public void init(ServletConfig config) throws ServletException;

    
        public ServletConfig getServletConfig();

    /**
    *由 servlet 容器调用以允许 servlet 响应请求。
	*此方法仅在 servlet 的init()方法成功完成后调用。
	*对于抛出或发送错误的 servlet，应始终设置响应的状态代码。
	*Servlet 通常在可以同时处理多个请求的多线程 servlet 容器中运		*行。开发人员必须注意同步对任何共享资源（例如文件、网络连接以	*及servlet 的类和实例变量）的访问。
    */
    
        public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException;

	/**
	*由 servlet 容器调用以向 servlet 指示 servlet 正在停止服务。 	 *只有在 servlet 的service方法中的所有线程都退出或超时时间过		*后，才会调用此方法。 servlet 容器调用此方法后，将不会在此 		*servlet 上	再次调用service方法。
	*此方法使 servlet 有机会清理任何被占用的资源（例如，内存、文件	*句柄、线程）并确保任何持久状态与 servlet 在内存中的当前状态同	*步。
	*/
        public void destroy();

    
}
```



##### 	③ Servlet的核心作用？

​		(1) 接受客户端请求，完成service操作任务

​		(2) 动态生成网页(网页数据可变)

​		(3) 将包含操作结果的动态网页响应给客户端



##### ④ Servlet的运行过程？(面试问题)

​		Servlet程序是由WEB服务器调用，WEB服务器收到客户端的Servlet访问请求后：

​		(1) Web服务器首先检查是否已经装载并创建了该Servlet的实例对象(是否new了Servlet并分配地址)，如果是则执行第4步，否则执行第2步

​		(2) 装载并创建该Servlet的一个实例对象。

​		(3) 调用Servlet实例对象的init() 方法。

​		(4) 创建一个用于封装HTTP请求消息的HttpServletRequest对象和一个代表HTTP响应消息的HttpServletResponse对象。然后调用Servlet的service() 方法并将请求和响应对象作为参数传递进去。如下HttpServlet类中的service()方法：

```java
protected void service(HttpServletRequest req, HttpServletResponse resp)
        throws ServletException, IOException
    {
        String method = req.getMethod();

        if (method.equals(METHOD_GET)) {
            long lastModified = getLastModified(req);
            if (lastModified == -1) {
                // servlet doesn't support if-modified-since, no reason
                // to go through further expensive logic
                doGet(req, resp);
            } else {
                long ifModifiedSince = req.getDateHeader(HEADER_IFMODSINCE);
                if (ifModifiedSince < lastModified) {
                    // If the servlet mod time is later, call doGet()
                    // Round down to the nearest second for a proper compare
                    // A ifModifiedSince of -1 will always be less
                    maybeSetLastModified(resp, lastModified);
                    doGet(req, resp);
                } else {
                    resp.setStatus(HttpServletResponse.SC_NOT_MODIFIED);
                }
            }

        } else if (method.equals(METHOD_HEAD)) {
            long lastModified = getLastModified(req);
            maybeSetLastModified(resp, lastModified);
            doHead(req, resp);

        } else if (method.equals(METHOD_POST)) {
            doPost(req, resp);
            
        } else if (method.equals(METHOD_PUT)) {
            doPut(req, resp);
            
        } else if (method.equals(METHOD_DELETE)) {
            doDelete(req, resp);
            
        } else if (method.equals(METHOD_OPTIONS)) {
            doOptions(req,resp);
            
        } else if (method.equals(METHOD_TRACE)) {
            doTrace(req,resp);
            
        } else {
            //
            // Note that this means NO servlet supports whatever
            // method was requested, anywhere on this server.
            //

            String errMsg = lStrings.getString("http.method_not_implemented");
            Object[] errArgs = new Object[1];
            errArgs[0] = method;
            errMsg = MessageFormat.format(errMsg, errArgs);
            
            resp.sendError(HttpServletResponse.SC_NOT_IMPLEMENTED, errMsg);
        }
    }
```



##### 	⑤ Servlet核心目录结构

```java
—web ：存放需要部署的网站项目

——WEB-INF ：核心内容，分别是以下内容

———classes ：存放.class文件（XxxServlet.class）

———lib ：储存所需jar包

———web.xml ：web配置文件

——index.html/index.jsp.index.css/images等

见idea目录结构如下图： （因为idea会自动处理部署的文件并打包成war包的形式储存在out文件中，所以我们在使用IDEA时不用自己创建classes文件）
```


 ![Servlet核心目录结构](C:\Users\AWU\Desktop\面试学习\Servlet学习图片存储池\Servlet核心目录结构.png)



⑥ web.xml配置文件添加配置信息(这是有关Servlet的配置信息，SpringMVC会略有不同)

```java
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
         version="4.0">
	<!--下面两个标签，写在web-app标签内-->
	<!--Servlet配置-->
    <servlet>
        <!--Servlet的全称类名，通过名称找到对应的Servlet，因为的配置文件中可能存在很多Servlet，他需要一个可识别的名称标签-->
        <servlet-name>myservlet</servlet-name>
        <!--访问实际的类，这里需要写全限定名-->
        <servlet-class>com.mylifes1110.java.MyServlet</servlet-class>
    </servlet>
	<!--映射配置  -->
    <servlet-mapping>
        <!--同上，Servlet名称-->
        <servlet-name>myservlet</servlet-name>
        <!--URL路径访问名称，比如：localhost:8080/firstservlet/test（这里访问就需要在地址栏上假如test）-->
        <url-pattern>/test</url-pattern>
    </servlet-mapping>
</web-app>

```

##### 补充点：

		/**
	     * 利用流输出信息在浏览器内显示
	     * 解决浏览器显示乱码问题
	     */
	    servletResponse.setContentType("text/html;charset=utf-8");
	    servletResponse.getWriter().println("Servlet学习");




### 二. Servlet的使用

##### 	① 如何使用Servlet呢？

​		由于Servlet被定义成一个接口，不能直接实例化成对象，那么就要通过继承了它的实现类来进行实例化。那么将有下面三种方法：	

​		**实现Servlet接口、继承GenericServlet 抽象类、继承HttpServlet 抽象类。**

​	那么，上述实现方法中**有什么区别**呢？

​		可以看到，如果**实现Servlet接口来使用Servlet，可以看到Servlet接口中有5个方法：初始化、获取配置、提供服务、返回信息以及销毁。**(可以在 一.Servlet基本认识中的第二点查看Servlet接口)。但对于开发者来说，这5个方法中不是全部必须实现的方法。因此，在这个层面上考虑，可以通过优化把某个方法封装来实现复用，例如**封装初始化init()和destroy()方法来实现多个Servlet之间复用**。从而出现了下面即将叙述的GenericServlet抽象类。

​		关于GenericServlet类，GenericServlet实际上是一个实现了Servlet接口的类，并重写了初始化、获取配置、返回信息、销毁方法。而有关返回Servlet的相关信息的方法getServletInfo() 在源码中如下：

```java
public String getServletInfo() {
	return "";
    }
```

如上，可了解到GenericServlet类重写了想要简化的方法并返回默认空值。



