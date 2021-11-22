// 发送端.cpp : 定义控制台应用程序的入口点。
//客户端 client

#include "stdafx.h"

//头文件
#include <WinSock2.h>
//静态库
#pragma comment(lib,"ws2_32.lib")


int _tmain(int argc, _TCHAR* argv[])
{
	//1 请求版本
	WSADATA wsaData;
	WSAStartup(MAKEWORD(2, 2), &wsaData);
	if (LOBYTE(wsaData.wVersion) != 2 || HIBYTE(wsaData.wVersion) != 2){
		printf("请求版本失败！\n");
		return -1;
	}
	printf("请求版本成功\n");

	//2 创建socket                 通信协议   通信载体   保护方式
	SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (serverSocket == INVALID_SOCKET){
		printf("创建socket失败!\n");
		return -1;
	}
	printf("创建socket成功!\n");

	//3 创建协议地址族
	SOCKADDR_IN addr = { 0 };
	addr.sin_family = AF_INET;
	addr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//ip地址
	addr.sin_port = htons(10086);//端口号

	//4 连接服务器
	int r = connect(serverSocket, (sockaddr*)&addr, sizeof addr);
	if (r == SOCKET_ERROR){
		printf("连接服务器出错!\n");
		return -2;
	}
	printf("连接服务器成功!\n");

	//5发送
#if 0
	char buff[1024];
	while (1){
		printf("请输入:");
		scanf("%s",buff);
		send(serverSocket, buff, strlen(buff), NULL);
	}
#endif

	char fileName[256] = { 0 };
	printf("请输入文件名:");
	scanf("%s", fileName);
	r = send(serverSocket, fileName, strlen(fileName), NULL);
	if (r > 0){
		printf("文件名发送成功!\n");
	}

	//打开文件
	FILE* fp = fopen(fileName, "rb");//读方式打开文件  字节
	int size;
	//获取文件大小
	fseek(fp, 0, SEEK_END);//把文件内容指针定位到文件末尾
	size = ftell(fp);//返回文件内容指针到文件头的长度
	fseek(fp, 0, SEEK_SET);//文件内容指针定位到文件头
	//发送文件大小
	r = send(serverSocket,(char*)&size,4,NULL);
	if (r > 0){
		printf("文件大小发送成功!\n");
	}
	//发送文件
	char buff[1024];
	while (1){
		memset(buff, 0, 1024);
		r = fread(buff, 1, 1024, fp);
		if (r > 0){
			send(serverSocket, buff, r, NULL);
		}
		else{
			break;
		}

	}

	//关闭文件
	fclose(fp);

	while (1);
	return 0;
}

