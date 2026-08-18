from jinja2 import Template

def generate_nginx_config(filename="nginx.conf"):
    # 1. Define your template structure
    nginx_template = """
    server {
        listen {{ port }};
        server_name {{ domain }};

        location / {
            proxy_pass http://localhost:{{ app_port }};
            proxy_set_header Host $host;
        }
    }
    """
    
    # 2. Define the runtime variables
    context = {
        "port": 80,
        "domain": "myapp.com",
        "app_port": 8080
    }

    # 3. Render and save the file
    template = Template(nginx_template)
    rendered_config = template.render(context)

    with open(filename, "w", encoding="utf-8") as configfile:
        configfile.write(rendered_config.strip())
    print(f"Success: {filename} generated.")

generate_nginx_config()
