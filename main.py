import os

def highlight_lua_code(content):
    highlighted_content = ""
    code_block = False
    for line in content.split('\n'):
        if line.strip() == "```":
            if code_block:
                highlighted_content += "</code></pre>\n"
                code_block = False
            else:
                highlighted_content += "<pre><code class='hljs lua'>"
                code_block = True
        elif code_block:
            highlighted_content += line + "\n"
        else:
            highlighted_content += line + "<br>\n"  # Preserve line breaks outside code blocks
    return highlighted_content

def generate_index_html(input_folder, output_folder):
    output_file = os.path.join(output_folder, "index.html")
    with open(output_file, 'w') as f:
        # Write HTML header
        f.write("<!DOCTYPE html>\n<html>\n<head>\n<title>Stormworks Addon Markdown Documentation</title>\n")
        f.write("<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/atom-one-dark.min.css'>\n")
        f.write("<script src='https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/highlight.min.js'></script>\n")
        f.write("<script>hljs.highlightAll();</script>\n")
        f.write("<style>\n")
        f.write("body { font-family: Arial, sans-serif; margin: 0; background-color: #282c34; color: #abb2bf; }\n")
        f.write("#nav { position: fixed; top: 0; bottom: 0; left: 0; width: 200px; background-color: #2c313a; padding: 20px; overflow-y: auto; }\n")
        f.write("#content { margin-left: 240px; padding: 20px; }\n")
        f.write("#about { position: absolute; bottom: 10px; left: 10px; color: #abb2bf; }\n")
        f.write("a { display: block; margin-bottom: 10px; text-decoration: none; color: #abb2bf; }\n")
        f.write("a:hover { color: #fff; }\n")
        f.write("h2 { font-size: 24px; margin-bottom: 5px; }\n")
        f.write("pre { background-color: #1e2127; padding: 5px; border-radius: 5px; }\n")
        f.write("code { white-space: pre-wrap; }\n")  # Enforce text wrapping
        f.write("</style>\n")
        f.write("</head>\n<body>\n")

        # Write navigation menu
        f.write("<div id='nav'>\n")
        f.write("<h2 style='color: #abb2bf; margin-bottom: 20px;'>Navigation</h2>\n<ul>\n")
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".md"):
                file_path = os.path.join(input_folder, file_name)
                name = file_name.replace(".md", "").capitalize()
                f.write(f"<li><a href='#{file_name.replace(' ', '%20')}'>{name}</a></li>\n")
        f.write("</ul>\n")
        f.write("<div id='about'>\n")
        f.write("<h2 style='color: #abb2bf; margin-bottom: 10px;'>About</h2>\n")
        f.write("<p style='font-size: 14px;'>Stormworks Addon Markdown Documentation. Created by angezockt9980 with the help of fabi123. <a href='https://discord.gg/s4YSHf5qGt' style='color: #abb2bf; text-decoration: underline;'>https://discord.gg/s4YSHf5qGt</a></p>\n")
        f.write("</div>\n")
        f.write("</div>\n")

        # Write content for each markdown file in the input folder
        f.write("<div id='content'>\n")
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".md"):
                file_path = os.path.join(input_folder, file_name)
                with open(file_path, 'r') as markdown_file:
                    file_content = markdown_file.read()
                name = file_name.replace(".md", "").capitalize()
                f.write(f"<h2 id='{file_name.replace(' ', '%20')}' style='color: #abb2bf; margin-bottom: 5px;'>{name}</h2>\n")
                highlighted_content = highlight_lua_code(file_content)
                f.write(highlighted_content)
                f.write("<hr>\n")
        f.write("</div>\n")

        # Write JavaScript for smooth scrolling
        f.write("<script>\n")
        f.write("document.addEventListener('DOMContentLoaded', function() {\n")
        f.write("    document.querySelectorAll('a').forEach(anchor => {\n")
        f.write("        anchor.addEventListener('click', function(e) {\n")
        f.write("            e.preventDefault();\n")
        f.write("            const targetId = this.getAttribute('href').substring(1);\n")
        f.write("            const targetElement = document.getElementById(targetId);\n")
        f.write("            if (targetElement) {\n")
        f.write("                targetElement.scrollIntoView({\n")
        f.write("                    behavior: 'smooth'\n")
        f.write("                });\n")
        f.write("            }\n")
        f.write("        });\n")
        f.write("    });\n")
        f.write("});\n")
        f.write("</script>\n")

        # Write HTML footer
        f.write("</body>\n</html>")

if __name__ == "__main__":
    input_folder = "E:/Stormworks Documentation/manual2"  # Change this to the path of your input folder containing .md files
    output_folder = "E:/Stormworks Documentation/Code/Stormworks Addon Lua Documentation"  # Change this to the desired output folder

    generate_index_html(input_folder, output_folder)
    print("index2.html generated successfully.")
