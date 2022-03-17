def character_replace(s,a,x):
    l=len(s)
    if l==0:
        return s
    small_string=s[1:]
    small_Output=character_replace(small_string,a,x)
    if s[0]==a:
        return x+small_Output
    else:
        return s[0]+small_Output



string=input()
character_to_replace=input()
character_to_add=input()
print(character_replace(string,character_to_replace,character_to_add))