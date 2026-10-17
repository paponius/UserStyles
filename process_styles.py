# process_styles.py
import os
import re
import yaml
import requests
import logging

def setup_logging():
    os.makedirs("site-clones", exist_ok=True)
    log_file = "site-clones/update.log"
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

def process_styles():
    setup_logging()
    logging.info("Starting style update process.")
    
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

        safe_name = raw_name.replace(" ", "-")
        logging.info(f"Processing style: {raw_name} ({url})")

        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            content = response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to download style '{raw_name}' from {url}: {e}")
            continue

        base_filename = f"site-clones/{safe_name}.user.css"
        try:
            with open(base_filename, "w", encoding="utf-8") as bf:
                bf.write(content)
            logging.info(f"Successfully saved: {base_filename}")
        except IOError as e:
            logging.error(f"Failed to write file {base_filename}: {e}")
            continue

        for i in range(1, clones_count + 1):
            clone_filename = f"site-clones/{safe_name}-site-clone-{i}.user.css"
            clone_suffix = f" site-clone-{i}"
            
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

    logging.info("Style update process completed.")

if __name__ == "__main__":
    process_styles()
