from rest_framework.routers import SimpleRouter
from .views import UserViewSet, PersonalViewSet, DetailsViewSet, LocationViewSet, NameViewSet, ContactsViewSet, PaymentViewSet, PlanViewSet, DirectorViewSet, GenreViewSet, SoapViewSet, MovieViewSet, ReleaseViewSet

router = SimpleRouter()

router.register("User", UserViewSet)
router.register("Personal", PersonalViewSet)
router.register("Details", DetailsViewSet)
router.register("Location", LocationViewSet)
router.register("Name", NameViewSet)
router.register("Contacts", ContactsViewSet)
router.register("Payment", PaymentViewSet)
router.register("Plan", PlanViewSet)
router.register("Director", DirectorViewSet)
router.register("Genre", GenreViewSet)
router.register("Soap", SoapViewSet)
router.register("Movie", MovieViewSet)
router.register("Release", ReleaseViewSet)

urlpatterns = router.urls
