import os
import re
import shutil
from pathlib import Path

# === CONFIGURATION ===
# Paths to your Obsidian posts and attachments
posts_dir = Path("D:/ethernetdude/Posts/blogposts")  # Obsidian vault
attachments_dir = posts_dir / "attachments"  # Folder containing images

# Paths for your Hugo site
hugo_content_dir = Path("C:/Users/kapil/Documents/ethernetdude/content")  # Hugo content folder
static_images_dir = Path("C:/Users/kapil/Documents/ethernetdude/static/images")  # Hugo static images folder

# Create directories if they don't exist
hugo_content_dir.mkdir(parents=True, exist_ok=True)
static_images_dir.mkdir(parents=True, exist_ok=True)

# === MAIN PROCESSING ===
for root, dirs, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            original_path = Path(root) / filename

            # Compute the relative path for the destination folder
            relative_path = original_path.relative_to(posts_dir)
            destination_path = hugo_content_dir / relative_path

            # Ensure the subdirectory exists in the destination
            destination_path.parent.mkdir(parents=True, exist_ok=True)

            # Read the content of the .md file
            with original_path.open("r", encoding="utf-8") as f:
                content = f.read()

            # Find all images in the Obsidian format [[image.png]]
            images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg|webp|gif|bmp|svg))\]\]', content, re.IGNORECASE)

            # Process each image
            for image in images:
                # Convert the Obsidian image link format to Hugo format
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)

                image_source = attachments_dir / image
                image_target = static_images_dir / image

                # Check if the image exists in the attachments folder
                if image_source.exists():
                    # Copy the image to the static/images folder if it doesn't already exist there
                    if not image_target.exists():
                        shutil.copy(image_source, image_target)
                        print(f"✅ Copied image: {image}")
                    else:
                        print(f"🟡 Image already exists: {image}")
                else:
                    print(f"❌ Missing image: {image_source}")

            # Write the modified content back to the destination folder
            with destination_path.open("w", encoding="utf-8") as f:
                f.write(content)

print("✅ All Markdown files processed and images copied.")
