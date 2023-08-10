import os
from PIL import Image

# Replace this path with the directory containing your CR2 files
input_directory = '/Users/quielo/Images/cr2png/raw'
# Replace this path with the directory where you want to save the PNG files
output_directory = '/Users/quielo/Images/cr2png/converted'

# Ensure output directory exists
os.makedirs(output_directory, exist_ok=True)

# Check if the input directory is empty
if not os.listdir(input_directory):
    print("Input directory is empty.")
else:
    # Loop through all files in the input directory
    for filename in input_path:
        if filename.lower().endswith('.cr2'):
            input_cr2_file = os.path.join(input_directory, filename)
            output_png_file = os.path.join(output_directory, os.path.splitext(filename)[0] + '.png')

            try:
                # Open the CR2 file using PIL
                image = Image.open(input_cr2_file)

                # Convert and save the image as PNG
                image.save(output_png_file, 'PNG')

                print(f'{input_cr2_file} converted to {output_png_file}')
            except Exception as e:
                print(f'Error converting {input_cr2_file}: {e}')
