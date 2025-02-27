'''
import turtle

fill_color = input("Enter the circle fill color here: ")
circle_size = turtle.numinput("Your Drawing", "Enter the circle size you desire here:")
pen_color = input("Enter the desire pen color here: ")
turtle.pensize(10)
turtle.pencolor(pen_color)
turtle.fillcolor(fill_color)
turtle.begin_fill()
turtle.circle(circle_size)
turtle.end_fill()
turtle.pos()



# This program is to count the number of times A appears in my About Me Profile in linkedin

#create a def main structure

def main():

    About_me = input("Enter your LinkedIn About Me details here: ") #This will accept input from the user

    count = 0

    for counting in About_me:
        if counting == "A" or counting == "a":
            count += 1
    
    print(f"The number of 'A' in your profile is: {count}.")

if __name__ == "__main__":
    main()

print(main())


sentence = input("Enter a sentence here: ")

for letter in sentence:
    print(letter)


name = "Adeoluwa"

character = name[3]
print(name[-2] + name[-5] + name[-4] + name[-3])


   
def main():
    city = input("Enter your favorite city here: ")
    character = len(city)
    
    for letter in city:
        print(letter)

    print(f"The character size of {city} is: {character}")

    print(city[-1] + city[-2] + city[-3])

if __name__ == "__main__":
    main()



city = input("Enter a city here: ")

count = 0

while count < len(city):
    print(city[count + 1])
    count += 1


city = input("Enter a city here: ")

count = 0

for ch in city:
    if count < len(city):
        print(city[count])
        count += 1
'''

sentence = "This is a rainy day. Please be aware!"

new_sentence = sentence.replace("rainy", "sunny")

print(new_sentence)