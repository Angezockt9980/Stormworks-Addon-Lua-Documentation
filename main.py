import os
import re

def highlight_lua_code(content):
    # Regular expression to match Lua code blocks
    lua_code_blocks = re.findall(r'```lua\s*(.*?)\s*```', content, re.DOTALL)

    highlighted_content = ""
    last_index = 0
    for lua_code_block in lua_code_blocks:
        start_index = content.find(f'```lua\n{lua_code_block}\n```', last_index)
        if start_index > last_index:
            # Append the normal text before the Lua code block
            highlighted_content += f"<p>{content[last_index:start_index]}</p>\n"
        # Highlight the Lua code block
        highlighted_content += f"<pre><code class='hljs lua'>{lua_code_block}</code></pre>\n"
        last_index = start_index + len(f'```lua\n{lua_code_block}\n```')

    # Append any remaining normal text after the last Lua code block
    if last_index < len(content):
        highlighted_content += f"<p>{content[last_index:]}</p>\n"

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
        f.write(".selected { background-color: #1e2127; padding: 5px; border-radius: 5px; }\n")  # Background color for selected buttons
        f.write("a:hover { color: #fff; }\n")  # Change color on hover
        f.write("h2 { font-size: 24px; margin-bottom: 5px; }\n")
        f.write("pre { background-color: #1e2127; padding: 5px; border-radius: 5px; margin-top: -15px}\n")
        f.write("code { white-space: pre-wrap; }\n")  # Enforce text wrapping
        f.write("</style>\n")
        f.write("</head>\n<body>\n")

        # Write navigation menu and About section container
        f.write("<div id='nav-container'>\n")
        f.write("<div id='nav'>\n")
        f.write("<h2 style='color: #abb2bf; margin-bottom: 20px;'>Navigation</h2>\n")
        for file_name in os.listdir(input_folder):
            if file_name.endswith(".md"):
                file_path = os.path.join(input_folder, file_name)
                with open(file_path, 'r') as markdown_file:
                    file_content = markdown_file.read()
                name = file_name.replace(".md", "").capitalize()
                f.write(f"<a href='#{file_name.replace(' ', '%20')}' style='color: #abb2bf;'>{name}</a>\n")

        # Write About section inside the nav container
        f.write("<div id='about'>\n")
        f.write("<h2 style='color: #abb2bf; margin-bottom: 10px;'>Credits</h2>\n")
        f.write("Developed by angezockt9980 with the help of fabi123.<br/>\n")  # Replace "Your Name" with your actual name
        f.write("For support and updates, join our Discord Server! <a href='https://discord.gg/s4YSHf5qGt' target='_blank'>https://discord.gg/s4YSHf5qGt</a></p>\n")  # Replace "https://discord.gg/example" with your actual Discord invite link
        f.write("</div>\n")

        f.write("</div>\n")  # Close nav
        f.write("</div>\n")  # Close nav-container

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

        # Write JavaScript for smooth scrolling and button highlighting
        f.write("<script>\n")
        f.write("document.addEventListener('DOMContentLoaded', function() {\n")
        f.write("    const sections = document.querySelectorAll('h2');\n")
        f.write("    const navLinks = document.querySelectorAll('#nav a');\n")
        f.write("    window.addEventListener('scroll', () => {\n")
        f.write("        let current = '';\n")
        f.write("        sections.forEach(section => {\n")
        f.write("            const sectionTop = section.offsetTop;\n")
        f.write("            if (pageYOffset >= sectionTop - 200) {\n")  # Adjusted for accurate scrolling
        f.write("                current = section.getAttribute('id');\n")
        f.write("            }\n")
        f.write("        });\n")
        f.write("        navLinks.forEach(link => {\n")
        f.write("            link.classList.remove('selected');\n")
        f.write("            if (link.getAttribute('href').substring(1) === current) {\n")
        f.write("                link.classList.add('selected');\n")
        f.write("            }\n")
        f.write("        });\n")
        f.write("    });\n")

        # Smooth scrolling
        f.write("    navLinks.forEach(link => {\n")
        f.write("        link.addEventListener('click', (e) => {\n")
        f.write("            e.preventDefault();\n")
        f.write("            const targetId = link.getAttribute('href').substring(1);\n")
        f.write("            const targetElement = document.getElementById(targetId);\n")
        f.write("            if (targetElement) {\n")
        f.write("                const offset = targetElement.getBoundingClientRect().top + window.pageYOffset;\n")
        f.write("                window.scrollTo({\n")
        f.write("                    top: offset, // Adjust as needed\n")
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
    input_folder = "E:\Stormworks Documentation\manual3"  # Change this to the path of your input folder containing .md files
    output_folder = "E:\Stormworks Documentation\Stormworks Addon Lua Documentation\Website"  # Change this to the desired output folder

    generate_index_html(input_folder, output_folder)
    print("index.html generated successfully.")
