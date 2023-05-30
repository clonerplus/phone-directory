# Data Structure Project 📚📝🔍🗑️<br>

## Phone directory application using doubly-linked lists<br>

#### For such purpose these operations are implemented:

- 📝👉 **Command line interface:**<br>
  User should be able to return to the main menu from each part of the application (1, 2, 3) by pressing the Esc key on the keyboard. Another alternative way for such purpose can write the ‘back’ word as the input and hit `return`, but the first way is preferable. By selecting the 4th option from the menu, the application should be terminated completely.

```
Enter your command:
1- Add new contact.
2- Delete existing contact.
3- Search for a contact.
4- Exit.
```

- 📝👉 **Insertion operator:**<br>
  At the first step you should create the suitable data structure based on contact information using doubly-linked lists. The contact information includes the name and number of the contact.I have implemented an insertion procedure (function) to get new contact information as input and add it in the doubly-linked lists in alphabet order. In other words, the order of the information in the contact book must always be maintained.
  The example of insertion interface is shown as follows:

```
1- Enter contact name and number:
(e.g., Hana 09134567890)
```

- 📝👉 **Delete operator:**<br>
  Simply create a deletion procedure to find and delete the contact matching with the contact’s name which is
  entered as an input. You should obviously provide the proper interface as follows:

```
2- Enter the contact’s name to delete:
(e.g., Hana)
```

In the case of not finding the input name, following message should be printed:

```
There is no contact with the entered name!
```

Otherwise, it should print bellow message:

```
The contact deleted successfully.
```

- 📝👉 **Search operator:**<br>
  As mentioned before, the unique feature of the contact application is the updating result based on the search query. For this purpose, you should delete and reprint the new search result by each change in the search query. If no contact is found, the program should print the message “No contact is found!”. The result of search query should print as follows:

```
3- Searching for contact: a
Ali 0912...
Abbas 0913...
Ahlam 0914...

3- Searching for contact: ab
Abbas 0913...

3- Searching for contact: abc
No contact is found!
```

In the case that you could not handle the dynamic updatable search result format, you can simply print the result of the updated query at the end of previous result as follows, but you won’t get the full mark of this section:

```
3- Searching for contact: ab
Ali 0912...
Abbas 0913...
Ahlam 0914...
#######################
Abbas 0913...
```
