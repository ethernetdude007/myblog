import os
import re
import shutil

# Paths
source_posts_dir = r"D:\ethernetdude\Posts\blogposts"
destination_posts_dir = r"C:\Users\kapil\Documents\ethernetdude\content"
attachments_dir = os.path.join(source_posts_dir, "attachments")
static_images_dir = r"C:\Users\kapil\Documents\ethernetdude\static\images"

# Make sure output directories exist
os.makedirs(static_images_dir, exist_ok=True)
os.makedirs(destination_posts_dir, exist_ok=True)

# Copy all markdown files and rewrite links
for root, dirs, files in os.walk(source_posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            rel_path = os.path.relpath(root, source_posts_dir)
            target_dir = os.path.join(destination_posts_dir, rel_path)
            os.makedirs(target_dir, exist_ok=True)

            source_filepath = os.path.join(root, filename)
            target_filepath = os.path.join(target_dir, filename)

            with open(source_filepath, "r", encoding="utf-8") as file:
                content = file.read()

            # Replace Obsidian-style image links with Markdown for Hugo
            images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg|webp))\]\]', content, re.IGNORECASE)

            for image in images:
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)

                image_source = os.path.join(attachments_dir, image)
                image_target = os.path.join(static_images_dir, image)

                if os.path.exists(image_source):
                    if not os.path.exists(image_target):
                        shutil.copy(image_source, image_target)
                        print(f"Copied: {image}")
                    else:
                        print(f"Already exists: {image}")
                else:
                    print(f"⚠️ Missing: {image_source}")

            # Save modified file to Hugo content folder
            with open(target_filepath, "w", encoding="utf-8") as file:
                file.write(content)

print("✅ Markdown files copied and processed for Hugo.")
