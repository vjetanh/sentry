from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from sentry.integrations import Integration, IntegrationMetadata

from .client import JiraApiClient


alert_link = {
    'text': 'Visit the **Atlassian Marketplace** to install this integration.',
    # TODO(jess): update this when we have our app listed on the
    # atlassian marketplace
    'link': 'https://marketplace.atlassian.com/',
}

metadata = IntegrationMetadata(
    description='Sync Sentry and JIRA issues.',
    author='The Sentry Team',
    noun=_('Instance'),
    issue_url='https://github.com/getsentry/sentry/issues/new?title=JIRA%20Integration:%20&labels=Component%3A%20Integrations',
    source_url='https://github.com/getsentry/sentry/tree/master/src/sentry/integrations/jira',
    aspects={
        'alert_link': alert_link,
    },
)


class JiraIntegration(Integration):
    key = 'jira'
    name = 'JIRA'
    metadata = metadata

    can_add = False

    def get_pipeline_views(self):
        return []

    def get_client(self, instance):
        return JiraApiClient(
            instance.metadata['base_url'],
            instance.metadata['shared_secret'],
        )

    def get_issue(self, instance, issue_id):
        client = self.get_client(instance)
        issue = client.get_issue(issue_id)
        return {
            'title': issue['fields']['summary'],
            'description': issue['fields']['description'],
        }
