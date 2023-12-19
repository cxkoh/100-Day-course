def police(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return "They can drive"
#-> shows that the return of the def expects boolean
#it is a type hint
