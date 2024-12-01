	.file	"return2.i"
	.text
	.globl	main
	.type	main, @function
main:
	movl	$3, %eax
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 13.2.0-23ubuntu4) 13.2.0"
	.section	.note.GNU-stack,"",@progbits
