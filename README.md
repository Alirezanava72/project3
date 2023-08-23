![GA Logo](./images/)
# Project 3 - UniMate
By team of [Alireza](https://github.com/Alirezanava72),[Miya Miah](https://github.com/miya-w)
## Overview

The third project of the software engineering immersive course at GA Australia. The assignment was to create a full-stack application with Python, Django, SQL. This project was completed in a team of 2 within a week.
About **UniMate**. It’s a platform is designed for university students seeking hassle-free accommodation solutions. Whether you're on the hunt for the perfect shared room or looking for a compatible housemate to share your space with.

## Table of Contents
1. [Brief](#Project-Brief)
2. [Technologies used](#Technologies-Used)
3. [Approach](#Approach)
    - [Planning](#Planning)
    - [Back-end](#Back-end)
    - [A Journey](#A-Journey)
    - [Front-end](#Front-end)
- [Challenges and Lessons Learned](#Challenges-and-Lessons-Learned)
- [Victories](Victories)
- [Future Features and Improvements](#Future-Features-and-Improvements)
- [Credit](#Credit) 

## Project Brief
- Build a full-stack application

## Technologies Used

* HTML
* CSS
* JavaScript
* Python
* Django
* SQL

## Approach

### Planning
We began our project with a general discussion of our ideas and quickly agreed to make a website we both are interested in -- a property rental website. For having a different niche in the market, we want to create a platform exclusively for uni students searching for a room or roommate in Australia.

So, these are the functions needs to meet the needs

- As a user, I want to add the room for renting 
- As a user, I want to share the amenities the property provides.
- As a user, I want to see the list of the renting room.
- As a user, I want to see the lease date.

#### Figma and Trello
![]()

#### MVT (Model View Template)

Our first goal to work toward was our MVT, so we planned out what we would ideally like to have in the initial working version of our application:
---
# Back end:
---
Since our application is built around various types of property listings, each with its specific attributes, we have established a set of diverse models. These models include Property, Amenity, and Renting, alongside the central user model, to form the core of our backend infrastructure.
## Models: 

In our “models.py” file, we have defined three models:
Amenity: This model represents different amenities that a property can have, like features or facilities. Each amenity is described by its name.

```python
class Amenity(models.Model):
  name = models.CharField(max_length=100)
```

Property: This model represents a property listing with various attributes such as title, address, suburb, state, postcode, details, price, and a    Many-to-Many relationship with amenities.

```python
class Property(models.Model):
  title = models.CharField(max_length=50)
  address = models.TextField(max_length=200)
  suburb = models.CharField(max_length=50)
  state = models.CharField(max_length=3)
  postcode = models.IntegerField()
  details = models.TextField(max_length=200)
  price = models.IntegerField()
  amenities = models.ManyToManyField(Amenity)
```


Renting: This model represents a renting option associated with a specific property. It includes details such as the available date and purpose (house sharing, room sharing, entire property).

```python
class Renting(models.Model):
    available_date = models.DateField('availability Date')
    purpose = models.CharField(
      max_length=1,
      choices=PURPOSES,
      default=PURPOSES[0][0]
      )

```
## Views:

In “views.py” file, we defined various view functions and class-based views to handle different actions and interactions with the above models:
### home and about: 
Render simple templates for the home and about pages.
### properties_index: 
Retrieve all properties from the database and render them on the index page.
### properties_detail:
 Retrieve detailed information about a specific property, including its associated amenities and a form to add a new renting option.
### PropertyAdd, PropertyUpdate, PropertyDelete: 
Class-based views for creating, updating, and deleting properties(full CRUD functionality).
add_renting: To handle adding a new renting option to a property.
### AmenityList, AmenityDetail, AmenityCreate, AmenityUpdate, AmenityDelete: 
Class-based views for listing amenities, showing individual amenity details, creating, updating, and deleting amenities(full CRUD functionality).
### assoc_amenity and unassoc_amenity:
To associate or disassociate an amenity with a property.
## URLs:

In “urls.py” file, we’ve defined URL patterns that map to the respective views for different actions and interactions:
URLs related to properties, including property detail, creation, updating, and deletion.
URLs related to renting options, including adding a new renting option.
URLs related to amenities, including listing amenities, showing details, creating, updating, and deleting amenities.
## Forms:

“forms.py” file is defined with RentingForm class that inherits from ModelForm. This form is used for creating renting options associated with a property, allowing users to input the available date and purpose.</br>

Our Django project follows the Model-View-Template (MVT) architecture, where models represent data structures, views handle the logic and interactions, and templates render the user interface.This project focuses on managing property listings, associated amenities, and renting options through well-structured views and models. The provided URLs help to route requests to the appropriate views, and forms simplify the process of collecting user input for creating new renting options.
## DATABASES:

We have used PostgreSQL as the database backend which allows Django to establish a connection to the specified PostgreSQL database. 


---
### Front-end



## Challenges and Lessons Learned


## Wins


## Future Features and Improvements


### Resources
---
[Project 3 - brief]()