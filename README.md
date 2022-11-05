# RocketData-test
My test project for a RocketData company.


## Installation
For project installation you should enter:

    git clone git@github.com:eeeelya/RocketData-test.git

## Launch

    cd sales_network 
    chmod +x entrypoint.sh
    sudo docker-compose up --build

After that you can create a superuser.

    sudo docker exec -it web_server python manage.py createsuperuser

## Database seeding

If you want to create test data for database, you must do the following steps.

    sudo docker exec -it web_server python manage.py shell 
    
    # this code create 100 objects of sales network
    >>> from element.factories.element_model import ElementFactory
    >>> ElementFactory.create_batch(100)

    # this code create 300 products for objects of sales network
    >>> from element.factories.element_products_model import ElementProductsFactory
    >>> ElementProductsFactory.create_batch(300)

    # this code create 50 employees for objects of sales network
    >>> from element.factories.element_employees_model import ElementEmployeesFactory
    >>> ElementEmployeesFactory.create_batch(50)

## Usage 

You can access the application by this url
    
    http://localhost:8000/

If you want to know more about API:

    http://localhost:8000/swagger/ 
    or     
    http://localhost:8000/redoc/ 
