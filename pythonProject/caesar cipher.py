def caesar(original_text,shift_by,direction_b):
    output_text=""

    for latter in original_text:
        if latter not in alphabet:
            output_text +=latter
        else:
            if direction_b=="decode":
                shift_by *= (-1)
            shift_position=alphabet.index(latter)+shift_by
            shift_position%=len(alphabet)
            output_text += alphabet[shift_position]
    print(f"The {direction} text is :\n {output_text}")
should_continue=True
while should_continue:
    alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction=input("Type 'encode' for encrypt,type 'decode' for decrypt:\n").lower()
    text=input("type your message :\n").lower()
    shift=int(input("type the shift number :\n"))
    caesar(original_text=text,shift_by=shift,direction_b=direction)
    restart=input("type 'yes 'to restart .otherwise 'no':\n").lower()
    if restart=="No":
         should_continue=False
         print("good bye")
