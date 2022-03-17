def character_remove(s,a):
    l=len(s)
    if l==0:
        return s
    small_string=s[1:]
    small_Output=character_remove(small_string,a)
    if s[0]==a:
        return small_Output
    else:
        return s[0]+small_Output



string=input()
character_to_remove=input()
print(character_remove(string,character_to_remove)) 