#!/bin/bash
# 更新所有信件页面，添加返回问题页的功能

for file in wangdadao/2025-03-13.html wangdaxia/2025-03-13.html wangdaxia/2025-03-13-3.html wangxiaoxie/2026-03-13.html wangxiaoxie/2026-03-13-2.html wangxiaoxie/2026-03-13-3.html; do
    if [ -f "$file" ]; then
        # 检查是否已经更新过
        if grep -q "backUrl" "$file"; then
            echo "已更新: $file"
        else
            # 替换返回链接，添加JS代码
            sed -i 's/<a href="\.\.\/index\.html" class="back-link">← 返回信件列表<\/a>/<a href="\.\.\/index\.html" class="back-link" id="backLink">← 返回信件列表<\/a>\n        \n        <script>\n            \/\/ 检查是否有返回参数\n            const urlParams = new URLSearchParams(window.location.search);\n            const backUrl = urlParams.get('\''back'\'');\n            if (backUrl) {\n                document.getElementById('\''backLink'\'').href = '\''..\/'\'' + backUrl;\n                document.getElementById('\''backLink'\'').textContent = '\''← 返回问题'\'';\n            }\n        <\/script>/' "$file"
            echo "更新: $file"
        fi
    fi
done

echo "完成！"
