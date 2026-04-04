import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Capture the incorrectly injected FAQs
# They start just after `<html c` and end just before `lass="light" lang="ru">`
match = re.search(r'(<!DOCTYPE html>\n<html c)(.*?)(lass="light" lang="ru">)', html, flags=re.DOTALL)
if match:
    injected_faqs = match.group(2)
    # clean it out
    html = html.replace(match.group(0), '<!DOCTYPE html>\n<html class="light" lang="ru">')
    
    # 2. Find the REAL FAQ block
    faq_idx = html.find('<div class="space-y-4">')
    if faq_idx != -1:
        # insert right after `<div class="space-y-4">`
        # we need to find the exact insertion point
        insert_point = faq_idx + len('<div class="space-y-4">')
        html = html[:insert_point] + injected_faqs + html[insert_point:]
        
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Fix applied successfully.")
    else:
        print("Couldn't find target FAQ space-y-4")
else:
    print("Couldn't find the injected bug at top")
