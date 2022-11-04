from jira import JIRA
options = {'server': 'https://[instance_name].atlassian.net'}
jira = JIRA(options, basic_auth=('unknown@unknown.com', 'unknown '))