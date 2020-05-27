# Developer Portal and API Gateway

This project is a ready to use developer portal and API gateway, built using Django and React. A live demo is hosted at https://shrouded-eyrie-25569.herokuapp.com/

You can provide developers access to your API by adding your backend endpoints and choosing a name for your API. The project currently supports basic auth (username and password) and key auth (API token) as authentication methods for APIs. You can choose to have no authentication in place as well.

Documentation for your portal is auto generated based on your Swagger file. The project uses Redoc to generate the documentation page. The default Swagger file is set to "https://petstore.swagger.io/v2/swagger.json". This can be changed in tunnel/frontend/src/containers/Docs.js

It uses the Django Rest Framework and rest-auth for the backend user authentication. The frontend uses react redux for user authentication by storing the token in localstorage. A separate server for frontend is not required. The React code is compiled into the main.js file using webpack and is served by the backend Django server.

This project uses sqlite3 as its database by default. You can change the database configuration in the tunnel/tunnel/settings.py file

```json
cd Tunnel
virtualenv env
env\Scripts\activate.bat
pip install -r requirements.txt
npm install
cd tunnel
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

If you make changes to the React code in the frontend folder, recompile the JS by running the following command from the root folder

```json
npm run dev
```

To add your APIs, login to the admin panel at http://localhost:8000/admin using the credentials of the superuser you created. Provide your backend base url and specify an api name and choose an authentication method.

Set your throttling values for anonymous users and authenticated users.
Anonymous users are tracked based on their IP address, while authenticated users are tracked based on their API key.

The proxy endpoint exposed is the domainname/service/{api_name}/{uri_endpoint}.
For example, if the domain for your portal and gateway is 'https://apiproxy.com' and the api_name is 'microposts' and the API consumer would like to access /posts/1 from your backend service, the proxy endpoint would be https://apiproxy.com/service/microposts/posts/1

For developers to get an API key to consumer your API, they would have to signup on the portal at http://localhost:8000/signup

To consumer the API, add token in the header. For example, in Postman, choose API Key as the authorization and set the value to 'Token {apitoken}

If you are interested in a hosted version of this project, please leave your email here https://karthikve.typeform.com/to/Foo8hI
