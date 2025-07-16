title_of_an_article = input()
content_of_an_article = input()
saved_comments = []

while True:
    comments = input()
    if comments == 'end of comments':
        break
    saved_comments.append(comments)


print(f"<h1>\n    {title_of_an_article}\n</h1>")
print(f"<article>\n    {content_of_an_article}\n</article>")
for comment in saved_comments:
    print(f"<div>\n    {comment}\n</div>")
