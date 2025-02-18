import os

def generate_yaml_for_gallery(gallery_path, output_file):
    if not os.path.exists(gallery_path):
        print(f"Error: The directory '{gallery_path}' does not exist.")
        return
    
    images = sorted([f for f in os.listdir(gallery_path) if f.lower().endswith(".jpg")])

    yaml_content = ""
    for image in images:
        yaml_content += f"{image}:\n  description: Placeholder\n"

    with open(output_file, "w") as yaml_file:
        yaml_file.write(yaml_content)

    print(f"YAML file '{output_file}' generated successfully with {len(images)} entries.")

gallery_directory = "../gallery"
output_yaml_file = "../_data/photos.yml"

generate_yaml_for_gallery(gallery_directory, output_yaml_file)