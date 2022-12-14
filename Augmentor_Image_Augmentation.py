import Augmentor


path_to_data = "Dataset Path" #Enter the path to dataset

#uncommetn or add any augmentation you want
p = Augmentor.Pipeline(path_to_data)
#p.Affine(scale=(0.5, 1.5))
#p.rotate90(probability=0.5)
#p.rotate270(probability=0.5)
#p.flip_left_right(probability=0.8)
#p.flip_top_bottom(probability=0.3)
#p.crop_random(probability=1, percentage_area=0.5)
p.resize(probability=1.0, width=512, height=512)

#p.random_distortion(probability=1, grid_width=4, grid_height=4, magnitude=8)
#p.flip_left_right(probability=0.5)
#p.flip_top_bottom(probability=0.5)

p.sample(1033) #Number of images you get as output
