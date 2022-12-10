from django.urls import path

from bank_store.views import ifsc, index,branchesData, insert,data,delete

urlpatterns = [
	#Leave as empty string for base url
	path('', index, name="home"),
	path('ifsc/',ifsc),
	path('branches_data/',branchesData),
	path('insert_data/',insert),
	path('data/',data),
	path('delete/',delete),


]

"""
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

"""