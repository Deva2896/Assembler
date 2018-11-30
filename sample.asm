section .data
	
	sen2 dd 30,40,50,60
	sen3 dq 50,60,70
	sen4 dw 100
	sen1 db "string",10,0
section .bss
	a resb 4
	b resq 6
	c resd 10
	zz resw 10
section .text
	global main
	extern printf
main:	xor ecx,ecx	
	mov esi, 2
	mov eax, sen

abc:	mov ebx, eax
	dec ebx
	push ebx
	xor edx, edx
	xor ecx, ecx

	xor ecx, ecx
	xor edx, edx
	
pqr:	cmp byte[eax],'f'
	jz abc
	cmp byte[eax],'m'
	jz xyz
	inc eax
	inc ecx
	jz tst
	jmp pqr

xyz:	pop ebx
	inc ebx
	inc ebx
	inc ebx
	xor eax, eax
	xor edx, edx
	mov eax, ebx
	xor ecx, ecx
	push eax


