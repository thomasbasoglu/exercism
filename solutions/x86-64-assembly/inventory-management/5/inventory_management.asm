; Everything that comes after a semicolon (;) is a comment

WEIGHT_OF_EMPTY_BOX equ 500
TRUCK_HEIGHT equ 300
PAY_PER_BOX equ 5
PAY_PER_TRUCK_TRIP equ 220

section .text

; You should implement functions in the .text section
; A skeleton is provided for the first function

; the global directive makes a function visible to the test files
global get_box_weight
get_box_weight:
    ; This function takes the following parameters:
    ; - The number of items for the first product in the box, as a 16-bit non-negative integer
    ; - The weight of each item of the first product, in grams, as a 16-bit non-negative integer
    ; - The number of items for the second product in the box, as a 16-bit non-negative integer
    ; - The weight of each item of the second product, in grams, as a 16-bit non-negative integer
    ; The function must return the total weight of a box, in grams, as a 32-bit non-negative integer
    ; Changing all the values to 64 bit 
    mov edi, edi    
    mov esi, esi    
    mov edx, edx    
    mov ecx, ecx
    
    mov rax, WEIGHT_OF_EMPTY_BOX ; add box weight to the return value
    
    imul rdi, rsi ; getting first argument times the second 
    add rax, rdi ; adding to the result 

    imul rdx, rcx ; getting third argument times the fourth 
    add rax, rdx ; adding to the result 
     
    ret

global max_number_of_boxes
max_number_of_boxes:
    ; TODO: define the 'max_number_of_boxes' function
    ; This function takes the following parameter:
    ; - The height of the box, in centimeters, as a 8-bit non-negative integer
    ; The function must return how many boxes can be stacked vertically, as a 8-bit non-negative integer
    mov ax, TRUCK_HEIGHT
    idiv dil ; Divide the cm to the max_height then we can get how many boxes we can fit
    movzx eax, al 
    ret

global items_to_be_moved
items_to_be_moved:
    ; TODO: define the 'items_to_be_moved' function
    ; This function takes the following parameters:
    ; - The number of items still unaccounted for a product, as a 32-bit non-negative integer
    ; - The number of items for the product in a box, as a 32-bit non-negative integer
    ; The function must return how many items remain to be moved, after counting those in the box, as a 32-bit integer
    sub edi, esi
    mov eax, edi
    ret

global calculate_payment
calculate_payment:
    ; Move all the registers to 64 bit registers
    ; First 32bits mov 
    
    mov esi, esi ; Total boxes esi converted to rsi
    mov edx, edx ; Total trips converted edx to rdx 
    mov ecx, ecx ; Lost items ecx converted to rcx

    ; 8 bit to 64 with movzx 

    movzx r9, r9b

    ; Now operations 
    
    imul rsi, PAY_PER_BOX
    imul rdx, PAY_PER_TRUCK_TRIP
    add rdx, rsi        ; total cost
    
    imul rcx, r8        ; This is the total damage 
    
    sub rsi, rdi        ; Price after we subtract the payment upfront 
    sub rsi, rcx        ; Price after damage 
    
    ; Final step division 
    mov rax, rsi
    cqo 
    idiv r9

    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
