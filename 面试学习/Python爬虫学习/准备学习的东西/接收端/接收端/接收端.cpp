// 接收端.cpp : 定义控制台应用程序的入口点。
//  服务器 server

#include "stdafx.h"
//头文件
#include <WinSock2.h>
//静态库
#pragma comment(lib,"ws2_32.lib")

int _tmain(int argc, _TCHAR* argv[])
{
	//1 请求版本
	WSADATA wsaData;
	WSAStartup(MAKEWORD(2,2), &wsaData);
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

	//4 绑定
	int r = bind(serverSocket, (sockaddr*)&addr, sizeof addr);
	if (r == INVALID_SOCKET){
		printf("bind失败!\n");
		return -1;
	}
	printf("bind成功!\n");

	//5 监听
	r = listen(serverSocket,10);
	if (r == INVALID_SOCKET){
		printf("listen失败!\n");
		return -1;
	}
	printf("listen成功!\n");
	//6 接受客户端连接
	SOCKET clientSocket = accept(serverSocket, 0, 0);
	if (clientSocket == SOCKET_ERROR){
		printf("客户端出错!\n");
		return -2;
	}
	printf("客户端连接服务器成功!\n");

	//7 接受
#if 0
	char buff[1024];
	while (1){
		memset(buff, 0, 1024);//清空数组
		r = recv(clientSocket, buff, 1023, NULL);//从客户端接收数据
		if (r > 0) {//接收到数据
			printf(">>%s\n", buff);//打印
		}
 }
#endif

	char fileName[256] = { 0 };
	r = recv(clientSocket, fileName, 255, NULL);
	if (r > 0){
		printf("接收到文件名：%s\n", fileName);
	}
	int size = 0;
	r = recv(clientSocket,(char*)&size,4,NULL);
	if (r > 0){
		printf("接收到文件大小:%d\n", size);
	}
	FILE*fp = fopen(fileName, "wb");
	int count = 0;
	char buff[1024];
	while (1){
		memset(buff, 0, 1024);
		r = recv(clientSocket, buff, 1024, NULL);//接受数据
		if (r > 0){
			count += r;
			fwrite(buff, 1, r, fp);//写入文件
			if (count >= size){
				printf("文件接收完毕!\n");
				break;
			}
		}
	}
	fclose(fp);

	while (1);
	return 0;
}

