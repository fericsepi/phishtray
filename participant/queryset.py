from django.db.models import QuerySet
from users.models import User


class OrganizationQuerySet(QuerySet):
    def filter_by_user(self, user):
        if not user or not isinstance(user, User):
            return self.none()

        if user.is_superuser:
            return self

        return self.filter(id=user.organization_id)


class ParticipantQuerySet(QuerySet):
    def filter_by_user(self, user):
        from .models import Organization

        if not user.is_superuser:
            return self.filter(
                organization__in=Organization.objects.filter_by_user(user=user)
            )
        return self
