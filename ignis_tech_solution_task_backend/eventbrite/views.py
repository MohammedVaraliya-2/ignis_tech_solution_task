from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Event
from .serializer import ReactEventSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Register new user and create token.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')   
        if not username or not password or not email:
            return Response({'error': 'Please provide all required fields.'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken.'}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, email=email, password=password)
        token = Token.objects.create(user=user)
        return Response({'success': 'User registered successfully.', 'token': token.key}, status=status.HTTP_201_CREATED)

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        """
        Authenticate user and return token.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)

class EventListAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        """
        List all events.
        """
        events = Event.objects.all()
        serializer = ReactEventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)

class CreateEventAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        """
        Create new event.
        """
        serializer = ReactEventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ToggleEventLikeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, *args, **kwargs):
        """
        Toggle event like status.
        """
        try:
            event = Event.objects.get(pk=pk, user=request.user)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found.'}, status=status.HTTP_404_NOT_FOUND)
        event.is_liked = not event.is_liked
        event.save()
        return Response({'success': 'Event like status updated successfully.'})
