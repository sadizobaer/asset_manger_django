from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .serializers import RegisterSerializer, AssetSrializer, AssignManagerSerializer
from .models import Asset, AssignManager

# Create your views here.


####========= authentication =============
class RegisterUser(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


####========= asset updating view =============
class UpdateAsset(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = AssignManager.objects.all()
    serializer_class = AssignManagerSerializer
    lookup_field = "pk"


####========= admin site views =============
class AllAssigned(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(is_accepted=True)


class AllUnassigned(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(is_accepted=False)


class HandleReturnRequest(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(request_to_return=True)


####========= user site views =============
class AssignRequest(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(assigned_to=self.request.user, request_to_accept=True)


class AssignedToUser(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(assigned_to=self.request.user, is_accepted=True)


class ReturnRequest(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    model = AssignManager
    serializer_class = AssignManagerSerializer

    def get_queryset(self):
        return AssignManager.objects.filter(assigned_to=self.request.user, request_to_return=True)
