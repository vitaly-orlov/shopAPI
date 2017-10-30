from rest_framework import filters


class VisibleFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(visible=True)
