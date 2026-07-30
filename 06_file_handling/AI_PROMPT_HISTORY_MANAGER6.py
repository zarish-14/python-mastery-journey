print("=====================================")
print("AI PROMPT HISTORY MANAGER")
print("=====================================")
import os
#display menu 
def display_menu():
    print("1. Add New Prompt\n2. View All Prompts\n3. Search Prompt \n" \
    "4. Count Total Prompts \n5. Delete Prompt History \n6. Exit")
#ask for prompt
def add_new_prompt():
    prompt=input("Enter AI prompt:")
    f=open("prompts.txt","a+")
    f.write(prompt)
    f.write("\n")
    print("Prompt has saved successfully")
    f.close()
#view all the prompts:
def view_all_prompts():
    f=open("prompts.txt", "r+")
    data=f.readlines()
    if len(data) == 0:
        print("No prompts found.")
    else:
        idx =1
        for i in data:
            print("Prompt ",idx ," : \n ",i)
            idx=idx+1
    f.close()
#search any word :
def  search_prompt():
    keyword=input("Enter keyword:")
    f=open("prompts.txt","r+")
    data=f.read()
    line=data.find(keyword)
    if line == -1:
        print("not found")
    else:
        print("Found:",data[line:len(data)])
    f.close()
#count total prompt
def count_total_prompts():
    count=0
    f=open("prompts.txt","r+")
    data=f.readlines()
    count=len(data)
    print("Total prompts= ",count)
    f.close()
#delete prompt
def  delete_prompt_history():
    confirm = input("Are you sure (Y/N): ")
    if confirm.upper() == "Y":
        f=open("prompts.txt" , "w")
        f.close()
        print("History Deleted")
    


#loop to display menu again and ask choice 
val=True
while val:
    display_menu()
    choice=int(input("Enter your choice= "))
    if choice == 1:
        add_new_prompt()
    elif choice == 2:
        view_all_prompts()
    elif choice == 3:
        search_prompt()
    elif choice == 4:
        count_total_prompts()
    elif choice == 5:
        delete_prompt_history()
    elif choice == 6:
        print("Thank you !")
        val=False
    else:
        print("Invalid choice , try again")

   
    
    

