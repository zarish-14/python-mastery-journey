print("==================================")
print("AI PROMPT QUALITY ANALYZER")
print("==================================")

#count special characters:
def special_ch():
    specialch_count=0
    for i in user_prompt:
        if (not(i.isdigit() or i.islower() or i.isupper() or i.isspace())):
            specialch_count=specialch_count+1
    return specialch_count
#count digits
def digits():
    digitcount=0
    for i in user_prompt:
        if (i.isdigit()):
            digitcount=digitcount+1
    return digitcount
#count lowercase letters
def lowercase():
    lowercount=0
    for i in user_prompt:
        if (i.islower()):
            lowercount=lowercount+1
    return lowercount
#count uppercase letters
def uppercase():
    capitalize=0
    for i in user_prompt:
        if ( i.isupper()):
            capitalize=capitalize+1
    return capitalize

#count total words 
def total_words():
    totalwords = 0
    in_word = False

    for ch in user_prompt:
        if ch != " " and in_word == False:
            totalwords = totalwords + 1
            in_word = True
        elif ch == " ":
            in_word = False

    return totalwords
#count characters 
def count_characters():
    characters=len(user_prompt)
    return characters
#take prompt from user 
def input_prompt():
    prompt=input("Enter prompt = ")
    return prompt
print("----------------------------------")
user_prompt=input_prompt()
print("User prompt is : ",user_prompt)
print("----------------------------------")
total_characters=count_characters()
print("Total characters in prompt are= ",total_characters)
words_in_prompt=total_words()
print("Total words are= ",words_in_prompt)
uppercase_letters=uppercase()
print("Uppercase letters are = ",uppercase_letters)
lowercase_letters=lowercase()
print("Lowercase letters are = ",lowercase_letters)
total_digits=digits()
print("Total digits are = ", total_digits)
total_special_ch=special_ch()
print("Total special characters are = ",total_special_ch)
print("----------------------------------")
#scoring-system:
def calculate_score(words_in_prompt,uppercase_letters,
                    lowercase_letters,total_digits,
                    total_special_ch,total_characters):
    score=0
    if (words_in_prompt>3):
        score=score+20
    if (uppercase_letters>0):
        score=score+10
    if (lowercase_letters>0):
        score=score+10
    if (total_digits>0):
        score=score+10
    if (total_special_ch>0):
        score=score+10
    if (total_characters>30):
        score=score+20
    if total_characters > 0:
        if ( user_prompt[total_characters-1] == "?"):
            score=score+20
    return score
score=calculate_score(words_in_prompt,uppercase_letters,
                    lowercase_letters,total_digits,
                    total_special_ch,total_characters)
print("Prompt Score: ",score)
#rating according to score
def display_rating(score):

    print("Rating:")

    if score >= 90:
        print("Excellent Prompt")

    elif score >= 70:
        print("Good Prompt")

    elif score >= 50:
        print("Average Prompt")

    else:
        print("Weak Prompt")
display_rating(score)
#suggestions:
print("Sugestions:")
def suggestions(words_in_prompt,uppercase_letters,
                    total_special_ch,total_characters):
    if (words_in_prompt <= 2):
        print("Try adding more details.")
    if (uppercase_letters == 0):
        print("Use proper sentence formatting.")
    if ( total_characters < 5 ):
        print("Explain your requirements clearly.")
    if (total_special_ch==0):
        print("End your prompt with proper punctuation.")
suggestions(words_in_prompt,uppercase_letters,
                    total_special_ch,total_characters)
    
print("----------------------------------")

print("Thank you !")


