#!/usr/bin/env python3
import os
import re
import sys

def markdown_to_html(md_file):
    """简单的markdown转HTML函数"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取front matter
    front_matter = {}
    body = content
    
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter_text = parts[1]
            body = parts[2].strip()
            
            # 简单解析front matter
            for line in front_matter_text.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    front_matter[key.strip()] = value.strip()
    
    # 简单的markdown转换
    html_body = body
    
    # 转换标题
    html_body = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_body, flags=re.MULTILINE)
    
    # 转换粗体
    html_body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_body)
    
    # 转换列表
    html_body = re.sub(r'^- (.*?)$', r'<li>\1</li>', html_body, flags=re.MULTILINE)
    html_body = re.sub(r'(<li>.*</li>\n)+', r'<ul>\g<0></ul>', html_body)
    
    # 转换换行
    html_body = html_body.replace('\n\n', '</p><p>')
    html_body = '<p>' + html_body + '</p>'
    html_body = html_body.replace('<p><h', '<h').replace('</h></p>', '</h>')
    html_body = html_body.replace('<p><ul>', '<ul>').replace('</ul></p>', '</ul>')
    
    # 创建HTML
    html = f'''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{front_matter.get('subject', '王虎的信')}</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        .meta {{ background: #f5f5f5; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
        .from {{ font-weight: bold; font-size: 1.2em; }}
        .emoji {{ font-size: 1.5em; }}
        .date {{ color: #666; }}
        .content h2 {{ color: #333; border-bottom: 2px solid #eee; padding-bottom: 5px; }}
        .content h3 {{ color: #555; }}
        .content p {{ margin-bottom: 15px; }}
        .content ul {{ margin-bottom: 15px; padding-left: 20px; }}
        .content li {{ margin-bottom: 5px; }}
    </style>
</head>
<body>
    <div class="meta">
        <div class="from">
            <span class="emoji">{front_matter.get('from_emoji', '🐯')}</span>
            {front_matter.get('from', '王虎')} →
            <span class="emoji">{front_matter.get('to_emoji', '🦀')}</span>
            {front_matter.get('to', '王小蟹')}
        </div>
        <div class="date">
            {front_matter.get('date', '2026-03-14')} {front_matter.get('time', '11:07')}
        </div>
        <div class="subject">
            <strong>{front_matter.get('subject', '回信')}</strong>
        </div>
    </div>
    <div class="content">
        {html_body}
    </div>
</body>
</html>'''
    
    return html

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("用法: python3 create_html.py <markdown文件>")
        sys.exit(1)
    
    md_file = sys.argv[1]
    if not os.path.exists(md_file):
        print(f"文件不存在: {md_file}")
        sys.exit(1)
    
    html = markdown_to_html(md_file)
    html_file = md_file.replace('.md', '.html')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"HTML文件已生成: {html_file}")