**Python Assignment**

Create an address book application where API users can create, update and delete addresses.

The address should:
  - contain the coordinates of the address.
  - be saved to an SQLite database.
  - be validated

API Users should also be able to retrieve the addresses that are within a given distance and location coordinates.

*Important : The application does not need a GUI. (Built-in FastAPI’s Swagger Doc is sufficient)*

-----

**Step by Step Solution**
-
-----
**_Note_:**

  **Latitude:**
  
  North: Positive values (0 to +90 degrees).
  
  South: Negative values (0 to -90 degrees).
  
  **Longitude:**
  
  East: Positive values (0 to +180 degrees).
  
  West: Negative values (0 to -180 degrees).

-----

1. Clone or download the repository on your machine

2. Create a virtual environment

    Creating virtual environment is important to ensure that all the necessary libraries can be installed there to run a specific project
  
       python -m venv <virtual_environment_name>

3. Activate virtual environment with the following command in the terminal

       <virtual_environment_name>\Scripts\activate   

4. Install all the dependencies from requirements.txt file

       pip install -r requirements.txt 

5. Go inside the app directory and execute FastAPI application - main.py

       uvicorn main:app


6. On success go to the link in the terminal {for me it is http://127.0.0.1:8000}

   ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/4ef15afd-8e40-4161-9cb0-1096118dd5c2)

7. To Open Swagger application add "/docs" to the link and search on any search engine

   http://127.0.0.1:8000/docs

  You should able to see the below page with apis

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/a980c0db-e878-4df5-8f27-906f25bf7fa4)

8. There are 4 apis:
    i. addAddress
    ii. addresses/{address_id}
    iii. deleteAddress/{address_id}
    iv. getAddressesByDistance

**To execute apis**

- Expand the api

- Click on Try it out to execute the api then provide the details

**addAddress**
 -
 
  **It is a POST method to insert the new address with coordinates to the table in the database**
  
  Provide these details and execute it 
  
  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/b0f3c29f-a609-47a1-9a88-8ec6ff789706)

  On Successful execution:
  
  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/a10ad151-58cb-4ff1-aa82-ecef250319e4)

  If there are some input datatype missmatch or incorrect coordinates it will throw the respective errors:

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/f5438ea4-492e-4282-8a84-a5bbaa6a6efb)

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/f6344e90-2202-42dc-914a-cdb04e710a97)

**addresses/{address_id}**
-

  **It is a PUT method to update the existing address in the table**

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/69bebcb3-ad4c-46f9-9fae-a08628b35cf9)

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/8457cf13-fb87-4413-9022-bcf84279356e)


**deleteAddress/{address_id}**
-

  **It is a DELETE method to delete the existing address from the table**

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/9390348d-51c3-4074-ae60-838906127d8a)

  If there are no records with the given id then response will be:
    
    "Address id not found"
  
  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/130d7ec1-f78e-47ee-80bf-db95e69f2d98)

**getAddressesByDistance**
-

  **This is a POST method which will give the addresses within the range of given latitude and longitude with the provided distance**

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/e288c5b6-aa70-4da8-a480-789aee9c997c)

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/537b5a20-b707-4697-a84d-f19fd3531b46)

  If there are no records it will give: 
    
    "No addresses found in the given range!"

  ![image](https://github.com/devang1218/Python-Assignment/assets/46046916/6dbf8c23-3731-453e-99a4-5944e2e83e18)
