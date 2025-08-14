posts = [
        {
            "id": 1,
            "caption": "Welcome"
            },
        {
            "id": 2,
            "caption": "Welcome to AXIA hub"
            }
        ]
company_post = None
post_id = int(input("Enter post ID : "))
for post in posts:
    if post_id == post["id"]:
        company_post = post
        print(company_post)
        break
else:
    print(f"Post with {post_id} not found!")
