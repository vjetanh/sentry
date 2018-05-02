from __future__ import absolute_import
from sentry.tagstore.base import TagKeyStatus


class TagKey(object):
    def __init__(self, key, values_seen, status=TagKeyStatus.VISIBLE):
        self.key = key
        self.values_seen = values_seen
        self.status = status

    def __repr__(self):
        return '<%s: %r>' % (type(self).__name__, vars(self))


class TagValue(object):
    def __init__(self, key, value, times_seen, first_seen, last_seen):
        self.key = key
        self.value = value
        self.times_seen = times_seen
        self.first_seen = first_seen
        self.last_seen = last_seen

    def __repr__(self):
        return '<%s: %r>' % (type(self).__name__, vars(self))


class GroupTagKey(object):
    def __init__(self, group_id, key, values_seen):
        self.group_id = group_id
        self.key = key
        self.values_seen = values_seen

    def __repr__(self):
        return '<%s: %r>' % (type(self).__name__, vars(self))


class GroupTagValue(object):
    def __init__(self, group_id, key, value, times_seen, first_seen, last_seen):
        self.group_id = group_id
        self.key = key
        self.value = value
        self.times_seen = times_seen
        self.first_seen = first_seen
        self.last_seen = last_seen

    def __repr__(self):
        return '<%s: %r>' % (type(self).__name__, vars(self))


from sentry.api.serializers import Serializer, register


@register(TagKey)
class TagKeySerializer(Serializer):
    def serialize(self, obj, attrs, user):
        from sentry import tagstore

        return {
            'key': tagstore.get_standardized_key(obj.key),
            'name': tagstore.get_tag_key_label(obj.key),
            'uniqueValues': obj.values_seen,
        }


@register(TagValue)
class TagValueSerializer(Serializer):
    def serialize(self, obj, attrs, user):
        from sentry import tagstore

        return {
            'key': tagstore.get_standardized_key(obj.key),
            'name': tagstore.get_tag_value_label(obj.key, obj.value),
            'value': obj.value,
            'count': obj.times_seen,
            'lastSeen': obj.last_seen,
            'firstSeen': obj.first_seen,
        }


@register(GroupTagKey)
class GroupTagKeySerializer(Serializer):
    def serialize(self, obj, attrs, user):
        from sentry import tagstore

        return {
            'name': tagstore.get_tag_key_label(obj.key),
            'key': tagstore.get_standardized_key(obj.key),
            'uniqueValues': obj.values_seen,
        }


@register(GroupTagValue)
class GroupTagValueSerializer(Serializer):
    def serialize(self, obj, attrs, user):
        from sentry import tagstore

        return {
            'name': tagstore.get_tag_value_label(obj.key, obj.value),
            'key': tagstore.get_standardized_key(obj.key),
            'value': obj.value,
            'count': obj.times_seen,
            'lastSeen': obj.last_seen,
            'firstSeen': obj.first_seen,
        }
