# 												PostMan相关



本次测试，是使用搭建在本地电脑中的项目进行的一个测试( IP为127.0.0.1，本地IP地址)。

首先，正常进行一次登录操作，可以看到对应的请求地址、请求头、请求数据等信息。

![正常登录的一些信息采集](C:\Users\AWU\Desktop\面试学习\PostMan相关图片存储池\正常登录的一些信息采集.jpg)



可以看到，请求地址是  http://localhost:8080/login，请求方法是Post方法。(在使用PostMan进行测试时，勿用Get方法进行请求，因为在本地项目的该接口中被我设置了是必须为Post方法请求。如果使用Get方法请求会出现405-方法不允许的问题)

​	项目中对应的登录接口简要如下：

```java
@RequestMapping(value = "login", method = {RequestMethod.POST})  //限制只能通过 POST 才能访问该接口
    public String selectUserByAcountOrPhone(@RequestParam("id") String id, @RequestParam("password") String password,
                                    @RequestParam("checkcode") String checkcode  ,HttpServletRequest request,HttpSession session) {
        
     ...   
    }
```

​		根据正常登录获得的cookie，与账号密码放入postman进行请求，会出现400的bug问题。对应在IDEA工具中可以看到，出现的bug为**MissingServletRequestParameterException**。这是一个缺失了某个请求参数的bug。

​		通过IDEA中的提示，可以看到是缺失了 验证码checkcode的参数，但使用postman不将checkcode参数避免开就无法实现请求了。那么，**为什么会有了Cookie还一定需要checkcode的参数请求呢？按理来说，有了cookie就类似于已经登录了，可以在下次登录的时候直接进入主界面。这里还是因为@RequestParam 这个注解的问题。**

![session存储](C:\Users\AWU\Desktop\面试学习\PostMan相关图片存储池\session存储.jpg)

​		补充：HTTP 400错误，出现这个请求无效报错说明该网址所请求的接口并未得到后台服务器的处理(换句话说，要么请求少了参数，要么多了参数，要么提交的数据类型不同  json/对象)



在SSM中，@RequestParam 注解是将 请求参数绑定到方法参数中，也就是说如果  验证码只是通过 @RequestParam("checkcode") 来绑定的话，就默认 请求参数必须存在该字段，否则会返回错误。可以查看如下源代码：

```java

@Target(ElementType.PARAMETER)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface RequestParam {

	 
	@AliasFor("name")
	String value() default "";

	 
	@AliasFor("value")
	String name() default "";

	 
	boolean required() default true;

	 
	String defaultValue() default ValueConstants.DEFAULT_NONE;

}
```

可以看到， @RequestParam 中的 required 默认为true;

所以至此，目前已发现解决问题的方法有如下两种：

​	（1） 为验证码是否必须  设为false即可。

​	（2）将方法改为 @ResponseBody 注解，使该方法返回一个json字符串。(若想返回网址，使用HttpServletResponse类中的重定向方法sendRedirect()即可  )

```java
@RequestMapping(value = "login", method = {RequestMethod.POST})  //限制只能通过 POST 才能访问该接口
    @ResponseBody
    public String selectUserByAcountOrPhone(String id, String password,
                                            String checkcode  , HttpServletRequest request, HttpSession session, HttpServletResponse response) throws IOException {
  
        
        ...
            //使用@ResponseBody注解后仍想返回一个网址，即使用重定向即可
  		response.sendRedirect(request.getContextPath()+"/index.jsp");

        
        
    }
```

这样，就能使用PostMan进行请求，并得到响应数据。

![@ResponseBody对应请求](C:\Users\AWU\Desktop\面试学习\PostMan相关图片存储池\@ResponseBody对应请求.png)









了解：https://blog.csdn.net/yezongzhen/article/details/104154434

在这里补充一点：使用@ResponseBody 注解，在注销时应移除原有的session值。

具体代码 ：

```java
@GetMapping("/logout")
	@ResponseBody
	public void logout( String username,String password,
			HttpServletRequest request,HttpServletResponse response) {
		//操作数据
		request.getSession().removeAttribute("sessionUser");
		//页面跳转
		try {
            //地址栏路径，再次请求登录
			response.sendRedirect(request.getContextPath()+"/login.jsp");
			
		} catch (IOException e) {
			
			e.printStackTrace();
		} 
		
	}
```



在这时，做一个拦截器类MyHandlerInterceptor：若用户未登录就返回到登录界面。

```java

import org.springframework.web.servlet.HandlerInterceptor;
import org.springframework.web.servlet.ModelAndView;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

public class MyHandlerInterceptor implements HandlerInterceptor {

    /**
     * 在执行handler前执行
     * 返回值：true，放行,false:拦截
     */

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        HttpSession session=request.getSession();
        String path=request.getRequestURI();
        if(path.indexOf("login")!=-1||path.indexOf("register")!=-1){
            return true;
        }
        else if(session.getAttribute("user")!=null){
            System.out.println("用户已经登录");
            return true;
        }else {
            response.setHeader("REDIRECT", "REDIRECT");
            response.setHeader("SESSIONSTATUS", "TIMEOUT");
            response.setHeader("CONTEXTPATH", request.getContextPath()+"/login.jsp");
            response.setStatus(HttpServletResponse.SC_FORBIDDEN);
            System.out.println(response.getHeader("REDIRECT")+response.getHeader("CONTEXTPATH"));
            response.sendRedirect(request.getContextPath()+"/login.jsp");
            System.out.println("用户没登录");
            return false;
        }
    }

    @Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) throws Exception {

    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) throws Exception {

    }
}

```

同时，也需要在配置文件spring-mvc.xml中加入配置信息：

```java
<mvc:interceptors>
        <mvc:interceptor>
            <mvc:mapping path="/**"/>
            <mvc:exclude-mapping path="login"/>
            <mvc:exclude-mapping path="register"/>
            <bean class="com.ssm.Interceptor.MyHandlerInterceptor"></bean>
        </mvc:interceptor>
    </mvc:interceptors>
```



















