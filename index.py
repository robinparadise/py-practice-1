# Main concepts of strings, numbers, booleans, and lists in Python:
# check lessons 07, 08 from py-foundations


story = """Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA, a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.

Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad."""

# String

'''
Exercise 1
Create a Python program that counts the number of characters
in the provided story (including spaces and punctuation).
'''
character_count = 0 # write your code here
print("Number of characters in the story:", character_count)

# Numbers

'''
Exercise 2:** Calculate the number of YEARS until 2045.
Use the variable `year` to store the current year.
'''
year = 2023 # get current year
years_left = 0 # write your code here
print("Number of years left:", years_left)

'''
Exercise 3:** Calculate the number of DAYS until 2045.
'''
days_left = 0 # write your code here
print("Number of days left:", days_left)

# 3. Booleans

'''
Exercise 4:** Check if the word "IA" is includes in the story.
'''
ia_in_story = False # write your code here
if (ia_in_story):
  print("The word 'IA' is in the story")
else:
  print("The word 'IA' is not in the story")

# 4. Lists

'''
Exercise 5:** Create a list of the words in the story and print the first 10 words.
'''
words = [] # write your code here
print("First 10 words in the story:", words)

'''
Exercise 6:** Create a list of the words in the story and print the last 10 words.
'''
print("Last 10 words in the story:", words)

'''
Exercise 7:** Create a list of the words in the story and print the words in the 10th to 20th position.
'''
print("Words in the 10th to 20th position:", words)

'''
Exercise 8:** Count the number of times the word "Javier" appears in the story.
'''
javier_count = 0 # write your code here
print("Number of times the word 'Javier' appears in the story:", javier_count)

'''
Exercise 9:** Replace the word "Javier" with "Pepito" in the story.
'''
story2 = "" # write your code here
print("Story with 'Javier' replaced with 'Pepito':", story2)

'''
Exercise 10:** Reverse the order of the words in the story.
'''
story3 = "" # write your code here
print("Story with words reversed:", story3)

'''
Exercise 11:** write story to a file with a parameterized name.
'''

def writeFile(story, file_name):
  with open(file_name, "w") as f:
    f.write(story)