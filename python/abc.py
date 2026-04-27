posts = [     
            {"user" : "user1", "text" : "This was bad experiance http:www.user1post"},
            {"user" : "user2", "text" :"Wonderful Place"}, 
            {"user" : "user3", "text" :"They said its toxic"},
            {"user" : "user4", "text" :"People love each other"},
            {"user" : "user5", "text" :"The movie was bad http:www.user5post"}, 
            {"user" : "user6", "text" :"I hate this weather"}
                ]

banned_words = ["bad", "toxic", "hate"]

total_posts = len(posts)
cleaned_posts = 0
blocked_posts = 0

links = []
user_report = {}

for post in posts:
    user = post["user"]
    text = post["text"]
    
    if user not in user_report:
        user_report[user]=0
    
    lower_text = text.lower()
    found_bad_word = False
    
    for word in banned_words :
        if word in lower_text:
            found_bad_word = True
            text = text.replace(word,"***")
            user_report[user]+= 1
    
    words = text.split()
    for w in words:
        if w.startswith("http"):
            links.append(w)
        
    if found_bad_word:
        cleaned_posts+= 1
    
    post["text"]=text 


with open("links_found1.txt","w") as f:
    for link in links:
        f.write(link + "\n")

print("final Cleaned Posts:")
for post in posts:
    print(post)

print("\nUser Report:")
print(user_report)

print(f"\nTotal Posts Screened: {total_posts} | Cleaned: {cleaned_posts} | Blocked: {blocked_posts}")