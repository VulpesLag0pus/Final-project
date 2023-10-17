import imageio.v2 as imageio


file = ['0.png', '1.png', '2.png']
images = []

for filename in file:
    images.append(imageio.imread(filename))


imageio.mimsave('Sleeping_Vulpes.gif', images, duration = 5)