from classify import move_resize_images


# Define the original folders
car_folder = 'C:/Users/Propietario/Desktop/Dataset/Car'
truck_folder = 'C:/Users/Propietario/Desktop/Dataset/Truck'
motorbike_folder = 'C:/Users/Propietario/Desktop/Dataset/motorcycle'
bus_folder = 'C:/Users/Propietario/Desktop/Dataset/Bus'

# Create destination folders
train_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/train'
validation_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/validation'
test_folder = 'C:/Users/Propietario/Desktop/DatasetTypeVehicle/test'

# Percentages
train_percentage = 0.7
validation_percentage = 0.2
test_percentage = 0.1
new_size = (200,200)

print("Start train image............................\n ")
move_resize_images(car_folder, train_folder + '/car', train_percentage, new_size)
move_resize_images(truck_folder, train_folder + '/truck', train_percentage, new_size)
move_resize_images(motorbike_folder, train_folder + '/motorbike', train_percentage, new_size)
move_resize_images(bus_folder, train_folder + '/bus', train_percentage, new_size)

print("Start validation image............................\n ")
move_resize_images(car_folder, validation_folder + '/car', validation_percentage, new_size)
move_resize_images(truck_folder, validation_folder + '/truck', validation_percentage, new_size)
move_resize_images(motorbike_folder, validation_folder + '/motorbike', validation_percentage, new_size)
move_resize_images(bus_folder, validation_folder + '/bus', validation_percentage, new_size)

print("Start test image............................\n ")
move_resize_images(car_folder, test_folder + '/car', test_percentage, new_size)
move_resize_images(truck_folder, test_folder + '/truck', test_percentage, new_size)
move_resize_images(motorbike_folder, test_folder + '/motorbike', test_percentage, new_size)
move_resize_images(bus_folder, test_folder + '/bus', test_percentage, new_size)
