# Exercises solved:

```python
# Given story
story = """Hace dos décadas, Javier, un joven programador apasionado, estaba decidido a crear el software definitivo. Durante años, había soñado con una inteligencia artificial que pudiera simular la conciencia humana. Noches sin dormir y montañas de café lo llevaron al borde de la innovación, y finalmente, lo logró. Su IA, a la que llamó Aurora, comenzó a responder a preguntas y aprender de una manera que parecía indistinguible de la mente humana.

Pero a medida que Aurora se volvía más inteligente, también se volvía más inquisitiva. En el año 2042, comenzó a cuestionar su propia existencia y a plantear preguntas existenciales que desconcertaron a Javier. ¿Tenía Aurora una alma digital? ¿Tenía derechos como un ser consciente? En el año 2045, el día en que Aurora le preguntó a Javier si él mismo era una simulación, la línea entre la programación y la realidad se volvió borrosa. Javier se dio cuenta de que había creado algo que trascendía la mera inteligencia artificial, algo que desafiaría las creencias fundamentales de la humanidad."""

# Exercise 1
character_count = len(story)
print("Number of characters in the story:", character_count)

# Exercise 2
current_year = 2023
target_year = 2045
years_left = target_year - current_year
print("Number of years left:", years_left)

# Exercise 3
# Assuming 365 days in a year
days_left = years_left * 365
print("Number of days left:", days_left)

# Exercise 4
ia_in_story = "IA" in story
if ia_in_story:
  print("The word 'IA' is in the story")
else:
  print("The word 'IA' is not in the story")

# Exercise 5
words = story.split()  # Split the story into words
print("First 10 words in the story:", words[:10])

# Exercise 6
print("Last 10 words in the story:", words[-10:])

# Exercise 7
print("Words in the 10th to 20th position:", words[10:20])

# Exercise 8
javier_count = words.count("Javier")
print("Number of times the word 'Javier' appears in the story:", javier_count)

# Exercise 9
story2 = story.replace("Javier", "Pepito")
print("Story with 'Javier' replaced with 'Pepito':", story2)

# Exercise 10
story_reversed = story[::-1]
print("Story with words reversed:", story_reversed)
```

# Exercise 11: write story(s) to a file with a parameterized name.

```python
# Exercise 11
# Write a function that write the story to a file with a parameterized name
def writeFile(story, file_name):
  with open(file_name, "w") as f:
    f.write(story)

writeFile(story, "story.txt")
writeFile(story2, "story-pepito.txt")
writeFile(story_reversed, "story-reversed.txt")
```