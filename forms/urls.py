from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('login', views.login_view, name="login"),
    #path('register', views.register, name="register"),
    #path('logout', views.logout_view, name="logout"),
    path('create', views.create_form, name="create_form"),
    path('create/contact', views.contact_form_template, name="contact_form_template"),
    path('create/feedback', views.customer_feedback_template, name="customer_feedback_template"),
    path('create/event', views.event_registration_template, name="event_registration_template"),
    path('<str:code>/edit', views.edit_form, name="edit_form"),
    path('<str:code>/edit_title', views.edit_title, name="edit_title"),
    path('<str:code>/edit_description', views.edit_description, name="edit_description"),
    path('<str:code>/edit_background_color', views.edit_bg_color, name="edit_background_color"),
    path('<str:code>/edit_text_color', views.edit_text_color, name="edit_text_color"),
    path('<str:code>/edit_setting', views.edit_setting, name="edit_setting"),
    path('<str:code>/delete', views.delete_form, name="delete_form"),
    path('<str:code>/edit_question', views.edit_question, name="edit_question"),
    path('<str:code>/edit_choice', views.edit_choice, name="edit_choice"),
    path('<str:code>/add_choice', views.add_choice, name="add_choice"),
    path('<str:code>/remove_choice', views.remove_choice, name="remove_choice"),
    path('<str:code>/get_choice/<str:question>', views.get_choice, name="get_choice"),
    path('<str:code>/add_question', views.add_question, name="add_question"),
    path('<str:code>/delete_question/<str:question>', views.delete_question, name="delete_question"),
    path('<str:code>/score', views.score, name="score"),
    path('<str:code>/edit_score', views.edit_score, name="edit_score"),
    path('<str:code>/answer_key', views.answer_key, name="answer_key"),
    path('<str:code>/feedback', views.feedback, name="feedback"),
    path('<str:code>/viewform', views.view_form, name="view_form"),
    path('<str:code>/full_form', views.FormAPI.as_view({'get': 'retrieve'}), name="full_form"),
    path('<str:code>/submit', views.submit_form, name="submit_form"),
    path('submit_form', views.SubmitFormAPI.as_view(), name="submit_full_form"),
    path('<str:code>/responses', views.responses, name='responses'),
    path('<str:code>/response/<str:response_code>', views.response, name="response"),
    path('<str:code>/response/<str:response_code>/edit', views.edit_response, name="edit_response"),
    path('<str:code>/responses/delete', views.delete_responses, name="delete_responses"),
    path('send_responses', views.SendResponses.as_view(), name="send_responses"),
    path('403', views.FourZeroThree, name="403"),
    path('404', views.FourZeroFour, name="404")
]