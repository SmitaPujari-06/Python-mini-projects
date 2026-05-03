import imageio.v3 as iio
filenames = [r"C:\Smita\practice projects and more\Gif_python\img2 (1).png",r"C:\Smita\practice projects and more\Gif_python\img1 (2).png"]
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('PokeTeam.gif',images,duration=250,loop=10)