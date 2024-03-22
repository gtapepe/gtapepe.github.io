from PIL import Image
im = Image.open('2.png').convert('RGB')

# Split into 3 channels
r, g, b = im.split()


# Recombine back to RGB image
result = Image.merge('RGB', (r, b, g))

result.save('result2.png')