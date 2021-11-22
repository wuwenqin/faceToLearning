// ���Ͷ�.cpp : �������̨Ӧ�ó������ڵ㡣
//�ͻ��� client

#include "stdafx.h"

//ͷ�ļ�
#include <WinSock2.h>
//��̬��
#pragma comment(lib,"ws2_32.lib")


int _tmain(int argc, _TCHAR* argv[])
{
	//1 ����汾
	WSADATA wsaData;
	WSAStartup(MAKEWORD(2, 2), &wsaData);
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

	//4 ���ӷ�����
	int r = connect(serverSocket, (sockaddr*)&addr, sizeof addr);
	if (r == SOCKET_ERROR){
		printf("���ӷ���������!\n");
		return -2;
	}
	printf("���ӷ������ɹ�!\n");

	//5����
#if 0
	char buff[1024];
	while (1){
		printf("������:");
		scanf("%s",buff);
		send(serverSocket, buff, strlen(buff), NULL);
	}
#endif

	char fileName[256] = { 0 };
	printf("�������ļ���:");
	scanf("%s", fileName);
	r = send(serverSocket, fileName, strlen(fileName), NULL);
	if (r > 0){
		printf("�ļ������ͳɹ�!\n");
	}

	//���ļ�
	FILE* fp = fopen(fileName, "rb");//����ʽ���ļ�  �ֽ�
	int size;
	//��ȡ�ļ���С
	fseek(fp, 0, SEEK_END);//���ļ�����ָ�붨λ���ļ�ĩβ
	size = ftell(fp);//�����ļ�����ָ�뵽�ļ�ͷ�ĳ���
	fseek(fp, 0, SEEK_SET);//�ļ�����ָ�붨λ���ļ�ͷ
	//�����ļ���С
	r = send(serverSocket,(char*)&size,4,NULL);
	if (r > 0){
		printf("�ļ���С���ͳɹ�!\n");
	}
	//�����ļ�
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

	//�ر��ļ�
	fclose(fp);

	while (1);
	return 0;
}

