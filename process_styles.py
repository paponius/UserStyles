# process_styles.py
import os
import re
import yaml
import requests
import logging

def process_styles():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    
    os.makedirs("main_output", exist_ok=True)
    os.makedirs("clones_output", exist_ok=True)
    
    if not os.path.exists("manifest.yml"):
        logging.error("manifest.yml not found.")
        return

    try:
        with open("manifest.yml", "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        logging.error(f"Failed to parse manifest.yml: {e}")
        return

    styles = data.get("userstyles", [])
    if not styles:
        logging.warning("No userstyles found in manifest.yml.")
        return

    for style in styles:
        raw_name = style.get("name")
        url = style.get("url")
        clones_count = style.get("clones", 0)

        if not raw_name or not url:
            logging.error(f"Skipping entry due to missing 'name' or 'url': {style}")
            continue

        safe_name = raw_name.lower().replace(" ", "-")
        logging.info(f"Processing style: {raw_name} ({url})")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            content = response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to download style '{raw_name}' from {url}: {e}")
            continue

        # 1. Save base file into its own directory for the main branch
        style_dir = os.path.join("main_output", safe_name)
        os.makedirs(style_dir, exist_ok=True)
        base_filename = os.path.join(style_dir, f"{safe_name}.user.css")
        
        try:
            with open(base_filename, "w", encoding="utf-8") as bf:
                bf.write(content)
            logging.info(f"Saved base file: {base_filename}")
        except IOError as e:
            logging.error(f"Failed to write file {base_filename}: {e}")
            continue

        # 2. Generate clones for the site-clones branch if specified
        if clones_count > 0:
            clone_dir = os.path.join("clones_output", safe_name)
            os.makedirs(clone_dir, exist_ok=True)

            for i in range(1, clones_count + 1):
                clone_filename = os.path.join(clone_dir, f"{safe_name}-clone-{i}.user.css")
                clone_suffix = f" clone {i}"
                
                modified_content = re.sub(
                    r'(^@name[[:blank:]]+)(.*)',
                    r'\1\2' + clone_suffix,
                    content,
                    flags=re.MULTILINE
                )
                
                try:
                    with open(clone_filename, "w", encoding="utf-8") as cf:
                        cf.write(modified_content)
                    logging.info(f"Generated clone: {clone_filename}")
                except IOError as e:
                    logging.error(f"Failed to write clone file {clone_filename}: {e}")

if __name__ == "__main__":
    process_styles()
