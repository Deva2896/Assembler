%macro first 2
	mov eax,%1
	mov ebx,%2
	add eax,ebx
%endmacro
%macro second 2
	first 60,20
	push eax 
	push ans
	call printf
	add esp,8
%endmacro

section .data
	ans db "addition Is=%d",10,0
section .text
	global main
	extern printf
main:
	second 10,20
	push eax 
	push ans
	call printf
	add esp,8


	
	

