posts=[("Admin","hi am very bad guy"),
       ("Admin1","http:hello it is toxic"),
       ("Admin2","badwords bad words http:helloparty he was hated and bad"),
       ("Admin2","badwords bad words http:helloparty he was hated and bad"),
       ("karthik","Hi am karthik http")
       ]
banned_words = ["bad","toxic","hate"]
cleaned_posts=[]
moderatorflags={}
total_posts=len(posts)
cleaned = 0
blocked=0
with open("links_found.txt","w") as post_links:
    for user,post in posts:
        for c in post.split():
            if c.startswith('http'):
                blocked+=1
                post_links.write(user+' : '+c+'\n')
        bann = post
        found_banned = False
        for word in banned_words:
            if word in bann:
                bann = bann.replace(word,"***")
                found_banned = True
        if found_banned:
            cleaned+=1
            if user in moderatorflags:
                moderatorflags[user]+=1
            else:
                moderatorflags[user]=1
        else:
            moderatorflags[user]=0
        cleaned_posts.append(bann)
    print(cleaned_posts)
        
for user, count in moderatorflags.items():
    print(user, ":", count)
print(f"Total Posts Screened: {total_posts} | Cleaned: {cleaned} | Blocked: {blocked}")

