# myapp/handlers.py
from django.contrib.sessions.models import Session

def user_logged_in_handler(user, request):
    # Get or create session object
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)

    # Store login message in session
    request.session['login_message'] = f"User {user.username} has logged in."


