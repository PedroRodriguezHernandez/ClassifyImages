from classify import move_resize_images


# Define the original folders
main_folder = 'C:/Users/Propietario/Desktop/Dataset'
bus_folder = main_folder + '/Bus'
car_folder = main_folder + '/Car'
motorcycle_folder = main_folder + '/Motorcycle'
truck_folder = main_folder + '/Truck'

# Create destination folders
train_folder = 'C:/Users/Propietario/Desktop/TypesVehicles/train'
validation_folder = 'C:/Users/Propietario/Desktop/TypesVehicles/validation'
test_folder = 'C:/Users/Propietario/Desktop/TypesVehicles/test'

# Percentages
train_percentage = 0.7
validation_percentage = 0.2
test_percentage = 0.1
new_size = (150, 150)

print("Start train image............................\n ")

move_resize_images(bus_folder, train_folder + '/bus' , train_percentage, new_size)
move_resize_images(car_folder, train_folder + '/car' , train_percentage, new_size)
move_resize_images(motorcycle_folder, train_folder + '/motorcycle', train_percentage, new_size)
move_resize_images(truck_folder, train_folder + '/truck', train_percentage, new_size)

print("Start validation image............................\n ")
move_resize_images(bus_folder, validation_folder + '/bus' , validation_percentage, new_size)
move_resize_images(car_folder, validation_folder + '/car' , validation_percentage, new_size)
move_resize_images(motorcycle_folder, validation_folder + '/motorcycle', validation_percentage, new_size)
move_resize_images(truck_folder, validation_folder + '/truck', validation_percentage, new_size)
print("Start test image............................\n ")

move_resize_images(bus_folder, test_folder + '/bus' , test_percentage, new_size)
move_resize_images(car_folder, test_folder + '/car' , test_percentage, new_size)
move_resize_images(motorcycle_folder, test_folder + '/motorcycle', test_percentage, new_size)
move_resize_images(truck_folder, test_folder + '/truck', test_percentage, new_size)
