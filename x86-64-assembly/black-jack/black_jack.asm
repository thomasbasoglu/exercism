; Everything that comes after a semicolon (;) is a comment

C2 equ 2
C3 equ 3
C4 equ 4
C5 equ 5
C6 equ 6
C7 equ 7
C8 equ 8
C9 equ 9
C10 equ 10
CJ equ 11
CQ equ 12
CK equ 13
CA equ 14

TRUE equ 1
FALSE equ 0

section .text

; You should implement functions in the .text section

; the global directive makes a function visible to the test files
global value_of_card
value_of_card:
    ; This function takes as parameter a number representing a card
    ; The function should return the numerical value of the passed-in card 
    cmp dil, CK ; This is K comparison
    je .face_card
    cmp dil, CQ ; This is Q comparison
    je .face_card
    cmp dil, CJ ; This is J comparison
    je .face_card
    cmp dil, CA ; This is A comparison
    je .ace_card        
    mov rax, rdi
    ret

.face_card:
    mov rax, 10
    ret

.ace_card:
    mov rax, 1
    ret

global higher_card
higher_card:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return which card has the higher value
    ; If both have the same value, both should be returned
    ; If one is higher, the second one should be 
    ; Moving original values so not lost 
    mov r10, rdi
    mov r11, rsi

    ; Getting value of card 1
    call value_of_card  ; Result for rdi is now on rax
    mov r8, rax

    ; Getting value of card 2
    mov rdi, r11
    call value_of_card
    mov r9, rax

    ;Compare them 
    cmp r8, r9
    jl .second_is_higher
    jg .first_is_higher
    je .equal

.equal:
    mov rax, r10
    mov rdx, r11
    ret

.first_is_higher:
    mov rax, r10        ; Return original card1 
    xor rdx, rdx
    ret


.second_is_higher:
    mov rax, r11        ; Return original card2 
    xor rdx, rdx 
    ret

global value_of_ace
value_of_ace:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return the value of an upcoming ace
    ; Moving original values so not lost 

    ; Getting value of card 1
    call value_of_card  ; Result for rdi is now on rax
    cmp rax, 0x1    ; check if it returns an ace 
    je .ace_one     ; If its an ace it will probably be a one

    mov r8, rax


    ; Getting value of card 2
    mov rdi, rsi
    call value_of_card
    cmp rax, 0x1    ; check if it returns an ace  
    je .ace_one     ; if its an ace probably ace is one
    mov r9, rax

    ; Adding the values to check if ace value 11 or 1
    add r8,r9
    cmp r8, 10          ; Compare total of first two cards to 10
    jle .ace_eleven     ; If total <= 10, Ace can be 11

.ace_one:
    mov rax, 1
    ret

.ace_eleven:
    mov rax, 11
    ret

global is_blackjack
is_blackjack:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards form a blackjack, and FALSE otherwise
    ; Moving original values so not lost 

    ; Getting value of card 1
    call value_of_card  ; Result for rdi is now on rax
    mov r8, rax
    cmp r8, 0x1         ; If card1 0ace
    je .ace_card1


    ; Getting value of card 2
    mov rdi, rsi
    call value_of_card
    mov r9, rax
    cmp r9, 0x1         ; If card2 0ace
    je .ace_card2

    ; Is blackjack checker
    add r8, r9
    cmp r8, 0x15
    je .win
    mov rax, 0
    ret

.win:
    mov rax, 1
    ret

.ace_card1:
    add r8, 0xA
    
    ; Getting value of card 2
    mov rdi, rsi
    call value_of_card
    mov r9, rax
    
    ; Is blackjack checker
    add r8, r9
    cmp r8, 0x15
    je .win
    mov rax, 0
    ret

.ace_card2:
    add r9, 0xA
    
    ; Is blackjack checker
    add r8, r9
    cmp r8, 0x15
    je .win
    mov rax, 0
    ret



global can_split_pairs
can_split_pairs:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards can be split into two pairs, and FALSE otherwise

    ; Getting value of card 1
    call value_of_card  ; Result for rdi is now on rax
    mov r8, rax

    ; Getting value of card 2
    mov rdi, rsi
    call value_of_card
    mov r9, rax
    ; Check if both values are equal and able to split
    cmp r8, r9
    je .can_split
    mov rax, 0
    ret

.can_split:
    mov rax, 1
    ret

global can_double_down
can_double_down:
    ; This function takes as parameters two numbers each representing a card
    ; The function should return TRUE if the two cards form a hand that can be doubled down, and FALSE otherwise

    call value_of_card  ; Result for rdi is now on rax
    mov r8, rax


    ; Getting value of card 2
    mov rdi, rsi
    call value_of_card
    mov r9, rax

    add r8, r9

    cmp r8, 0x9
    je .double_down

    cmp r8, 0xA
    je .double_down

    cmp r8, 0xB
    je .double_down

    mov rax, 0
    ret
    

.double_down:
    mov rax, 0x1
    ret

%ifidn __OUTPUT_FORMAT__,elf64
section .note.GNU-stack noalloc noexec nowrite progbits
%endif
