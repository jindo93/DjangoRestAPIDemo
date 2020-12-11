from django.urls import path
import Prediction.views as views

urlpatterns = [
	path('add/', views.api_add, name = 'api_add'),
	# when a user sends a request starting with url http://127.0.0.1:8000/api/add/,
	# run the function 'api_add' in the views.py inside the Prediction app
	path('add_values/', views.Add_Values.as_view(), name = 'api_add_values'),
	path('predict/', views.IRIS_Model_Predict.as_view(), name = 'predict'),
]