import os
import re
import shutil

# Paths
posts_dir = r"D:\ethernetdude\Posts\blogposts"
attachments_dir = r"D:\ethernetdude\Posts\blogposts\attachments"
static_images_dir = r"C:\Users\kapil\Documents\ethernetdude\static\images"

# Make sure static image dir exists
os.makedirs(static_images_dir, exist_ok=True)

# Go through every .md file in subdirectories
for root, dirs, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)  # ✅ define filepath inside the loop

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

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

            with open(filepath, "w", encoding="utf-8") as file:
                file.write(content)

print("✅ All markdown files processed.")
