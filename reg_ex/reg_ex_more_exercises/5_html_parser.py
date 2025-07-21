import re

input_string = input()
html_title_pattern = r'(<title>)(.+?)(<\/title>)'
html_content_pattern = r'(<body>)(.+?)(<\/body>)'
title_match = re.search(html_title_pattern, input_string, re.DOTALL)

if title_match:
    title_text = title_match.group(2)

body_match = re.search(html_content_pattern, input_string, re.DOTALL)
if body_match:
    body_text = body_match.group(2)
    clean_body = re.sub(r'\\n|<.*?>', ' ', body_text)
    clean_body = re.sub(r'\s+', ' ',clean_body).strip()

if title_match:
    print(f'Title: {title_text}')
if body_match:
    print(f'Content: {clean_body}')