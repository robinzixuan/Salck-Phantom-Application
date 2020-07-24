"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'list_channels_1' block
    list_channels_1(container=container)

    return

def list_channels_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('list_channels_1() called')

    parameters = []

    phantom.act("list channels", parameters=parameters, assets=['slack_splunk'], callback=custom_function_2, name="list_channels_1")

    return

def custom_function_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('custom_function_2() called')
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.sourceUserName', 'artifact:*.id'])
    container_item_0 = [item[0] for item in container_data]

    custom_function_2__outputs = None

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...
    outputs = "{}".format(container_item_0[0])

    ################################################################################
    ## Custom Code End
    ################################################################################

    phantom.save_run_data(key='custom_function_2:outputs', value=json.dumps(custom_function_2__outputs))
    format_2(container=container)

    return

def format_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('format_2() called')
    
    template = """Hi {0}:
There are some channels:
{1}"""

    # parameter list for template variable replacement
    parameters = [
        "custom_function_2:custom_function:outputs",
        "list_channels_1:action_result.data.*.channels.*.name",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_2")

    send_message_2(container=container)
    send_email_1(container=container)
    playbook_local_Test_AD_to_Slack_notification_1(container=container)
    prompt_1(container=container)

    return

def send_message_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('send_message_2() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'send_message_2' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.sourceUserName', 'artifact:*.id'])
    formatted_data_1 = phantom.get_format_data(name='format_2')

    parameters = []
    
    # build parameters list for 'send_message_2' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'destination': container_item[0],
                'message': formatted_data_1,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act("send message", parameters=parameters, assets=['slack_splunk'], name="send_message_2")

    return

def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('send_email_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'send_email_1' call
    formatted_data_1 = phantom.get_format_data(name='format_2')

    parameters = []
    
    # build parameters list for 'send_email_1' call
    parameters.append({
        'body': formatted_data_1,
        'from': "rluo@splunk.com",
        'attachments': "",
        'to': "rluo@splunk.com",
        'cc': "",
        'bcc': "",
        'headers': "",
        'subject': "",
    })

    phantom.act("send email", parameters=parameters, assets=['smtp'], name="send_email_1")

    return

def playbook_local_Test_AD_to_Slack_notification_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('playbook_local_Test_AD_to_Slack_notification_1() called')
    
    # call playbook "local/Test - AD to Slack notification", returns the playbook_run_id
    playbook_run_id = phantom.playbook("local/Test - AD to Slack notification", container=container)

    return

def prompt_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('prompt_1() called')
    
    # set user and message variables for phantom.prompt call
    user = "rluo@splunk.local"
    message = """input something?"""

    #responses:
    response_types = [
        {
            "prompt": "",
            "options": {
                "type": "list",
                "choices": [
                    "Yes",
                    "No",
                ]
            },
        },
    ]

    phantom.prompt2(container=container, user=user, message=message, respond_in_mins=5, name="prompt_1", response_types=response_types, callback=format_3)

    return

def format_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('format_3() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "prompt_1:action_result.parameter.message",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_3")

    send_message_3(container=container)

    return

def send_message_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('send_message_3() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'send_message_3' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.sourceUserName', 'artifact:*.id'])
    formatted_data_1 = phantom.get_format_data(name='format_3')

    parameters = []
    
    # build parameters list for 'send_message_3' call
    for container_item in container_data:
        if container_item[0]:
            parameters.append({
                'destination': container_item[0],
                'message': formatted_data_1,
                # context (artifact id) is added to associate results with the artifact
                'context': {'artifact_id': container_item[1]},
            })

    phantom.act("send message", parameters=parameters, assets=['slack_splunk'], name="send_message_3")

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return