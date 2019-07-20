X=input()
 
if((X>='a' and X<='z') or (X>='A' and X<='Z')):
  if(X=='a' or X=='A' or X=='e' or X=='E' or X=='i' or X=='I' or X=='o' or X=='O' or X=='u' or X=='U'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
