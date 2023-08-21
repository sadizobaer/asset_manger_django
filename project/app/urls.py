from django.urls import path
from .views import (
    RegisterUser,
    UpdateAsset,
    AllAssigned,
    AllUnassigned,
    HandleReturnRequest,
    AssignRequest,
    AssignedToUser,
    ReturnRequest,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    # authentication apis
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterUser.as_view(), name="register_user"),
    # updating Asset
    path("update/<int:pk>/", UpdateAsset.as_view(), name="update_asset"),
    # admin site
    path("all_assigned/", AllAssigned.as_view(), name="admin_all_assigned"),
    path("all_unassigned/", AllUnassigned.as_view(), name="admin_all_unassigned"),
    path("handle_return/", HandleReturnRequest.as_view(), name="handle_return_request"),
    # user site
    path("assign_request/", AssignRequest.as_view(), name="assigned_request_to_user"),
    path("assigned_to_user/", AssignedToUser.as_view(), name="accepted_by_user"),
    path("return_request/", ReturnRequest.as_view(), name="user_return_request"),
]
