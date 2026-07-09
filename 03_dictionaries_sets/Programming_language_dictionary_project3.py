print("====================================================")
print("      PROGRAMMING LANGUAGE DICTIONARY")
print("====================================================")
languages={
    "C++" : "Competitive Programming", #dictionary key:value pair
    "Python" : "AI & Automation",
    "Java" : "Andriod Development",
    "SQL" : " Database Management",
    "Rust" : "System Programming",
    "Javascript " : "Web development",
}
favourite_language={"Python", "C++", "SQL"} #set
#display all langauges
print("\nProgramming Languages:\n")

for language,purpose in languages.items():
    print(language, "->", purpose)
#Enter  langauge to search
required_language=input("Enter language to search = ")
if required_language in languages:
    print("Required language: ",required_language)
    print("Primary Use: ",languages[required_language])
else:
    print("Required language not found")
#Add a new language
new_language=input("Enter new language= ")
purpose=input("Enter purpose= ")
if new_language in languages:
    print("Language already exits")
else:
    languages.update({new_language:purpose})
    print("New language:\n",new_language,"\n Purpose: \n",purpose)
    print("Language has added : \n Language: ",new_language,
      "\n Purpose: ",purpose)
    print(languages)
#Update language or purpose
updated_language=input("Enter updated language: \n Python \n C++ \n Java \n SQL \n Go \n Rust \n enter here: ")
updated_purpose=input("Enter updated purpose : ")
if updated_language in languages:
    languages.update({updated_language:updated_purpose})
    print("Language has updated : \n Language: ",updated_language,
      "\n Purpose: ",updated_purpose)
    print(languages)
else:
    print("Language  not found")
#Remove a language
remove_language=input("Enter language to remove= ")
if remove_language in languages:
    languages.pop(remove_language)
    print("Language has successfully removed : \n Language:",remove_language)
else:
    print("Language not found")
#Display Favourite Languages
print("Favourite Languages:")
print(favourite_language)
#Add Favourite language
new_favourite_language=input("Enter new Favourite Language:")
favourite_language.add(new_favourite_language)
print("New Favourite Language has added :",new_favourite_language)
#Remove favourite language
remove_favourite_language=input("Enter language to remove: ")
if remove_favourite_language in favourite_language:
    favourite_language.remove(remove_favourite_language)
    print("Language has removed from favourite Language: ", remove_favourite_language)
else:
    print("Language not found in Favourite language")
#Display updated language:
for language in favourite_language:
    print(language)
total_languages=len(languages)
total_favourite_languages=len(favourite_language)
print("Total Languages: ",total_languages)
print("Total Favourite Languages: ",total_favourite_languages)
print("Thank you!")

