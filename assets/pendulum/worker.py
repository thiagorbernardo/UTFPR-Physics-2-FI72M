import glob
from PIL import Image

# filepaths
fp_in = "assets/pendulum/pendulum_*.png"
fp_out = "assets/pendulum/pendulum.gif"

# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)
