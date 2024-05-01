# Clearthought
## Make computer gibberish human readable

Clearthought is a tool that aims to helps 42 school students debug their programs after a correction by the Moulinette.

After every correction, we receive a "trace", which is an email showing us what tests were performed on our programs. This email can guide us to understand what went wrong and how to improve our code. Unfortunatly, the way it's formated makes it difficult to seperate useful informations from boring details. So most students don't bother with it.

So my goal with this project, is to make those computer generated emails, human readable. I will do so by removing non critical informations and creating visual hierarchy for better readability.

![Interface before-after](/docs/Thumbnail.jpg)

### To-do List
- [ ] implement the text_to_HTML function
- [ ] add an about page
- [ ] add a naviguation bar (home, about, github link)
- [ ] make responsive

### Improvements

- [ ] Handle every type of trace (shell scripts, file rights, C code,...)
- [ ] Show exercice title
- [ ] add success/failed icons
- [ ] Show points when exercice is a success
- [ ] Make the erros standout (Segmentation fault, Bus error, does not compile, Nothing turned in, timed-out, )
- [ ] use gmail's API to more easily retrieve traces
