There is an insurance dataset and we have to predict the insurance premium category whether
low ,medium or high.

1. make the machine learning model 
2. the frontend of the model 
3. an api to connect the frontend and the model using fastapi

AFTER MAKING THE MODEL
After the ML model is made, then make the api in whcih i have to send the data from the user to 
the model, then find all the new features in the backend like bmi etc then after getting the output
send it back the frontend.

AFTER MAKING THE API AND THE frontend
Then make the model folder for the pkl file, for dockerizing afterwards the api has to be in a 
seperate folder 

After making the api
1. We have a problem in our api the when we enter the city we are not validating it. Means that 
we have divided the cities into different tiers like tier 1, tier 2, tier 3. so if the user even
enters lowercase letters that our included in the tier1, it will be included in the tier 3 so 
we have to validate all the fields
2. We have no home url like when the local host opens 8000/ and we have to go to specific endpoint
but it should be written that go to this endpoint instead of coming here
3. when hosting on amazon or using kubernetes, they say to end health_checkpoint endpoint so We
have to add that also
4. for checking the model version, we do this using MLFLOW but here i have to manually mention 
the model verion
5. we should have a seperate pydantic file for the data
6. city tier validation in different folder config
7. Seperate file for the api endpoints
8. seperate file for the output
9. always do the prediction in try catch block(try and exception)
10. now i want to mention confidence score also
11. We validated the input data earlier but we can also validate the output data using pydantic
12. Response Model in fastapi defines the structure of the data that api endpoint will return 