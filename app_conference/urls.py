from rest_framework.routers import DefaultRouter

from .views import ConferenceAgendaViewSet, ConferenceDaysViewSet, SponsorPartnerViewSet

router = DefaultRouter()

router.register('conference-agenda', ConferenceAgendaViewSet)
router.register('conference-days', ConferenceDaysViewSet)
router.register('sponsor-partner', SponsorPartnerViewSet)

urlpatterns = router.urls
