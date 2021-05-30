from types import new_class
from jira import JIRA
from cfg import api_user, api_key, api_server


class JiraQuery:
    # Connector to jira API

    def __init__(self):
        self.jira_options = {'server': api_server}
        self.jira = JIRA(options=self.jira_options, basic_auth=(api_user, api_key))
        self.project_key = 'RU'
        # self.work_date = '2021-05-28'
        self.jql = 'project = ' + self.project_key  # + ' AND  worklogDate >= ' + self.work_date

    def getIssueList(self):
        # Get issue list from jql query
        return self.jira.search_issues(self.jql)

    def printIssueList(self):
        print(issues_list)

    def getIssue(self):
        print('Start ')
        jira = self.jira
        issues_list = jira.search_issues(self.jql)
        result = []
        if issues_list:
            for item in issues_list:
                issue = jira.issue(item)
                result.append(issue.fields.project.key)
                print(issue.fields.project.key, issue.fields.issuetype.name, issue.fields.reporter.displayName)
        else:
            'no data'
            # jira.add_comment(issue, 'new comment')
            # print(jira.comments(issue))


j = JiraQuery()
j.jql = 'project = DESK'
j.getIssue()