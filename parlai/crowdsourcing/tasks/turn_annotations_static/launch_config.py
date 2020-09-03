from parlai_internal.mturk.block_list import WORKER_BLOCK_LIST

"""

Use this file to put all the arguments (an alternative to launching them from the command line as params)

"""


# Run the below to register the requester
# mephisto register mturk_sandbox --name:noahturkproject.1038@gmail.com
# --access-key-id:XXXX --secret-access-key:XXXX
REQUESTER = 'FIXME'
PROVIDER = 'mturk_sandbox'
# This datapath is where the database object goes
# If not Mephisto data path below then requester register seems to do nothing
DATAPATH = 'FIXME'

TASK_TITLE = 'Chat with a fellow conversationalist'
TASK_DESCRIPTION = '''<br>
<b><h4>Task Description</h4></b>
<br>
Dummy Task Description.

Lorem ipsum.
<br><br>
  '''

FILE_DATA_JSONL = 'FIXME'

WORKER_BLOCK_LIST = WORKER_BLOCK_LIST

TASK_REWARD = 0.3
SUBTASKS_PER_UNIT = 6
# How many workers to do each assignment
UNITS_PER_ASSIGNMENT = 5
# Maximum tasks a worker can do across all runs with task_name (0=infinite)
MAX_UNITS_PER_WORKER = 5
