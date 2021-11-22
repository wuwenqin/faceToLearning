// ���ն�.cpp : �������̨Ӧ�ó������ڵ㡣
//  ������ server

#include "stdafx.h"
//ͷ�ļ�
#include <WinSock2.h>
//��̬��
#pragma comment(lib,"ws2_32.lib")

int _tmain(int argc, _TCHAR* argv[])
{
	//1 ����汾
	WSADATA wsaData;
	WSAStartup(MAKEWORD(2,2), &wsaData);
	if (LOBYTE(wsaData.wVersion) != 2 || HIBYTE(wsaData.wVersion) != 2){
		printf("����汾ʧ�ܣ�\n");
		return -1;
	}
       printf("����汾�ɹ�\n");

	//2 ����socket                 ͨ��Э��   ͨ������   ������ʽ
	SOCKET serverSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
	if (serverSocket == INVALID_SOCKET){
		printf("����socketʧ��!\n");
		return -1;
	}
	printf("����socket�ɹ�!\n");
	
	//3 ����Э���ַ��
	SOCKADDR_IN addr = { 0 };
	addr.sin_family = AF_INET;
	addr.sin_addr.S_un.S_addr = inet_addr("127.0.0.1");//ip��ַ
	addr.sin_port = htons(10086);//�˿ں�

	//4 ��
	int r = bind(serverSocket, (sockaddr*)&addr, sizeof addr);
	if (r == INVALID_SOCKET){
		printf("bindʧ��!\n");
		return -1;
	}
	printf("bind�ɹ�!\n");

	//5 ����
	r = listen(serverSocket,10);
	if (r == INVALID_SOCKET){
		printf("listenʧ��!\n");
		return -1;
	}
	printf("listen�ɹ�!\n");
	//6 ���ܿͻ�������
	SOCKET clientSocket = accept(serverSocket, 0, 0);
	if (clientSocket == SOCKET_ERROR){
		printf("�ͻ��˳���!\n");
		return -2;
	}
	printf("�ͻ������ӷ������ɹ�!\n");

	//7 ����
#if 0
	char buff[1024];
	while (1){
		memset(buff, 0, 1024);//�������
		r = recv(clientSocket, buff, 1023, NULL);//�ӿͻ��˽�������
		if (r > 0) {//���յ�����
			printf(">>%s\n", buff);//��ӡ
		}
 }
#endif

	char fileName[256] = { 0 };
	r = recv(clientSocket, fileName, 255, NULL);
	if (r > 0){
		printf("���յ��ļ�����%s\n", fileName);
	}
	int size = 0;
	r = recv(clientSocket,(char*)&size,4,NULL);
	if (r > 0){
		printf("���յ��ļ���С:%d\n", size);
	}
	FILE*fp = fopen(fileName, "wb");
	int count = 0;
	char buff[1024];
	while (1){
		memset(buff, 0, 1024);
		r = recv(clientSocket, buff, 1024, NULL);//��������
		if (r > 0){
			count += r;
			fwrite(buff, 1, r, fp);//д���ļ�
			if (count >= size){
				printf("�ļ��������!\n");
				break;
			}
		}
	}
	fclose(fp);

	while (1);
	return 0;
}

