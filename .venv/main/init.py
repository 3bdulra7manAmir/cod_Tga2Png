import os
from PIL import Image

def convert_png_to_tga(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Get a list of all files in the input directory
    file_list = os.listdir(input_dir)

    # Process each file in the input directory
    for file_name in file_list:
        # Check if the file is a PNG image
        if file_name.endswith('.png'):
            # Construct the full path for the input and output files
            input_path = os.path.join(input_dir, file_name)
            output_path = os.path.join(output_dir, file_name.replace('.png', '.tga'))

            # Open the PNG image
            image = Image.open(input_path)

            # Save a copy of the image in TGA format
            image.save(output_path, format='TGA')

            # Close the image
            image.close()

    print("Conversion complete!")

# Example usage
input_directory = "E:\\Games\\Games_Laboratory\\Models\\mw_calisto_arms\\mw_calisto_arms\\textures"
output_directory = "E:\\Games\\Games_Laboratory\\Models\\mw_calisto_arms\\mw_calisto_arms"

convert_png_to_tga(input_directory, output_directory)