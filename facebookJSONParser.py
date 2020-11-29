import json

# Constants
ME = "Keith Chua"
test_path = "messages/facebook/json/message_short.json"

# Assumes two people in conversation and returns each messages as a list
def get_lists_of_messages(filepath, my_messages, other_person_messages):
    file = open(filepath)
    data = json.load(file)

    for i in range(len(data['messages'])):
        content = data['messages'][i]['content']
        sender = data['messages'][i]['sender_name']
        my_messages.append(content) if sender == ME else other_person_messages.append(content)

    file.close()
    return my_messages, other_person_messages

# a, b = get_lists_of_messages(test_path, [u"testing some my messages"], [u"testing some other person messages"])
# print(a)
# print(b)
