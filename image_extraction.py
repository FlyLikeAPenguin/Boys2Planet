from PIL import Image
import os

def extract_faces_from_grid(image_path, output_dir, cols, rows, padding=0, prefix="face", offset=0):
    """
    Extract faces from a grid-like image and save them as individual image files,
    trimming optional padding between cells.

    Args:
        image_path (str): Path to the composite grid image.
        output_dir (str): Directory to save the cropped face images.
        cols (int): Number of columns in the grid.
        rows (int): Number of rows in the grid.
        padding (int): Pixel spacing between images in both directions.
        prefix (str): Filename prefix for the cropped images.
    """
    # os.makedirs(output_dir, exist_ok=True)
    img = Image.open(image_path)
    img_width, img_height = img.size

    cell_width = 230
    cell_height = 230
    x_padding= 26
    y_padding = 25
    left_padding = 42


    count = 1
    for row in range(rows):
        for col in range(cols):
            left = col * (cell_width + x_padding) + left_padding
            upper = row * (cell_height + y_padding)
            right = left + cell_width
            lower = upper + cell_height
            face = img.crop((left, upper, right, lower))
            face.save(os.path.join(output_dir, f"{prefix}_{count+offset}.png"))
            count += 1

# Example usage
if __name__ == "__main__":
    # Replace with your image paths and grid specs
    images_to_process = [
        ("images7.jpg", 4, 6, 27),  # 30 faces with padding
    ]

    for i, (path, cols, rows, padding) in enumerate(images_to_process, start=1):
        extract_faces_from_grid(path, f"output_faces", cols, rows, padding, "face", 136)
