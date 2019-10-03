from django.db.models import QuerySet, Q


class UserQuerySet(QuerySet):
    def filter_by_user(self, user):
        from participant.models import Organization

        if not user.is_superuser:
            return self.filter(
                organization__in=Organization.objects.filter_by_user(user=user)
            )
        return self