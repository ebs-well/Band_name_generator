# First day challenge, I have been through some courses in college for python already before this course.
# For completion I wanted to start from the beginning and see what early lessons this course taught that I didn't know.
def band_name_gen ():
  city_name = input("What city did you grow up in? ")
  print("Cool I have always wanted to visit " + city_name)
  pet_name = input("What was the name of your pet? ")
  print("I think your band name should be " + city_name + " " + pet_name + "!")
  band_name = city_name + " " + pet_name
  print("I can already hear them chanting " + band_name + "!!!")

band_name_gen()