from rest_framework.routers import DefaultRouter

from .views import (GenderViewSet, CommitteeViewSet, PositionsViewSet,
                    UniversitiesViewSet, CommitteeGroupViewSet, SpeakersViewSet)


router = DefaultRouter()

router.register('gender', GenderViewSet)
router.register('committee-group', CommitteeGroupViewSet)
router.register('positions', PositionsViewSet)
router.register('universities', UniversitiesViewSet)
router.register('committee', CommitteeViewSet)
router.register('speakers', SpeakersViewSet)

urlpatterns = router.urls
